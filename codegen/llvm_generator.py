"""
Gerador de Código LLVM IR para a linguagem Apollo
Converte a AST em código LLVM IR
"""

from typing import Dict, List, Optional
from parser.ast import (
    ASTNode, Program, VarDeclaration, Assignment, IfStatement, WhileStatement,
    WriteStatement, ReadNumberStatement, ReadTextStatement,
    BinaryOp, UnaryOp, IntegerLiteral, RealLiteral, StringLiteral,
    BooleanLiteral, Variable, FunctionCall, Type
)


class LLVMGenerator:
    """Gerador de código LLVM IR"""
    
    def __init__(self):
        self.code: List[str] = []
        self.variable_counter = 0
        self.label_counter = 0
        self.string_counter = 0
        self.variables: Dict[str, str] = {}  # nome -> registro LLVM
        self.strings: Dict[str, str] = {}  # valor -> nome global
    
    def generate(self, program: Program) -> str:
        """Gera código LLVM IR para o programa"""
        self.code = []
        self.variable_counter = 0
        self.label_counter = 0
        self.string_counter = 0
        self.variables = {}
        self.strings = {}
        
        # Cabeçalho
        self.code.append("; Código LLVM IR gerado para Apollo")
        self.code.append("")
        
        # Declarações de funções padrão
        self.code.append("declare i32 @printf(i8*, ...)")
        self.code.append("declare i32 @scanf(i8*, ...)")
        self.code.append("")
        
        # Função main
        self.code.append("define i32 @main() {")
        self.code.append("entry:")
        
        # Gera código para declarações
        for decl in program.declarations:
            self.visit_var_declaration(decl)
        
        # Gera código para statements
        for stmt in program.statements:
            self.visit_statement(stmt)
        
        # Retorno
        self.code.append("  ret i32 0")
        self.code.append("}")
        self.code.append("")
        
        # Adiciona strings globais
        for value, name in self.strings.items():
            self.code.append(f"{name} = private unnamed_addr constant [{len(value) + 1} x i8] c\"{self.escape_string(value)}\\00\"")
        
        return "\n".join(self.code)
    
    def new_register(self) -> str:
        """Gera um novo registro temporário"""
        reg = f"%{self.variable_counter}"
        self.variable_counter += 1
        return reg
    
    def new_label(self) -> str:
        """Gera um novo label"""
        label = f"label{self.label_counter}"
        self.label_counter += 1
        return label
    
    def escape_string(self, s: str) -> str:
        """Escapa caracteres especiais em strings"""
        return s.replace("\\", "\\5C").replace("\n", "\\0A").replace('"', '\\22')
    
    def get_string_global(self, value: str) -> str:
        """Obtém ou cria uma string global"""
        if value not in self.strings:
            name = f"@.str{self.string_counter}"
            self.string_counter += 1
            self.strings[value] = name
        return self.strings[value]
    
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
    
    def visit_var_declaration(self, decl: VarDeclaration):
        """Visita uma declaração de variável"""
        reg = self.new_register()
        self.variables[decl.name] = reg
        
        # Inicializa com zero
        if decl.var_type == Type.INTEGER:
            self.code.append(f"  {reg} = alloca i32")
            self.code.append(f"  store i32 0, i32* {reg}")
        elif decl.var_type == Type.REAL:
            self.code.append(f"  {reg} = alloca double")
            self.code.append(f"  store double 0.0, double* {reg}")
        elif decl.var_type == Type.TEXT:
            self.code.append(f"  {reg} = alloca i8*")
            self.code.append(f"  store i8* null, i8** {reg}")
        elif decl.var_type == Type.BOOLEAN:
            self.code.append(f"  {reg} = alloca i1")
            self.code.append(f"  store i1 false, i1* {reg}")
        
        if decl.initial_value:
            value_reg = self.visit_expression(decl.initial_value)
            self.code.append(f"  store {self.get_llvm_type(decl.var_type)} {value_reg}, {self.get_llvm_type(decl.var_type)}* {reg}")
    
    def visit_assignment(self, assign: Assignment):
        """Visita uma atribuição"""
        if assign.variable not in self.variables:
            # Variável não declarada, cria automaticamente (para compatibilidade)
            reg = self.new_register()
            self.variables[assign.variable] = reg
            self.code.append(f"  {reg} = alloca i32")
        
        var_reg = self.variables[assign.variable]
        
        # Trata leia_numero() e leia_texto() como chamadas especiais
        if isinstance(assign.value, FunctionCall):
            if assign.value.name == "leia_numero":
                format_str = self.get_string_global("%d")
                format_reg = self.new_register()
                self.code.append(f"  {format_reg} = getelementptr inbounds [2 x i8], [2 x i8]* {format_str}, i32 0, i32 0")
                self.code.append(f"  call i32 (i8*, ...) @scanf(i8* {format_reg}, i32* {var_reg})")
                return
            elif assign.value.name == "leia_texto":
                format_str = self.get_string_global("%s")
                format_reg = self.new_register()
                self.code.append(f"  {format_reg} = getelementptr inbounds [2 x i8], [2 x i8]* {format_str}, i32 0, i32 0")
                self.code.append(f"  call i32 (i8*, ...) @scanf(i8* {format_reg}, i8** {var_reg})")
                return
        
        value_reg = self.visit_expression(assign.value)
        
        # Assume i32 por padrão (pode ser melhorado com análise de tipo)
        self.code.append(f"  store i32 {value_reg}, i32* {var_reg}")
    
    def visit_if_statement(self, stmt: IfStatement):
        """Visita um comando if"""
        cond_reg = self.visit_expression(stmt.condition)
        then_label = self.new_label()
        else_label = self.new_label()
        end_label = self.new_label()
        
        # Branch
        self.code.append(f"  br i1 {cond_reg}, label %{then_label}, label %{else_label if stmt.else_block else end_label}")
        
        # Then block
        self.code.append(f"{then_label}:")
        self.visit_statement(stmt.then_block)
        self.code.append(f"  br label %{end_label}")
        
        # Else block
        if stmt.else_block:
            self.code.append(f"{else_label}:")
            self.visit_statement(stmt.else_block)
            self.code.append(f"  br label %{end_label}")
        
        # End
        self.code.append(f"{end_label}:")
    
    def visit_while_statement(self, stmt: WhileStatement):
        """Visita um comando while"""
        cond_label = self.new_label()
        body_label = self.new_label()
        end_label = self.new_label()
        
        # Condição inicial
        self.code.append(f"  br label %{cond_label}")
        self.code.append(f"{cond_label}:")
        
        # Avalia condição
        cond_reg = self.visit_expression(stmt.condition)
        self.code.append(f"  br i1 {cond_reg}, label %{body_label}, label %{end_label}")
        
        # Corpo
        self.code.append(f"{body_label}:")
        self.visit_statement(stmt.body)
        self.code.append(f"  br label %{cond_label}")
        
        # Fim
        self.code.append(f"{end_label}:")
    
    def visit_write_statement(self, stmt: WriteStatement):
        """Visita um comando escreva"""
        for expr in stmt.expressions:
            expr_type = self.get_expression_type(expr)
            value_reg = self.visit_expression(expr)
            
            if expr_type == Type.INTEGER:
                format_str = self.get_string_global("%d\\0A")
                format_reg = self.new_register()
                self.code.append(f"  {format_reg} = getelementptr inbounds [3 x i8], [3 x i8]* {format_str}, i32 0, i32 0")
                self.code.append(f"  call i32 (i8*, ...) @printf(i8* {format_reg}, i32 {value_reg})")
            elif expr_type == Type.REAL:
                format_str = self.get_string_global("%f\\0A")
                format_reg = self.new_register()
                self.code.append(f"  {format_reg} = getelementptr inbounds [3 x i8], [3 x i8]* {format_str}, i32 0, i32 0")
                self.code.append(f"  call i32 (i8*, ...) @printf(i8* {format_reg}, double {value_reg})")
            elif expr_type == Type.TEXT:
                format_str = self.get_string_global("%s\\0A")
                format_reg = self.new_register()
                self.code.append(f"  {format_reg} = getelementptr inbounds [3 x i8], [3 x i8]* {format_str}, i32 0, i32 0")
                self.code.append(f"  call i32 (i8*, ...) @printf(i8* {format_reg}, i8* {value_reg})")
            elif expr_type == Type.BOOLEAN:
                format_str = self.get_string_global("%s\\0A")
                format_reg = self.new_register()
                true_str = self.get_string_global("verdadeiro")
                false_str = self.get_string_global("falso")
                str_reg = self.new_register()
                self.code.append(f"  {str_reg} = select i1 {value_reg}, i8* {true_str}, i8* {false_str}")
                self.code.append(f"  {format_reg} = getelementptr inbounds [3 x i8], [3 x i8]* {format_str}, i32 0, i32 0")
                self.code.append(f"  call i32 (i8*, ...) @printf(i8* {format_reg}, i8* {str_reg})")
    
    def visit_read_number_statement(self, stmt: ReadNumberStatement):
        """Visita um comando leia_numero"""
        if stmt.variable not in self.variables:
            reg = self.new_register()
            self.variables[stmt.variable] = reg
            self.code.append(f"  {reg} = alloca i32")
        
        var_reg = self.variables[stmt.variable]
        format_str = self.get_string_global("%d")
        format_reg = self.new_register()
        self.code.append(f"  {format_reg} = getelementptr inbounds [2 x i8], [2 x i8]* {format_str}, i32 0, i32 0")
        self.code.append(f"  call i32 (i8*, ...) @scanf(i8* {format_reg}, i32* {var_reg})")
    
    def visit_read_text_statement(self, stmt: ReadTextStatement):
        """Visita um comando leia_texto"""
        if stmt.variable not in self.variables:
            reg = self.new_register()
            self.variables[stmt.variable] = reg
            self.code.append(f"  {reg} = alloca i8*")
        
        var_reg = self.variables[stmt.variable]
        format_str = self.get_string_global("%s")
        format_reg = self.new_register()
        self.code.append(f"  {format_reg} = getelementptr inbounds [2 x i8], [2 x i8]* {format_str}, i32 0, i32 0")
        self.code.append(f"  call i32 (i8*, ...) @scanf(i8* {format_reg}, i8** {var_reg})")
    
    def visit_expression(self, expr: ASTNode) -> str:
        """Visita uma expressão e retorna o registro LLVM"""
        if isinstance(expr, IntegerLiteral):
            return str(expr.value)
        elif isinstance(expr, RealLiteral):
            return str(expr.value)
        elif isinstance(expr, StringLiteral):
            str_global = self.get_string_global(expr.value)
            reg = self.new_register()
            self.code.append(f"  {reg} = getelementptr inbounds [{len(expr.value) + 1} x i8], [{len(expr.value) + 1} x i8]* {str_global}, i32 0, i32 0")
            return reg
        elif isinstance(expr, BooleanLiteral):
            return "1" if expr.value else "0"
        elif isinstance(expr, FunctionCall):
            return self.visit_function_call(expr)
        elif isinstance(expr, Variable):
            if expr.name not in self.variables:
                # Variável não declarada, cria automaticamente
                reg = self.new_register()
                self.variables[expr.name] = reg
                self.code.append(f"  {reg} = alloca i32")
                self.code.append(f"  store i32 0, i32* {reg}")
            
            var_reg = self.variables[expr.name]
            load_reg = self.new_register()
            self.code.append(f"  {load_reg} = load i32, i32* {var_reg}")
            return load_reg
        elif isinstance(expr, BinaryOp):
            return self.visit_binary_op(expr)
        elif isinstance(expr, UnaryOp):
            return self.visit_unary_op(expr)
        else:
            return "0"
    
    def visit_function_call(self, call: FunctionCall) -> str:
        """Visita uma chamada de função"""
        if call.name == "leia_numero":
            # Retorna um registro temporário (será usado em atribuições)
            # Em atribuições, isso será tratado especialmente
            return "0"  # Placeholder, será substituído na atribuição
        elif call.name == "leia_texto":
            return ""  # Placeholder
        else:
            return "0"
    
    def visit_binary_op(self, op: BinaryOp) -> str:
        """Visita uma operação binária"""
        left_reg = self.visit_expression(op.left)
        right_reg = self.visit_expression(op.right)
        result_reg = self.new_register()
        
        if op.operator == "+":
            self.code.append(f"  {result_reg} = add i32 {left_reg}, {right_reg}")
        elif op.operator == "-":
            self.code.append(f"  {result_reg} = sub i32 {left_reg}, {right_reg}")
        elif op.operator == "*":
            self.code.append(f"  {result_reg} = mul i32 {left_reg}, {right_reg}")
        elif op.operator == "/":
            self.code.append(f"  {result_reg} = sdiv i32 {left_reg}, {right_reg}")
        elif op.operator == "==":
            cmp_reg = self.new_register()
            self.code.append(f"  {cmp_reg} = icmp eq i32 {left_reg}, {right_reg}")
            self.code.append(f"  {result_reg} = zext i1 {cmp_reg} to i32")
        elif op.operator == "!=":
            cmp_reg = self.new_register()
            self.code.append(f"  {cmp_reg} = icmp ne i32 {left_reg}, {right_reg}")
            self.code.append(f"  {result_reg} = zext i1 {cmp_reg} to i32")
        elif op.operator == "<":
            cmp_reg = self.new_register()
            self.code.append(f"  {cmp_reg} = icmp slt i32 {left_reg}, {right_reg}")
            self.code.append(f"  {result_reg} = zext i1 {cmp_reg} to i32")
        elif op.operator == ">":
            cmp_reg = self.new_register()
            self.code.append(f"  {cmp_reg} = icmp sgt i32 {left_reg}, {right_reg}")
            self.code.append(f"  {result_reg} = zext i1 {cmp_reg} to i32")
        elif op.operator == "<=":
            cmp_reg = self.new_register()
            self.code.append(f"  {cmp_reg} = icmp sle i32 {left_reg}, {right_reg}")
            self.code.append(f"  {result_reg} = zext i1 {cmp_reg} to i32")
        elif op.operator == ">=":
            cmp_reg = self.new_register()
            self.code.append(f"  {cmp_reg} = icmp sge i32 {left_reg}, {right_reg}")
            self.code.append(f"  {result_reg} = zext i1 {cmp_reg} to i32")
        else:
            result_reg = left_reg
        
        return result_reg
    
    def visit_unary_op(self, op: UnaryOp) -> str:
        """Visita uma operação unária"""
        operand_reg = self.visit_expression(op.operand)
        result_reg = self.new_register()
        
        if op.operator == "-":
            self.code.append(f"  {result_reg} = sub i32 0, {operand_reg}")
        else:
            result_reg = operand_reg
        
        return result_reg
    
    def get_expression_type(self, expr: ASTNode) -> Type:
        """Retorna o tipo de uma expressão"""
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
            # Assume INTEGER por padrão (deveria usar tabela de símbolos)
            return Type.INTEGER
        elif isinstance(expr, BinaryOp):
            if expr.operator in ("==", "!=", "<", ">", "<=", ">="):
                return Type.BOOLEAN
            return Type.INTEGER
        else:
            return Type.INTEGER
    
    def get_llvm_type(self, var_type: Type) -> str:
        """Converte tipo Apollo para tipo LLVM"""
        type_map = {
            Type.INTEGER: "i32",
            Type.REAL: "double",
            Type.TEXT: "i8*",
            Type.BOOLEAN: "i1"
        }
        return type_map.get(var_type, "i32")

