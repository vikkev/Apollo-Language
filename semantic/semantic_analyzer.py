"""
Analisador Semântico para a linguagem Apollo
Verifica tipos, escopos e outras regras semânticas
"""

from typing import Dict, List, Optional, Set
from parser.ast import (
    ASTNode, Program, VarDeclaration, Assignment, IfStatement, WhileStatement,
    WriteStatement, ReadNumberStatement, ReadTextStatement,
    BinaryOp, UnaryOp, IntegerLiteral, RealLiteral, StringLiteral,
    BooleanLiteral, Variable, FunctionCall, Type
)


class Symbol:
    """Representa um símbolo na tabela de símbolos"""
    
    def __init__(self, name: str, var_type: Type, line: int = 0, column: int = 0):
        self.name = name
        self.var_type = var_type
        self.line = line
        self.column = column
        self.initialized = False
    
    def __repr__(self):
        return f"Symbol({self.name}: {self.var_type.value})"


class SemanticError(Exception):
    """Exceção para erros semânticos"""
    
    def __init__(self, message: str, line: int = 0, column: int = 0):
        self.message = message
        self.line = line
        self.column = column
        super().__init__(f"Erro semântico na linha {line}, coluna {column}: {message}")


class Scope:
    """Representa um escopo (nível de aninhamento)"""
    
    def __init__(self, parent: Optional['Scope'] = None):
        self.parent = parent
        self.symbols: Dict[str, Symbol] = {}
    
    def declare(self, name: str, var_type: Type, line: int = 0, column: int = 0) -> Symbol:
        """Declara uma variável no escopo atual"""
        if name in self.symbols:
            raise SemanticError(f"Variável '{name}' já foi declarada neste escopo", line, column)
        
        symbol = Symbol(name, var_type, line, column)
        self.symbols[name] = symbol
        return symbol
    
    def lookup(self, name: str) -> Optional[Symbol]:
        """Busca uma variável no escopo atual e nos escopos pais"""
        if name in self.symbols:
            return self.symbols[name]
        if self.parent:
            return self.parent.lookup(name)
        return None
    
    def is_declared(self, name: str) -> bool:
        """Verifica se uma variável está declarada"""
        return self.lookup(name) is not None


