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
    def __init__(self):
        self.keywords = {'algoritmo', 'fim_algoritmo', 'se', 'senao', 'enquanto',
                         'para', 'faca', 'escreva', 'leia_numero', 'leia_texto',
                         'verdadeiro', 'falso', 'inteiro', 'real', 'texto', 'logico'}
        self.operators = {'==', '!=', '<=', '>=', '<', '>', '=', '+', '-', '*', '/'}
        self.symbols = {'(', ')', ':', ','}

    def tokenize(self, source_code: str) -> list[Token]:
        tokens = []
        line = 1
        column = 1
        i = 0

        while i < len(source_code):
            char = source_code[i]

            if char.isspace():
                if char == '\n':
                    line += 1
                    column = 1
                else:
                    column += 1
                i += 1
                continue

            if char == '#':
                start = i
                while i < len(source_code) and source_code[i] != '\n':
                    i += 1
                continue

            if char == '"':
                start_col = column
                start_line = line
                value = char
                i += 1
                column += 1
                while i < len(source_code) and source_code[i] != '"':
                    value += source_code[i]
                    if source_code[i] == '\n':
                        line += 1
                        column = 1
                    else:
                        column += 1
                    i += 1

                if i < len(source_code) and source_code[i] == '"':
                    value += '"'
                    tokens.append(Token(TokenType.STRING, value, start_line, start_col))
                    i += 1
                    column += 1
                else:
                    tokens.append(Token(TokenType.INVALID, value, start_line, start_col))
                continue

            if i + 1 < len(source_code):
                two_char_op = source_code[i:i+2]
                if two_char_op in self.operators:
                    tokens.append(Token(TokenType.OPERATOR, two_char_op, line, column))
                    i += 2
                    column += 2
                    continue
            
            if char in self.operators:
                tokens.append(Token(TokenType.OPERATOR, char, line, column))
                i += 1
                column += 1
                continue
            
            if char in self.symbols:
                tokens.append(Token(TokenType.SYMBOL, char, line, column))
                i += 1
                column += 1
                continue
            
            if char.isdigit() or (char in '+-' and i + 1 < len(source_code) and source_code[i+1].isdigit()):
                start_col = column
                value = char
                i += 1
                column += 1
                while i < len(source_code) and source_code[i].isdigit():
                    value += source_code[i]
                    i += 1
                    column += 1
                
                if i < len(source_code) and source_code[i] == '.':
                    value += '.'
                    i += 1
                    column += 1
                    while i < len(source_code) and source_code[i].isdigit():
                        value += source_code[i]
                        i += 1
                        column += 1
                    tokens.append(Token(TokenType.REAL, value, line, start_col))
                else:
                    tokens.append(Token(TokenType.INTEGER, value, line, start_col))
                continue
            
            if char.isalpha() or char in 'áàâãéèêíìîóòôõúùûç_ÁÀÂÃÉÈÊÍÌÎÓÒÔÕÚÙÛÇ':
                start_col = column
                value = char
                i += 1
                column += 1
                while i < len(source_code) and (source_code[i].isalnum() or source_code[i] in '_áàâãéèêíìîóòôõúùûçÁÀÂÃÉÈÊÍÌÎÓÒÔÕÚÙÛÇ'):
                    value += source_code[i]
                    i += 1
                    column += 1
                
                token_type = TokenType.KEYWORD if value.lower() in self.keywords else TokenType.IDENTIFIER
                tokens.append(Token(token_type, value, line, start_col))
                continue

            tokens.append(Token(TokenType.INVALID, char, line, column))
            i += 1
            column += 1

        tokens.append(Token(TokenType.EOF, "", line, column))
        return tokens