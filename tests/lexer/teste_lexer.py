#!/usr/bin/env python3
"""
Script de teste para o analisador léxico Apollo melhorado.
Demonstra o princípio do match mais longo, bufferização e estrutura de tokens.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'lexer'))
from apollo_lexer import ApolloLexer, TokenType, LexerInterface

def test_lexer():
    """Testa o analisador léxico com diferentes casos"""
    
    # Código de exemplo na linguagem Apollo
    codigo_exemplo = """
algoritmo exemplo
    inteiro x = 42
    real y = 3.14
    texto nome = "Apollo"
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
    
    print("=== TESTE DO ANALISADOR LÉXICO APOLLO ===\n")
    print("Código de exemplo:")
    print(codigo_exemplo)
    print("\n" + "="*60 + "\n")
    
    # Cria o lexer
    lexer = ApolloLexer()
    
    # Realiza a tokenização
    tokens = lexer.tokenize(codigo_exemplo)
    
    # Exibe os tokens encontrados
    print("TOKENS RECONHECIDOS:")
    print("-" * 80)
    print(f"{'Token':<20} | {'Tipo':<15} | {'Linha':<6} | {'Coluna':<6} | {'Comprimento'}")
    print("-" * 80)
    
    for token in tokens:
        if token.type != TokenType.WHITESPACE:  # Ignora espaços em branco na exibição
            print(f"{token.value:<20} | {token.type.name:<15} | {token.line:<6} | {token.column:<6} | {token.length}")
    
    print("-" * 80)
    
    # Verifica se há tokens inválidos
    tokens_invalidos = [t for t in tokens if t.type == TokenType.INVALID]
    if tokens_invalidos:
        print(f"\nERRO: {len(tokens_invalidos)} token(s) inválido(s) encontrado(s):")
        for token in tokens_invalidos:
            print(f"   '{token.value}' na linha {token.line}, coluna {token.column}")
    else:
        print("\nAnálise léxica concluída com sucesso!")
    
    return tokens

def test_longest_match():
    """Testa especificamente o princípio do match mais longo"""
    
    print("\n=== TESTE DO PRINCÍPIO DO MATCH MAIS LONGO ===\n")
    
    casos_teste = [
        "x=10",      # Deve reconhecer 'x' como IDENTIFIER, '=' como OPERATOR, '10' como INTEGER
        "x==10",     # Deve reconhecer 'x' como IDENTIFIER, '==' como OPERATOR, '10' como INTEGER
        "x!=10",     # Deve reconhecer 'x' como IDENTIFIER, '!=' como OPERATOR, '10' como INTEGER
        "x<=10",     # Deve reconhecer 'x' como IDENTIFIER, '<=' como OPERATOR, '10' como INTEGER
        "x>=10",     # Deve reconhecer 'x' como IDENTIFIER, '>=' como OPERATOR, '10' como INTEGER
        "variavel123",  # Deve reconhecer como IDENTIFIER completo
        "3.14159",   # Deve reconhecer como REAL completo
        "42",        # Deve reconhecer como INTEGER
        "\"texto\"", # Deve reconhecer como STRING
        "# comentário", # Deve reconhecer como COMMENT
    ]
    
    lexer = ApolloLexer()
    
    for caso in casos_teste:
        print(f"Testando: '{caso}'")
        tokens = lexer.tokenize(caso)
        
        for token in tokens:
            if token.type not in [TokenType.WHITESPACE, TokenType.EOF]:
                print(f"  -> {token.type.name}: '{token.value}'")
        print()

def test_lexer_interface():
    """Testa a interface para integração com análise sintática"""
    
    print("\n=== TESTE DA INTERFACE LEXER-PARSER ===\n")
    
    codigo = "x = 10 + 20"
    lexer = ApolloLexer()
    lexer.reset(codigo)
    
    interface = LexerInterface(lexer)
    
    print(f"Código: '{codigo}'")
    print("\nTokens consumidos sequencialmente:")
    
    token = interface.next_token()
    contador = 1
    
    while token.type != TokenType.EOF:
        print(f"{contador}. {token}")
        token = interface.next_token()
        contador += 1
    
    print(f"{contador}. {token}")

def demonstrar_bufferizacao():
    """Demonstra o funcionamento da bufferização"""
    
    print("\n=== DEMONSTRAÇÃO DA BUFFERIZAÇÃO ===\n")
    
    import sys
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'lexer'))
    from apollo_lexer import CircularBuffer
    
    buffer = CircularBuffer(size=5)
    
    print("Adicionando caracteres ao buffer:")
    caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    
    for char in caracteres:
        buffer.append(char)
        print(f"Adicionado '{char}': buffer = {buffer.buffer[:buffer.count]}")
    
    print(f"\nBuffer final: {buffer.buffer}")
    print(f"Posição inicial: {buffer.start}, Posição final: {buffer.end}")
    print(f"Contagem: {buffer.count}")
    
    print("\nConsumindo caracteres:")
    while not buffer.is_empty():
        char = buffer.consume()
        print(f"Consumido '{char}': restam {buffer.count} caracteres")

def main():
    """Função principal que executa todos os testes"""
    
    try:
        # Teste principal do lexer
        tokens = test_lexer()
        
        # Teste do princípio do match mais longo
        test_longest_match()
        
        # Teste da interface lexer-parser
        test_lexer_interface()
        
        # Demonstração da bufferização
        demonstrar_bufferizacao()
        
        print("\n" + "="*60)
        print("TODOS OS TESTES CONCLUÍDOS COM SUCESSO!")
        print("="*60)
        
    except Exception as e:
        print(f"\nERRO durante a execução dos testes: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
