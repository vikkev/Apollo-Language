"""
Abstract Syntax Tree (AST) para a linguagem Apollo
Define os nós da árvore sintática abstrata
"""

from abc import ABC, abstractmethod
from typing import List, Optional, Any
from enum import Enum


class Type(Enum):
    """Tipos de dados da linguagem Apollo"""
    INTEGER = "inteiro"
    REAL = "real"
    TEXT = "texto"
    BOOLEAN = "logico"
    VOID = "void"


class ASTNode(ABC):
    """Classe base para todos os nós da AST"""
    
    def __init__(self, line: int = 0, column: int = 0):
        self.line = line
        self.column = column
    
    @abstractmethod
    def accept(self, visitor):
        """Aceita um visitor para percorrer a árvore"""
        pass


# ========== Program ==========

class Program(ASTNode):
    """Nó raiz do programa"""
    
    def __init__(self, declarations: List[ASTNode], statements: List[ASTNode], line: int = 0, column: int = 0):
        super().__init__(line, column)
        self.declarations = declarations
        self.statements = statements
    
    def accept(self, visitor):
        return visitor.visit_program(self)
    
    def __repr__(self):
        return f"Program(declarations={len(self.declarations)}, statements={len(self.statements)})"


# ========== Declarations ==========

class VarDeclaration(ASTNode):
    """Declaração de variável"""
    
    def __init__(self, var_type: Type, name: str, initial_value: Optional[ASTNode] = None, line: int = 0, column: int = 0):
        super().__init__(line, column)
        self.var_type = var_type
        self.name = name
        self.initial_value = initial_value
    
    def accept(self, visitor):
        return visitor.visit_var_declaration(self)
    
    def __repr__(self):
        return f"VarDeclaration({self.var_type.value} {self.name})"


# ========== Statements ==========

class Block(ASTNode):
    """Bloco de comandos"""
    
    def __init__(self, statements: List[ASTNode], line: int = 0, column: int = 0):
        super().__init__(line, column)
        self.statements = statements
    
    def accept(self, visitor):
        return visitor.visit_block(self)
    
    def __repr__(self):
        return f"Block({len(self.statements)} statements)"


class Assignment(ASTNode):
    """Atribuição de valor"""
    
    def __init__(self, variable: str, value: ASTNode, line: int = 0, column: int = 0):
        super().__init__(line, column)
        self.variable = variable
        self.value = value
    
    def accept(self, visitor):
        return visitor.visit_assignment(self)
    
    def __repr__(self):
        return f"Assignment({self.variable} = {self.value})"


class IfStatement(ASTNode):
    """Comando condicional"""
    
    def __init__(self, condition: ASTNode, then_block: ASTNode, else_block: Optional[ASTNode] = None, line: int = 0, column: int = 0):
        super().__init__(line, column)
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block
    
    def accept(self, visitor):
        return visitor.visit_if_statement(self)
    
    def __repr__(self):
        return f"IfStatement(condition={self.condition})"


class WhileStatement(ASTNode):
    """Comando de repetição enquanto"""
    
    def __init__(self, condition: ASTNode, body: ASTNode, line: int = 0, column: int = 0):
        super().__init__(line, column)
        self.condition = condition
        self.body = body
    
    def accept(self, visitor):
        return visitor.visit_while_statement(self)
    
    def __repr__(self):
        return f"WhileStatement(condition={self.condition})"


class WriteStatement(ASTNode):
    """Comando de escrita (escreva)"""
    
    def __init__(self, expressions: List[ASTNode], line: int = 0, column: int = 0):
        super().__init__(line, column)
        self.expressions = expressions
    
    def accept(self, visitor):
        return visitor.visit_write_statement(self)
    
    def __repr__(self):
        return f"WriteStatement({len(self.expressions)} expressions)"


class ReadNumberStatement(ASTNode):
    """Comando de leitura de número (leia_numero)"""
    
    def __init__(self, variable: str, line: int = 0, column: int = 0):
        super().__init__(line, column)
        self.variable = variable
    
    def accept(self, visitor):
        return visitor.visit_read_number_statement(self)
    
    def __repr__(self):
        return f"ReadNumberStatement({self.variable})"


class ReadTextStatement(ASTNode):
    """Comando de leitura de texto (leia_texto)"""
    
    def __init__(self, variable: str, line: int = 0, column: int = 0):
        super().__init__(line, column)
        self.variable = variable
    
    def accept(self, visitor):
        return visitor.visit_read_text_statement(self)
    
    def __repr__(self):
        return f"ReadTextStatement({self.variable})"


# ========== Expressions ==========

class BinaryOp(ASTNode):
    """Operação binária"""
    
    def __init__(self, operator: str, left: ASTNode, right: ASTNode, line: int = 0, column: int = 0):
        super().__init__(line, column)
        self.operator = operator
        self.left = left
        self.right = right
    
    def accept(self, visitor):
        return visitor.visit_binary_op(self)
    
    def __repr__(self):
        return f"BinaryOp({self.operator}, {self.left}, {self.right})"


class UnaryOp(ASTNode):
    """Operação unária"""
    
    def __init__(self, operator: str, operand: ASTNode, line: int = 0, column: int = 0):
        super().__init__(line, column)
        self.operator = operator
        self.operand = operand
    
    def accept(self, visitor):
        return visitor.visit_unary_op(self)
    
    def __repr__(self):
        return f"UnaryOp({self.operator}, {self.operand})"


class IntegerLiteral(ASTNode):
    """Literal inteiro"""
    
    def __init__(self, value: int, line: int = 0, column: int = 0):
        super().__init__(line, column)
        self.value = value
    
    def accept(self, visitor):
        return visitor.visit_integer_literal(self)
    
    def __repr__(self):
        return f"IntegerLiteral({self.value})"


class RealLiteral(ASTNode):
    """Literal real"""
    
    def __init__(self, value: float, line: int = 0, column: int = 0):
        super().__init__(line, column)
        self.value = value
    
    def accept(self, visitor):
        return visitor.visit_real_literal(self)
    
    def __repr__(self):
        return f"RealLiteral({self.value})"


class StringLiteral(ASTNode):
    """Literal string"""
    
    def __init__(self, value: str, line: int = 0, column: int = 0):
        super().__init__(line, column)
        self.value = value
    
    def accept(self, visitor):
        return visitor.visit_string_literal(self)
    
    def __repr__(self):
        return f"StringLiteral('{self.value}')"


class BooleanLiteral(ASTNode):
    """Literal booleano"""
    
    def __init__(self, value: bool, line: int = 0, column: int = 0):
        super().__init__(line, column)
        self.value = value
    
    def accept(self, visitor):
        return visitor.visit_boolean_literal(self)
    
    def __repr__(self):
        return f"BooleanLiteral({self.value})"


class Variable(ASTNode):
    """Referência a variável"""
    
    def __init__(self, name: str, line: int = 0, column: int = 0):
        super().__init__(line, column)
        self.name = name
    
    def accept(self, visitor):
        return visitor.visit_variable(self)
    
    def __repr__(self):
        return f"Variable({self.name})"


class FunctionCall(ASTNode):
    """Chamada de função"""
    
    def __init__(self, name: str, arguments: List[ASTNode] = None, line: int = 0, column: int = 0):
        super().__init__(line, column)
        self.name = name
        self.arguments = arguments or []
    
    def accept(self, visitor):
        return visitor.visit_function_call(self)
    
    def __repr__(self):
        return f"FunctionCall({self.name}, {len(self.arguments)} args)"
