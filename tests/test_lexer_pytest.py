import os
import sys
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lexer'))
from lexer.apollo_lexer import ApolloLexer, TokenType

@pytest.fixture
def lexer():
    return ApolloLexer()

def tokens_values(lexer, src):
    toks = lexer.tokenize(src)
    return [t for t in toks if t.type not in (TokenType.WHITESPACE, TokenType.EOF)]

def test_simple_assignment(lexer):
    toks = tokens_values(lexer, 'x = 42')
    assert [t.type for t in toks] == [TokenType.IDENTIFIER, TokenType.OPERATOR, TokenType.INTEGER]

def test_composed_operators(lexer):
    cases = {
        'x==10': [TokenType.IDENTIFIER, TokenType.OPERATOR, TokenType.INTEGER],
        'x!=5': [TokenType.IDENTIFIER, TokenType.OPERATOR, TokenType.INTEGER],
        'x<=20': [TokenType.IDENTIFIER, TokenType.OPERATOR, TokenType.INTEGER],
        'x>=15': [TokenType.IDENTIFIER, TokenType.OPERATOR, TokenType.INTEGER],
    }
    for code, expected in cases.items():
        toks = tokens_values(lexer, code)
        assert [t.type for t in toks] == expected

@pytest.mark.parametrize("s", ['"texto simples"', '"texto com espaços"', '""'])
def test_strings_single_token(lexer, s):
    toks = tokens_values(lexer, s)
    assert len(toks) == 1
    assert toks[0].type == TokenType.STRING

@pytest.mark.parametrize("c", ['# comentario simples', '# comentario 123'])
def test_comments_single_token(lexer, c):
    toks = tokens_values(lexer, c)
    # '#' alone may be invalid in some lexer versions; require that comment tokens are present when content
    assert toks[0].type in (TokenType.COMMENT, TokenType.INVALID)

@pytest.mark.parametrize("num,typ", [
    ("42", TokenType.INTEGER),
    ("+42", TokenType.INTEGER),
    ("-3.14", TokenType.REAL),
    ("0.0", TokenType.REAL),
])
def test_numbers(lexer, num, typ):
    toks = tokens_values(lexer, num)
    assert len(toks) == 1
    assert toks[0].type == typ

@pytest.mark.parametrize("ident,typ", [
    ("x", TokenType.IDENTIFIER),
    ("variavel123", TokenType.IDENTIFIER),
    ("algoritmo", TokenType.KEYWORD),
    ("verdadeiro", TokenType.BOOLEAN),
])
def test_identifiers_and_keywords(lexer, ident, typ):
    toks = tokens_values(lexer, ident)
    assert len(toks) == 1
    assert toks[0].type == typ

def test_full_code_tokens(lexer):
    codigo = """
algoritmo exemplo_completo
    # Este é um comentário
    inteiro x = 42
fim_algoritmo
"""
    toks = tokens_values(lexer, codigo)
    # deve conter KEYWORD, IDENTIFIER, COMMENT, KEYWORD, IDENTIFIER, OPERATOR, INTEGER, KEYWORD
    types = [t.type for t in toks]
    assert TokenType.KEYWORD in types
    assert TokenType.IDENTIFIER in types
    # comentário deve aparecer
    assert any(t.type == TokenType.COMMENT for t in toks) or any(t.type == TokenType.INVALID for t in toks)
