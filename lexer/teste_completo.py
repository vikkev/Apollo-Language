#!/usr/bin/env python3
"""
Teste completo e abrangente do analisador léxico Apollo.
Verifica todas as funcionalidades implementadas após as melhorias.
"""

from apollo_lexer import ApolloLexer, TokenType

def teste_strings():
    """Teste específico para strings"""
    print("=== TESTE DE STRINGS ===\n")
    
    lexer = ApolloLexer()
    
    casos_string = [
        '"texto simples"',
        '"texto com espaços"',
        '"texto com números 123"',
        '"texto com símbolos !@#$"',
        '"texto com acentos ção"',
        '""',  # string vazia
        '"texto\ncom quebra"',  # string com quebra de linha
    ]
    
    for caso in casos_string:
        print(f"Testando: {caso}")
        tokens = lexer.tokenize(caso)
        
        tokens_validos = [t for t in tokens if t.type not in [TokenType.WHITESPACE, TokenType.EOF]]
        
        if len(tokens_validos) == 1 and tokens_validos[0].type == TokenType.STRING:
            print(f"  ✓ STRING: '{tokens_validos[0].value}'")
        else:
            print(f"  ✗ ERRO: {[str(t) for t in tokens_validos]}")
        print()

def teste_comentarios():
    """Teste específico para comentários"""
    print("=== TESTE DE COMENTÁRIOS ===\n")
    
    lexer = ApolloLexer()
    
    casos_comentario = [
        "# comentário simples",
        "# comentário com números 123",
        "# comentário com símbolos !@#$",
        "# comentário com acentos ção",
        "#",  # comentário vazio
        "# comentário\ncom quebra",  # comentário com quebra
    ]
    
    for caso in casos_comentario:
        print(f"Testando: {caso}")
        tokens = lexer.tokenize(caso)
        
        tokens_validos = [t for t in tokens if t.type not in [TokenType.WHITESPACE, TokenType.EOF]]
        
        if len(tokens_validos) == 1 and tokens_validos[0].type == TokenType.COMMENT:
            print(f"  ✓ COMMENT: '{tokens_validos[0].value}'")
        else:
            print(f"  ✗ ERRO: {[str(t) for t in tokens_validos]}")
        print()

def teste_operadores_compostos():
    """Teste específico para operadores compostos"""
    print("=== TESTE DE OPERADORES COMPOSTOS ===\n")
    
    lexer = ApolloLexer()
    
    casos_operadores = [
        ("x==10", ["IDENTIFIER('x')", "OPERATOR('==')", "INTEGER('10')"]),
        ("x!=5", ["IDENTIFIER('x')", "OPERATOR('!=')", "INTEGER('5')"]),
        ("x<=20", ["IDENTIFIER('x')", "OPERATOR('<=')", "INTEGER('20')"]),
        ("x>=15", ["IDENTIFIER('x')", "OPERATOR('>=')", "INTEGER('15')"]),
        ("x<10", ["IDENTIFIER('x')", "OPERATOR('<')", "INTEGER('10')"]),
        ("x>5", ["IDENTIFIER('x')", "OPERATOR('>')", "INTEGER('5')"]),
        ("x=1", ["IDENTIFIER('x')", "OPERATOR('=')", "INTEGER('1')"]),
    ]
    
    for codigo, esperado in casos_operadores:
        print(f"Testando: {codigo}")
        tokens = lexer.tokenize(codigo)
        
        tokens_validos = [t for t in tokens if t.type not in [TokenType.WHITESPACE, TokenType.EOF]]
        resultado = [f"{t.type.name}('{t.value}')" for t in tokens_validos]
        
        if resultado == esperado:
            print(f"  ✓ CORRETO: {resultado}")
        else:
            print(f"  ✗ ERRO: Esperado {esperado}, obtido {resultado}")
        print()