class SemanticAnalyzer:
    """Analisador semântico para Apollo"""
    
    def __init__(self):
        self.current_scope: Optional[Scope] = None
        self.errors: List[SemanticError] = []
    
    def analyze(self, program: Program) -> List[SemanticError]:
        """Realiza a análise semântica do programa"""
        self.errors = []
        self.current_scope = Scope()
        
        # Analisa declarações
        for decl in program.declarations:
            self.visit_var_declaration(decl)
        
        # Analisa comandos
        for stmt in program.statements:
            self.visit_statement(stmt)
        
        return self.errors
    
    def visit_statement(self, stmt: ASTNode):
        """Visita um statement"""
        if isinstance(stmt, Assignment):
            self.visit_assignment(stmt)
        elif isinstance(stmt, IfStatement):
            self.visit_if_statement(stmt)
        elif isinstance(stmt, WhileStatement):
            self.visit_while_statement(stmt)
        elif isinstance(stmt, WriteStatement):
            self.visit_write_statement(stmt)
        elif isinstance(stmt, ReadNumberStatement):
            self.visit_read_number_statement(stmt)
        elif isinstance(stmt, ReadTextStatement):
            self.visit_read_text_statement(stmt)
        elif hasattr(stmt, 'statements'):  # Block
            self.visit_block(stmt)
    
    def visit_var_declaration(self, decl: VarDeclaration):
        """Visita uma declaração de variável"""
        try:
            symbol = self.current_scope.declare(decl.name, decl.var_type, decl.line, decl.column)
            if decl.initial_value:
                expr_type = self.visit_expression(decl.initial_value)
                self.check_type_compatibility(decl.var_type, expr_type, decl.line, decl.column)
                symbol.initialized = True
        except SemanticError as e:
            self.errors.append(e)
    
    def visit_assignment(self, assign: Assignment):
        """Visita uma atribuição"""
        # Verifica se a variável existe
        symbol = self.current_scope.lookup(assign.variable)
        if not symbol:
            self.errors.append(SemanticError(
                f"Variável '{assign.variable}' não foi declarada",
                assign.line, assign.column
            ))
            return
        
        # Verifica o tipo da expressão
        expr_type = self.visit_expression(assign.value)
        self.check_type_compatibility(symbol.var_type, expr_type, assign.line, assign.column)
        symbol.initialized = True
    
    def visit_if_statement(self, stmt: IfStatement):
        """Visita um comando if"""
        # Condição deve ser booleana
        cond_type = self.visit_expression(stmt.condition)
        if cond_type != Type.BOOLEAN:
            self.errors.append(SemanticError(
                f"Condição do 'se' deve ser do tipo logico, encontrado {cond_type.value}",
                stmt.condition.line, stmt.condition.column
            ))
        
        # Analisa blocos
        self.visit_statement(stmt.then_block)
        if stmt.else_block:
            self.visit_statement(stmt.else_block)
    
    def visit_while_statement(self, stmt: WhileStatement):
        """Visita um comando while"""
        # Condição deve ser booleana
        cond_type = self.visit_expression(stmt.condition)
        if cond_type != Type.BOOLEAN:
            self.errors.append(SemanticError(
                f"Condição do 'enquanto' deve ser do tipo logico, encontrado {cond_type.value}",
                stmt.condition.line, stmt.condition.column
            ))
        
        # Analisa corpo
        self.visit_statement(stmt.body)
    
    def visit_write_statement(self, stmt: WriteStatement):
        """Visita um comando escreva"""
        for expr in stmt.expressions:
            self.visit_expression(expr)  # Qualquer tipo pode ser escrito
    
    def visit_read_number_statement(self, stmt: ReadNumberStatement):
        """Visita um comando leia_numero"""
        symbol = self.current_scope.lookup(stmt.variable)
        if not symbol:
            self.errors.append(SemanticError(
                f"Variável '{stmt.variable}' não foi declarada",
                stmt.line, stmt.column
            ))
        elif symbol.var_type not in (Type.INTEGER, Type.REAL):
            self.errors.append(SemanticError(
                f"Variável '{stmt.variable}' deve ser do tipo inteiro ou real para leia_numero",
                stmt.line, stmt.column
            ))
    
    def visit_read_text_statement(self, stmt: ReadTextStatement):
        """Visita um comando leia_texto"""
        symbol = self.current_scope.lookup(stmt.variable)
        if not symbol:
            self.errors.append(SemanticError(
                f"Variável '{stmt.variable}' não foi declarada",
                stmt.line, stmt.column
            ))
        elif symbol.var_type != Type.TEXT:
            self.errors.append(SemanticError(
                f"Variável '{stmt.variable}' deve ser do tipo texto para leia_texto",
                stmt.line, stmt.column
            ))
    
    def visit_block(self, block):
        """Visita um bloco (cria novo escopo)"""
        old_scope = self.current_scope
        self.current_scope = Scope(old_scope)
        
        for stmt in block.statements:
            self.visit_statement(stmt)
        
        self.current_scope = old_scope
    
    def visit_expression(self, expr: ASTNode) -> Type:
        """Visita uma expressão e retorna seu tipo"""
        if isinstance(expr, IntegerLiteral):
            return Type.INTEGER
        elif isinstance(expr, RealLiteral):
            return Type.REAL
        elif isinstance(expr, StringLiteral):
            return Type.TEXT
        elif isinstance(expr, BooleanLiteral):
            return Type.BOOLEAN
        elif isinstance(expr, FunctionCall):
            if expr.name == "leia_numero":
                return Type.INTEGER
            elif expr.name == "leia_texto":
                return Type.TEXT
            return Type.INTEGER
        elif isinstance(expr, Variable):
            symbol = self.current_scope.lookup(expr.name)
            if not symbol:
                self.errors.append(SemanticError(
                    f"Variável '{expr.name}' não foi declarada",
                    expr.line, expr.column
                ))
                return Type.INTEGER  # Tipo padrão para continuar análise
            return symbol.var_type
        elif isinstance(expr, BinaryOp):
            return self.visit_binary_op(expr)
        elif isinstance(expr, UnaryOp):
            return self.visit_unary_op(expr)
        else:
            return Type.INTEGER  # Tipo padrão
    
    def visit_binary_op(self, op: BinaryOp) -> Type:
        """Visita uma operação binária"""
        left_type = self.visit_expression(op.left)
        right_type = self.visit_expression(op.right)
        
        # Operadores aritméticos
        if op.operator in ("+", "-", "*", "/"):
            if left_type in (Type.INTEGER, Type.REAL) and right_type in (Type.INTEGER, Type.REAL):
                # Promoção: se um for real, resultado é real
                if left_type == Type.REAL or right_type == Type.REAL:
                    return Type.REAL
                return Type.INTEGER
            else:
                self.errors.append(SemanticError(
                    f"Operador '{op.operator}' requer operandos numéricos",
                    op.line, op.column
                ))
                return Type.INTEGER
        
        # Operadores relacionais
        elif op.operator in ("<", ">", "<=", ">="):
            if left_type in (Type.INTEGER, Type.REAL) and right_type in (Type.INTEGER, Type.REAL):
                return Type.BOOLEAN
            else:
                self.errors.append(SemanticError(
                    f"Operador '{op.operator}' requer operandos numéricos",
                    op.line, op.column
                ))
                return Type.BOOLEAN
        
        # Operadores de igualdade
        elif op.operator in ("==", "!="):
            if left_type == right_type:
                return Type.BOOLEAN
            else:
                self.errors.append(SemanticError(
                    f"Operador '{op.operator}' requer operandos do mesmo tipo",
                    op.line, op.column
                ))
                return Type.BOOLEAN
        
        # Operadores lógicos
        elif op.operator in ("&&", "||"):
            if left_type == Type.BOOLEAN and right_type == Type.BOOLEAN:
                return Type.BOOLEAN
            else:
                self.errors.append(SemanticError(
                    f"Operador '{op.operator}' requer operandos do tipo logico",
                    op.line, op.column
                ))
                return Type.BOOLEAN
        
        return Type.INTEGER
    
    def visit_unary_op(self, op: UnaryOp) -> Type:
        """Visita uma operação unária"""
        operand_type = self.visit_expression(op.operand)
        
        if op.operator == "-":
            if operand_type in (Type.INTEGER, Type.REAL):
                return operand_type
            else:
                self.errors.append(SemanticError(
                    "Operador unário '-' requer operando numérico",
                    op.line, op.column
                ))
                return Type.INTEGER
        
        return operand_type
    
    def check_type_compatibility(self, expected: Type, actual: Type, line: int, column: int):
        """Verifica compatibilidade de tipos"""
        if expected == actual:
            return
        
        # Promoção: inteiro pode ser atribuído a real
        if expected == Type.REAL and actual == Type.INTEGER:
            return
        
        # Incompatível
        self.errors.append(SemanticError(
            f"Tipo incompatível: esperado {expected.value}, encontrado {actual.value}",
            line, column
        ))

