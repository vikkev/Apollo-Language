#!/usr/bin/env python3
"""
Teste simples para verificar parse de blocos `{ ... }` no parser Apollo.
"""

import sys
import os
# Adiciona diretório raiz ao path para que pacotes como `lexer` e `parser` sejam importáveis
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from parser.parser import ApolloParser
from lexer.apollo_lexer import ApolloLexer


def main():
    codigo = '''
algoritmo exemplo
{
    inteiro x
    x = 10
    se x > 0 faca {
        escreva("positivo")
    } senao {
        escreva("nao positivo")
    }
}
fim_algoritmo
'''
    lexer = ApolloLexer()
    parser = ApolloParser(lexer)
    ast = parser.parse(codigo)

    print('AST:', ast)

    # Verificações básicas
    assert hasattr(ast, 'declarations')
    assert hasattr(ast, 'statements')
    # Programa tem pelo menos um bloco/statement
    assert len(ast.statements) >= 1

    # Confirma que o primeiro statement é um Block quando usado { ... }
    first = ast.statements[0]
    from parser.ast import Block
    assert isinstance(first, Block), f"Esperado Block, obteve {type(first)}"

    print('Teste de bloco: OK')


if __name__ == '__main__':
    main()