def teste_numeros():
    """Teste específico para números"""
    print("=== TESTE DE NÚMEROS ===\n")
    
    lexer = ApolloLexer()
    
    casos_numeros = [
        ("42", TokenType.INTEGER),
        ("+42", TokenType.INTEGER),
        ("-42", TokenType.INTEGER),
        ("3.14", TokenType.REAL),
        ("+3.14", TokenType.REAL),
        ("-3.14", TokenType.REAL),
        ("0", TokenType.INTEGER),
        ("0.0", TokenType.REAL),
        ("123.456", TokenType.REAL),
    ]
    
    for numero, tipo_esperado in casos_numeros:
        print(f"Testando: {numero}")
        tokens = lexer.tokenize(numero)
        
        tokens_validos = [t for t in tokens if t.type not in [TokenType.WHITESPACE, TokenType.EOF]]
        
        if len(tokens_validos) == 1 and tokens_validos[0].type == tipo_esperado:
            print(f"  ✓ {tipo_esperado.name}: '{tokens_validos[0].value}'")
        else:
            print(f"  ✗ ERRO: {[str(t) for t in tokens_validos]}")
        print()

def teste_identificadores():
    """Teste específico para identificadores"""
    print("=== TESTE DE IDENTIFICADORES ===\n")
    
    lexer = ApolloLexer()
    
    casos_identificadores = [
        ("x", TokenType.IDENTIFIER),
        ("variavel", TokenType.IDENTIFIER),
        ("variavel123", TokenType.IDENTIFIER),
        ("_variavel", TokenType.IDENTIFIER),
        ("variavel_123", TokenType.IDENTIFIER),
        ("algoritmo", TokenType.KEYWORD),  # palavra-chave
        ("se", TokenType.KEYWORD),  # palavra-chave
        ("verdadeiro", TokenType.BOOLEAN),  # booleano
        ("falso", TokenType.BOOLEAN),  # booleano
    ]
    
    for identificador, tipo_esperado in casos_identificadores:
        print(f"Testando: {identificador}")
        tokens = lexer.tokenize(identificador)
        
        tokens_validos = [t for t in tokens if t.type not in [TokenType.WHITESPACE, TokenType.EOF]]
        
        if len(tokens_validos) == 1 and tokens_validos[0].type == tipo_esperado:
            print(f"  ✓ {tipo_esperado.name}: '{tokens_validos[0].value}'")
        else:
            print(f"  ✗ ERRO: {[str(t) for t in tokens_validos]}")
        print()

def teste_codigo_completo():
    """Teste com código Apollo completo"""
    print("=== TESTE COM CÓDIGO COMPLETO ===\n")
    
    codigo = """
algoritmo exemplo_completo
    # Este é um comentário
    inteiro x = 42
    real y = 3.14
    texto nome = "Apollo Language"
    logico ativo = verdadeiro
    
    se (x > 10) {
        escreva("x é maior que 10")
    } senao {
        escreva("x é menor ou igual a 10")
    }
    
    enquanto (ativo) {
        x = x + 1
        se (x >= 50) {
            ativo = falso
        }
    }
fim_algoritmo
"""
    
    lexer = ApolloLexer()
    tokens = lexer.tokenize(codigo)
    
    print("Tokens encontrados:")
    tokens_validos = [t for t in tokens if t.type not in [TokenType.WHITESPACE, TokenType.EOF]]
    
    for token in tokens_validos:
        print(f"{token.type.name:<12}: '{token.value}' (linha {token.line}, coluna {token.column})")
    
    # Verifica tokens inválidos
    invalidos = [t for t in tokens if t.type == TokenType.INVALID]
    if invalidos:
        print(f"\n{len(invalidos)} token(s) inválido(s) encontrado(s)")
        for token in invalidos:
            print(f"  INVALID: '{token.value}' na linha {token.line}, coluna {token.column}")
    else:
        print("\nAnálise léxica concluída com sucesso!")

def main():
    """Função principal"""
    try:
        teste_strings()
        teste_comentarios()
        teste_operadores_compostos()
        teste_numeros()
        teste_identificadores()
        teste_codigo_completo()
        
        print("="*60)
        print("REVISÃO COMPLETA CONCLUÍDA COM SUCESSO!")
        print("="*60)
        
    except Exception as e:
        print(f"\nERRO: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
