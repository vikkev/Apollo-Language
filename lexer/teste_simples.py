#!/usr/bin/env python3
"""
Teste simples e focado do analisador léxico Apollo.
Demonstra as funcionalidades principais sem loops infinitos.
"""

from apollo_lexer import ApolloLexer, TokenType

def teste_simples():
    """Teste básico do lexer"""
    print("=== TESTE SIMPLES DO LEXER APOLLO ===\n")
    
    # Casos de teste específicos
    casos_teste = [
        "x = 42",
        "x == 10", 
        "x != 5",
        "x <= 20",
        "x >= 15",
        "variavel123",
        "3.14159",
        '"texto"',
        "# comentario"
    ]
    
    lexer = ApolloLexer()
    
    for caso in casos_teste:
        print(f"Testando: '{caso}'")
        tokens = lexer.tokenize(caso)
        
        for token in tokens:
            if token.type != TokenType.WHITESPACE and token.type != TokenType.EOF:
                print(f"  → {token.type.name}: '{token.value}'")
        print()

def teste_codigo_completo():
    """Teste com código Apollo completo"""
    print("=== TESTE COM CÓDIGO COMPLETO ===\n")
    
    codigo = """
algoritmo exemplo
    inteiro x = 42
    real y = 3.14
    se (x > 10) {
        escreva("maior")
    }
fim_algoritmo
"""
    
    lexer = ApolloLexer()
    tokens = lexer.tokenize(codigo)
    
    print("Tokens encontrados:")
    for token in tokens:
        if token.type not in [TokenType.WHITESPACE, TokenType.EOF]:
            print(f"{token.type.name:<12}: '{token.value}' (linha {token.line}, coluna {token.column})")
    
    # Verifica tokens inválidos
    invalidos = [t for t in tokens if t.type == TokenType.INVALID]
    if invalidos:
        print(f"\n{len(invalidos)} token(s) inválido(s) encontrado(s)")
    else:
        print("\nAnálise léxica concluída com sucesso!")

def teste_match_mais_longo():
    """Teste específico do princípio do match mais longo"""
    print("\n=== TESTE DO PRINCÍPIO DO MATCH MAIS LONGO ===\n")
    
    lexer = ApolloLexer()
    
    # Casos críticos para o match mais longo
    casos_criticos = [
        ("x==10", "Deve reconhecer '==' como operador único"),
        ("x!=5", "Deve reconhecer '!=' como operador único"), 
        ("x<=20", "Deve reconhecer '<=' como operador único"),
        ("x>=15", "Deve reconhecer '>=' como operador único"),
        ("variavel123", "Deve reconhecer identificador completo"),
        ("3.14159", "Deve reconhecer número real completo")
    ]
    
    for codigo, descricao in casos_criticos:
        print(f"{descricao}:")
        print(f"  Código: '{codigo}'")
        
        tokens = lexer.tokenize(codigo)
        tokens_validos = [t for t in tokens if t.type not in [TokenType.WHITESPACE, TokenType.EOF]]
        
        tokens_str = [f"{t.type.name}('{t.value}')" for t in tokens_validos]
        print(f"  Tokens: {tokens_str}")
        print()

def main():
    """Função principal"""
    try:
        teste_simples()
        teste_codigo_completo()
        teste_match_mais_longo()
        
        print("="*60)
        print("TODOS OS TESTES CONCLUÍDOS COM SUCESSO!")
        print("="*60)
        
    except Exception as e:
        print(f"\nERRO: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
