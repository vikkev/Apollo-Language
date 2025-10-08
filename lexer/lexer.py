from enum import Enum
from typing import Dict, Set, Optional
import re

class TokenType(Enum):
    IDENTIFIER = "IDENTIFIER"
    KEYWORD = "KEYWORD"
    INTEGER = "INTEGER"
    REAL = "REAL"
    STRING = "STRING"
    OPERATOR = "OPERATOR"
    COMMENT = "COMMENT"
    SYMBOL = "SYMBOL"
    EOF = "EOF"
    INVALID = "INVALID"

class Token:
    def __init__(self, type: TokenType, value: str, line: int = 1, column: int = 1):
        self.type = type
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self) -> str:
        return f"Token({self.type.name}, '{self.value}', {self.line}, {self.column})"

class ApolloLexer:
    def __init__(self, afd=None):
        self.keywords = {'algoritmo', 'fim_algoritmo', 'se', 'senao', 'enquanto',
                         'para', 'faca', 'escreva', 'leia_numero', 'leia_texto',
                         'verdadeiro', 'falso', 'inteiro', 'real', 'texto', 'logico'}
        self.operators = {'==', '!=', '<=', '>=', '<', '>', '=', '+', '-', '*', '/'}
        self.symbols = {'(', ')', ':', ','}
        self.afd = afd

    def tokenize(self, source_code: str) -> list[Token]:
        if self.afd is None:
            raise Exception("AFD não fornecido para o analisador léxico.")
        tokens = []
        line = 1
        column = 1
        i = 0
        while i < len(source_code):
            estado = self.afd.estado_inicial
            inicio = i
            inicio_col = column
            inicio_line = line
            ultimo_final = None
            ultimo_pos = i
            while i < len(source_code):
                char = source_code[i]
                trans = self.afd.transicoes.get((estado, char))
                if trans is None:
                    break
                estado = trans
                i += 1
                column += 1
                if char == '\n':
                    line += 1
                    column = 1
                if estado in self.afd.estados_finais:
                    ultimo_final = estado
                    ultimo_pos = i
            if ultimo_final is not None:
                lexema = source_code[inicio:ultimo_pos]
                # Determinar tipo de token
                if lexema in self.keywords:
                    token_type = TokenType.KEYWORD
                elif lexema in self.operators:
                    token_type = TokenType.OPERATOR
                elif lexema in self.symbols:
                    token_type = TokenType.SYMBOL
                elif re.match(r'^\d+$', lexema):
                    token_type = TokenType.INTEGER
                elif re.match(r'^\d+\.\d+$', lexema):
                    token_type = TokenType.REAL
                elif re.match(r'^".*"$', lexema):
                    token_type = TokenType.STRING
                elif re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', lexema):
                    token_type = TokenType.IDENTIFIER
                else:
                    token_type = TokenType.INVALID
                tokens.append(Token(token_type, lexema, inicio_line, inicio_col))
                i = ultimo_pos
            else:
                if source_code[i].isspace():
                    if source_code[i] == '\n':
                        line += 1
                        column = 1
                    else:
                        column += 1
                    i += 1
                    continue
                tokens.append(Token(TokenType.INVALID, source_code[i], line, column))
                i += 1
                column += 1
        tokens.append(Token(TokenType.EOF, "", line, column))
        return tokens