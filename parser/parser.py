"""
Analisador Sintático (Parser) para a linguagem Apollo
Implementa um parser recursivo descendente
"""

from typing import List, Optional
import sys
import os

# Adiciona o diretório lexer ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lexer'))

from lexer.apollo_lexer import ApolloLexer, TokenType, Token
import sys
import os

# Adiciona diretório atual ao path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from parser.ast import (
    ASTNode, Program, VarDeclaration, Block, Assignment, IfStatement, WhileStatement,
    WriteStatement, ReadNumberStatement, ReadTextStatement,
    BinaryOp, UnaryOp, IntegerLiteral, RealLiteral, StringLiteral,
    BooleanLiteral, Variable, FunctionCall, Type
)


class ParseError(Exception):
    """Exceção para erros de parsing"""
    
    def __init__(self, message: str, token: Token):
        self.message = message
        self.token = token
        super().__init__(f"{message} na linha {token.line}, coluna {token.column}")


class ApolloParser:
    """Parser recursivo descendente para Apollo"""
    
    def __init__(self, lexer: ApolloLexer):
        self.lexer = lexer
        self.current_token: Optional[Token] = None
        self.tokens: List[Token] = []
        self.position = 0
    
    def parse(self, source_code: str) -> Program:
        """Inicia o parsing do código-fonte"""
        # Tokeniza o código
        self.tokens = [t for t in self.lexer.tokenize(source_code) 
                      if t.type not in (TokenType.WHITESPACE, TokenType.COMMENT)]
        self.position = 0
        self.current_token = self.tokens[0] if self.tokens else None
        
        # Parse do programa
        program = self.parse_program()
        
        # Verifica se chegou ao fim
        if self.current_token and self.current_token.type != TokenType.EOF:
            raise ParseError(f"Token inesperado: {self.current_token.value}", self.current_token)
        
        return program
    
    def advance(self):
        """Avança para o próximo token"""
        self.position += 1
        if self.position < len(self.tokens):
            self.current_token = self.tokens[self.position]
        else:
            self.current_token = Token(TokenType.EOF, "", 0, 0)
    
    def expect(self, token_type: TokenType, value: Optional[str] = None):
        """Espera um token específico"""
        if not self.current_token:
            raise ParseError(f"Esperado {token_type.name}, mas chegou ao fim do arquivo", 
                          Token(TokenType.EOF, "", 0, 0))
        
        if self.current_token.type != token_type:
            raise ParseError(f"Esperado {token_type.name}, encontrado {self.current_token.type.name}",
                          self.current_token)
        
        if value and self.current_token.value != value:
            raise ParseError(f"Esperado '{value}', encontrado '{self.current_token.value}'",
                          self.current_token)
        
        token = self.current_token
        self.advance()
        return token
    
    def match(self, token_type: TokenType, value: Optional[str] = None) -> bool:
        """Verifica se o token atual corresponde ao tipo/valor esperado"""
        if not self.current_token:
            return False
        if self.current_token.type != token_type:
            return False
        if value and self.current_token.value != value:
            return False
        return True
    
    # ========== Parsing do Programa ==========
    
    def parse_program(self) -> Program:
        """Programa ::= algoritmo IDENT { Declaração* Comando* } fim_algoritmo"""
        line = self.current_token.line if self.current_token else 0
        column = self.current_token.column if self.current_token else 0
        
        # algoritmo
        self.expect(TokenType.KEYWORD, "algoritmo")
        
        # Nome do algoritmo (opcional)
        name = None
        if self.match(TokenType.IDENTIFIER):
            name = self.current_token.value
            self.advance()
        
        declarations: List[VarDeclaration] = []
        statements: List[ASTNode] = []
        
        # Parse declarações e comandos
        while self.current_token and self.current_token.type != TokenType.EOF:
            if self.match(TokenType.KEYWORD, "fim_algoritmo"):
                break
            
            # Tenta parsear declaração
            if self.match(TokenType.KEYWORD) and self.current_token.value in ("inteiro", "real", "texto", "logico"):
                decls = self.parse_declaration()
                declarations.extend(decls)
                continue
            
            # Tenta parsear comando
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
        
        # fim_algoritmo
        self.expect(TokenType.KEYWORD, "fim_algoritmo")
        
        return Program(declarations, statements, line, column)
    
    def parse_declaration(self) -> List[VarDeclaration]:
        """Declaração ::= tipo IDENT { , IDENT } ;"""
        if not self.match(TokenType.KEYWORD):
            return []
        
        type_keyword = self.current_token.value
        type_map = {
            "inteiro": Type.INTEGER,
            "real": Type.REAL,
            "texto": Type.TEXT,
            "logico": Type.BOOLEAN
        }
        
        if type_keyword not in type_map:
            return []
        
        var_type = type_map[type_keyword]
        line = self.current_token.line
        column = self.current_token.column
        self.advance()
        
        # Lista de variáveis
        variables: List[str] = []
        while True:
            if not self.match(TokenType.IDENTIFIER):
                break
            
            var_name = self.current_token.value
            variables.append(var_name)
            self.advance()
            
            if not self.match(TokenType.SYMBOL, ","):
                break
            self.advance()
        
        # Cria declarações para todas as variáveis
        declarations = []
        for var_name in variables:
            declarations.append(VarDeclaration(var_type, var_name, None, line, column))
        
        return declarations
    
    # ========== Parsing de Statements ==========
    
    def parse_statement(self) -> Optional[ASTNode]:
        """Statement ::= Assignment | IfStatement | WhileStatement | WriteStatement | ReadStatement"""
        if not self.current_token:
            return None
        
        line = self.current_token.line
        column = self.current_token.column
        
        # Atribuição
        if self.match(TokenType.IDENTIFIER):
            next_pos = self.position + 1
            if next_pos < len(self.tokens) and self.tokens[next_pos].type == TokenType.OPERATOR and self.tokens[next_pos].value == "=":
                return self.parse_assignment()
        
        # escreva
        if self.match(TokenType.KEYWORD, "escreva"):
            return self.parse_write_statement()
        
        # leia_numero como statement (sem atribuição)
        if self.match(TokenType.KEYWORD, "leia_numero"):
            # Verifica se é statement ou expressão
            next_pos = self.position + 1
            if next_pos < len(self.tokens) and self.tokens[next_pos].type == TokenType.SYMBOL and self.tokens[next_pos].value == "(":
                # É uma chamada de função, será tratada como expressão
                pass
            else:
                return self.parse_read_number_statement()
        
        # leia_texto como statement (sem atribuição)
        if self.match(TokenType.KEYWORD, "leia_texto"):
            # Verifica se é statement ou expressão
            next_pos = self.position + 1
            if next_pos < len(self.tokens) and self.tokens[next_pos].type == TokenType.SYMBOL and self.tokens[next_pos].value == "(":
                # É uma chamada de função, será tratada como expressão
                pass
            else:
                return self.parse_read_text_statement()
        
        # se
        if self.match(TokenType.KEYWORD, "se"):
            return self.parse_if_statement()
        
        # enquanto
        if self.match(TokenType.KEYWORD, "enquanto"):
            return self.parse_while_statement()
        
        # Ponto e vírgula vazio
        if self.match(TokenType.SYMBOL, ";"):
            self.advance()
            return None
        # Bloco explícito: { ... }
        if self.match(TokenType.SYMBOL, "{"):
            return self.parse_block()

        return None

    def parse_block(self) -> Block:
        """Parseia um bloco delimitado por `{` `}` e retorna um `Block`"""
        if not self.match(TokenType.SYMBOL, "{"):
            raise ParseError("Esperado '{' para início de bloco", self.current_token or Token(TokenType.EOF, "", 0, 0))

        line = self.current_token.line
        column = self.current_token.column
        # consome '{'
        self.advance()

        statements: List[ASTNode] = []

        # Continua parseando statements até encontrar '}' ou EOF
        while self.current_token and not self.match(TokenType.SYMBOL, "}"):
            if self.current_token.type == TokenType.EOF:
                raise ParseError("Fim de arquivo dentro de bloco (esperado '}')", self.current_token)

            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
            else:
                # Se parse_statement não consumiu token, avançar para evitar loop infinito
                # Isto evita travamentos em casos de tokens inesperados dentro do bloco
                if self.current_token and self.current_token.type != TokenType.EOF:
                    self.advance()

        # espera '}'
        self.expect(TokenType.SYMBOL, "}")

        return Block(statements, line, column)
    
    def parse_assignment(self) -> Assignment:
        """Assignment ::= IDENT = Expression ;"""
        if not self.match(TokenType.IDENTIFIER):
            raise ParseError("Esperado identificador", self.current_token)
        
        var_name = self.current_token.value
        line = self.current_token.line
        column = self.current_token.column
        self.advance()
        
        # =
        self.expect(TokenType.OPERATOR, "=")
        
        # Expression
        expr = self.parse_expression()
        
        return Assignment(var_name, expr, line, column)
    
    def parse_if_statement(self) -> IfStatement:
        """IfStatement ::= se Expression faca Statement { senao Statement }"""
        line = self.current_token.line
        column = self.current_token.column
        
        # se
        self.expect(TokenType.KEYWORD, "se")
        
        # Expression
        condition = self.parse_expression()
        
        # faca
        self.expect(TokenType.KEYWORD, "faca")
        
        # Then block
        then_block = self.parse_statement() or Block([], line, column)
        
        # senao (opcional)
        else_block = None
        if self.match(TokenType.KEYWORD, "senao"):
            self.advance()
            else_block = self.parse_statement() or Block([], line, column)
        
        return IfStatement(condition, then_block, else_block, line, column)
    
    def parse_while_statement(self) -> WhileStatement:
        """WhileStatement ::= enquanto Expression faca Statement"""
        line = self.current_token.line
        column = self.current_token.column
        
        # enquanto
        self.expect(TokenType.KEYWORD, "enquanto")
        
        # Expression
        condition = self.parse_expression()
        
        # faca
        self.expect(TokenType.KEYWORD, "faca")
        
        # Body
        body = self.parse_statement() or Block([], line, column)
        
        return WhileStatement(condition, body, line, column)
    
    def parse_write_statement(self) -> WriteStatement:
        """WriteStatement ::= escreva ( Expression { , Expression } ) ;"""
        line = self.current_token.line
        column = self.current_token.column
        
        # escreva
        self.expect(TokenType.KEYWORD, "escreva")
        
        # (
        self.expect(TokenType.SYMBOL, "(")
        
        # Expression list
        expressions: List[ASTNode] = []
        if not self.match(TokenType.SYMBOL, ")"):
            while True:
                expr = self.parse_expression()
                expressions.append(expr)
                
                if self.match(TokenType.SYMBOL, ","):
                    self.advance()
                else:
                    break
        
        # )
        self.expect(TokenType.SYMBOL, ")")
        
        return WriteStatement(expressions, line, column)
    
    def parse_read_number_statement(self) -> ReadNumberStatement:
        """ReadNumberStatement ::= leia_numero ( IDENT ) ;"""
        line = self.current_token.line
        column = self.current_token.column
        
        # leia_numero
        self.expect(TokenType.KEYWORD, "leia_numero")
        
        # (
        self.expect(TokenType.SYMBOL, "(")
        
        # IDENT
        if not self.match(TokenType.IDENTIFIER):
            raise ParseError("Esperado identificador", self.current_token)
        var_name = self.current_token.value
        self.advance()
        
        # )
        self.expect(TokenType.SYMBOL, ")")
        
        return ReadNumberStatement(var_name, line, column)
    
    def parse_read_text_statement(self) -> ReadTextStatement:
        """ReadTextStatement ::= leia_texto ( IDENT ) ;"""
        line = self.current_token.line
        column = self.current_token.column
        
        # leia_texto
        self.expect(TokenType.KEYWORD, "leia_texto")
        
        # (
        self.expect(TokenType.SYMBOL, "(")
        
        # IDENT
        if not self.match(TokenType.IDENTIFIER):
            raise ParseError("Esperado identificador", self.current_token)
        var_name = self.current_token.value
        self.advance()
        
        # )
        self.expect(TokenType.SYMBOL, ")")
        
        return ReadTextStatement(var_name, line, column)
    
    # ========== Parsing de Expressions ==========
    
    def parse_expression(self) -> ASTNode:
        """Expression ::= OrExpression"""
        return self.parse_or_expression()
    
    def parse_or_expression(self) -> ASTNode:
        """OrExpression ::= AndExpression { || AndExpression }"""
        left = self.parse_and_expression()
        
        while self.match(TokenType.OPERATOR, "||"):
            op = self.current_token.value
            self.advance()
            right = self.parse_and_expression()
            left = BinaryOp(op, left, right, left.line, left.column)
        
        return left
    
    def parse_and_expression(self) -> ASTNode:
        """AndExpression ::= RelExpression { && RelExpression }"""
        left = self.parse_rel_expression()
        
        while self.match(TokenType.OPERATOR, "&&"):
            op = self.current_token.value
            self.advance()
            right = self.parse_rel_expression()
            left = BinaryOp(op, left, right, left.line, left.column)
        
        return left
    
    def parse_rel_expression(self) -> ASTNode:
        """RelExpression ::= AddExpression [ (==|!=|<|>|<=|>=) AddExpression ]"""
        left = self.parse_add_expression()
        
        if self.match(TokenType.OPERATOR):
            op = self.current_token.value
            if op in ("==", "!=", "<", ">", "<=", ">="):
                self.advance()
                right = self.parse_add_expression()
                return BinaryOp(op, left, right, left.line, left.column)
        
        return left
    
    def parse_add_expression(self) -> ASTNode:
        """AddExpression ::= MulExpression { (+|-) MulExpression }"""
        left = self.parse_mul_expression()
        
        while self.match(TokenType.OPERATOR) and self.current_token.value in ("+", "-"):
            op = self.current_token.value
            self.advance()
            right = self.parse_mul_expression()
            left = BinaryOp(op, left, right, left.line, left.column)
        
        return left
    
    def parse_mul_expression(self) -> ASTNode:
        """MulExpression ::= UnaryExpression { (*|/) UnaryExpression }"""
        left = self.parse_unary_expression()
        
        while self.match(TokenType.OPERATOR) and self.current_token.value in ("*", "/"):
            op = self.current_token.value
            self.advance()
            right = self.parse_unary_expression()
            left = BinaryOp(op, left, right, left.line, left.column)
        
        return left
    
    def parse_unary_expression(self) -> ASTNode:
        """UnaryExpression ::= [ - ] Primary"""
        if self.match(TokenType.OPERATOR, "-"):
            op = self.current_token.value
            line = self.current_token.line
            column = self.current_token.column
            self.advance()
            operand = self.parse_primary()
            return UnaryOp(op, operand, line, column)
        
        return self.parse_primary()
    
    def parse_primary(self) -> ASTNode:
        """Primary ::= Literal | Variable | FunctionCall | ( Expression )"""
        if not self.current_token:
            raise ParseError("Esperado expressão", Token(TokenType.EOF, "", 0, 0))
        
        line = self.current_token.line
        column = self.current_token.column
        
        # Integer literal
        if self.match(TokenType.INTEGER):
            value = int(self.current_token.value)
            self.advance()
            return IntegerLiteral(value, line, column)
        
        # Real literal
        if self.match(TokenType.REAL):
            value = float(self.current_token.value)
            self.advance()
            return RealLiteral(value, line, column)
        
        # String literal
        if self.match(TokenType.STRING):
            value = self.current_token.value[1:-1]  # Remove aspas
            self.advance()
            return StringLiteral(value, line, column)
        
        # Boolean literal
        if self.match(TokenType.BOOLEAN):
            value = self.current_token.value == "verdadeiro"
            self.advance()
            return BooleanLiteral(value, line, column)
        
        # Function call: leia_numero() ou leia_texto()
        if self.match(TokenType.KEYWORD, "leia_numero"):
            self.advance()
            self.expect(TokenType.SYMBOL, "(")
            self.expect(TokenType.SYMBOL, ")")
            return FunctionCall("leia_numero", [], line, column)
        
        if self.match(TokenType.KEYWORD, "leia_texto"):
            self.advance()
            self.expect(TokenType.SYMBOL, "(")
            self.expect(TokenType.SYMBOL, ")")
            return FunctionCall("leia_texto", [], line, column)
        
        # Variable
        if self.match(TokenType.IDENTIFIER):
            name = self.current_token.value
            self.advance()
            return Variable(name, line, column)
        
        # Parenthesized expression
        if self.match(TokenType.SYMBOL, "("):
            self.advance()
            expr = self.parse_expression()
            self.expect(TokenType.SYMBOL, ")")
            return expr
        
        raise ParseError(f"Expressão inválida: {self.current_token.value}", self.current_token)

