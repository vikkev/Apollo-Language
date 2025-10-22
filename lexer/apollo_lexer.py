from enum import Enum
from typing import Dict, Set, Optional, List, Tuple
import re
from dataclasses import dataclass
from collections import deque

class TokenType(Enum):
    """Enumeração dos tipos de tokens reconhecidos pela linguagem Apollo"""
    # Identificadores e palavras-chave
    IDENTIFIER = "IDENTIFIER"
    KEYWORD = "KEYWORD"
    
    # Literais
    INTEGER = "INTEGER"
    REAL = "REAL"
    STRING = "STRING"
    BOOLEAN = "BOOLEAN"
    
    # Operadores
    OPERATOR = "OPERATOR"
    
    # Símbolos
    SYMBOL = "SYMBOL"
    
    # Controle
    EOF = "EOF"
    INVALID = "INVALID"
    COMMENT = "COMMENT"
    WHITESPACE = "WHITESPACE"

@dataclass
class Token:
    """Estrutura completa de um token com informações de posição e contexto"""
    type: TokenType
    value: str
    line: int
    column: int
    length: int = 0
    
    def __post_init__(self):
        if self.length == 0:
            self.length = len(self.value)
    
    def __repr__(self) -> str:
        return f"Token({self.type.name}, '{self.value}', linha={self.line}, coluna={self.column})"
    
    def __str__(self) -> str:
        return f"{self.type.name}: '{self.value}'"

class CircularBuffer:
    """Buffer circular eficiente para leitura de caracteres"""
    
    def __init__(self, size: int = 4096):
        self.buffer = [''] * size
        self.size = size
        self.start = 0
        self.end = 0
        self.count = 0
    
    def append(self, char: str):
        """Adiciona um caractere ao buffer"""
        if self.count < self.size:
            self.buffer[self.end] = char
            self.end = (self.end + 1) % self.size
            self.count += 1
        else:
            # Buffer cheio, substitui o caractere mais antigo
            self.buffer[self.end] = char
            self.end = (self.end + 1) % self.size
            self.start = (self.start + 1) % self.size
    
    def peek(self, offset: int = 0) -> Optional[str]:
        """Retorna o caractere na posição offset sem consumir"""
        if offset >= self.count:
            return None
        pos = (self.start + offset) % self.size
        return self.buffer[pos]
    
    def consume(self, count: int = 1) -> str:
        """Consome e retorna os próximos count caracteres"""
        result = ""
        for i in range(min(count, self.count)):
            result += self.buffer[self.start]
            self.start = (self.start + 1) % self.size
            self.count -= 1
        return result
    
    def is_empty(self) -> bool:
        return self.count == 0

class AFD:
    """Autômato Finito Determinístico para reconhecimento de tokens"""
    
    def __init__(self, name: str, initial_state: int, final_states: Set[int], 
                 transitions: Dict[Tuple[int, str], int]):
        self.name = name
        self.initial_state = initial_state
        self.final_states = final_states
        self.transitions = transitions
    
    def simulate(self, text: str, start_pos: int) -> Optional[Tuple[int, int]]:
        """
        Simula o AFD a partir de start_pos no texto.
        Retorna (final_pos, estado_final) se reconhecer, None caso contrário.
        """
        state = self.initial_state
        pos = start_pos
        
        while pos < len(text):
            char = text[pos]
            key = (state, char)
            
            # Tratamento especial para strings e comentários
            if self.name == 'string' and state == 1:
                # No estado 1 de string, aceita qualquer caractere exceto aspas
                if char == '"':
                    state = 2
                    pos += 1
                    break
                else:
                    pos += 1
                    continue
            elif self.name == 'comment' and state == 1:
                # No estado 1 de comentário, aceita qualquer caractere exceto quebra de linha
                if char == '\n':
                    state = 2
                    pos += 1
                    break
                elif pos == len(text) - 1:
                    # Se chegou ao fim do texto, considera o comentário completo
                    state = 2
                    pos += 1
                    break
                else:
                    pos += 1
                    continue
            
            if key not in self.transitions:
                break
            
            state = self.transitions[key]
            pos += 1
        
        if state in self.final_states:
            return (pos, state)
        return None

class ApolloLexer:
    """Analisador léxico da linguagem Apollo com princípio do match mais longo"""
    
    def __init__(self):
        # Palavras-chave da linguagem Apollo
        self.keywords = {
            'algoritmo', 'fim_algoritmo', 'se', 'senao', 'enquanto',
            'para', 'faca', 'escreva', 'leia_numero', 'leia_texto',
            'verdadeiro', 'falso', 'inteiro', 'real', 'texto', 'logico'
        }
        
        # Operadores com precedência
        self.operators = {
            '==', '!=', '<=', '>=', '<', '>', '=', '+', '-', '*', '/'
        }
        
        # Símbolos especiais
        self.symbols = {'(', ')', '{', '}', '[', ']', ':', ',', ';', '.'}
        
        # AFDs para reconhecimento de tokens
        self.afds = self._create_afds()
        
        # Buffer para leitura eficiente
        self.buffer = CircularBuffer()
        
        # Estado do lexer
        self.position = 0
        self.line = 1
        self.column = 1
        self.source = ""
    
    def _create_afds(self) -> Dict[str, AFD]:
        """Cria os AFDs para reconhecimento de diferentes tipos de tokens"""
        afds = {}
        
        # AFD para identificadores
        afds['identifier'] = AFD(
            name='identifier',
            initial_state=0,
            final_states={1},
            transitions={
                (0, 'a'): 1, (0, 'b'): 1, (0, 'c'): 1, (0, 'd'): 1, (0, 'e'): 1,
                (0, 'f'): 1, (0, 'g'): 1, (0, 'h'): 1, (0, 'i'): 1, (0, 'j'): 1,
                (0, 'k'): 1, (0, 'l'): 1, (0, 'm'): 1, (0, 'n'): 1, (0, 'o'): 1,
                (0, 'p'): 1, (0, 'q'): 1, (0, 'r'): 1, (0, 's'): 1, (0, 't'): 1,
                (0, 'u'): 1, (0, 'v'): 1, (0, 'w'): 1, (0, 'x'): 1, (0, 'y'): 1,
                (0, 'z'): 1, (0, 'A'): 1, (0, 'B'): 1, (0, 'C'): 1, (0, 'D'): 1,
                (0, 'E'): 1, (0, 'F'): 1, (0, 'G'): 1, (0, 'H'): 1, (0, 'I'): 1,
                (0, 'J'): 1, (0, 'K'): 1, (0, 'L'): 1, (0, 'M'): 1, (0, 'N'): 1,
                (0, 'O'): 1, (0, 'P'): 1, (0, 'Q'): 1, (0, 'R'): 1, (0, 'S'): 1,
                (0, 'T'): 1, (0, 'U'): 1, (0, 'V'): 1, (0, 'W'): 1, (0, 'X'): 1,
                (0, 'Y'): 1, (0, 'Z'): 1, (0, '_'): 1,
                # Transições do estado 1 (aceita letras, dígitos e _)
                (1, 'a'): 1, (1, 'b'): 1, (1, 'c'): 1, (1, 'd'): 1, (1, 'e'): 1,
                (1, 'f'): 1, (1, 'g'): 1, (1, 'h'): 1, (1, 'i'): 1, (1, 'j'): 1,
                (1, 'k'): 1, (1, 'l'): 1, (1, 'm'): 1, (1, 'n'): 1, (1, 'o'): 1,
                (1, 'p'): 1, (1, 'q'): 1, (1, 'r'): 1, (1, 's'): 1, (1, 't'): 1,
                (1, 'u'): 1, (1, 'v'): 1, (1, 'w'): 1, (1, 'x'): 1, (1, 'y'): 1,
                (1, 'z'): 1, (1, 'A'): 1, (1, 'B'): 1, (1, 'C'): 1, (1, 'D'): 1,
                (1, 'E'): 1, (1, 'F'): 1, (1, 'G'): 1, (1, 'H'): 1, (1, 'I'): 1,
                (1, 'J'): 1, (1, 'K'): 1, (1, 'L'): 1, (1, 'M'): 1, (1, 'N'): 1,
                (1, 'O'): 1, (1, 'P'): 1, (1, 'Q'): 1, (1, 'R'): 1, (1, 'S'): 1,
                (1, 'T'): 1, (1, 'U'): 1, (1, 'V'): 1, (1, 'W'): 1, (1, 'X'): 1,
                (1, 'Y'): 1, (1, 'Z'): 1, (1, '_'): 1,
                (1, '0'): 1, (1, '1'): 1, (1, '2'): 1, (1, '3'): 1, (1, '4'): 1,
                (1, '5'): 1, (1, '6'): 1, (1, '7'): 1, (1, '8'): 1, (1, '9'): 1
            }
        )
        
        # AFD para números inteiros
        afds['integer'] = AFD(
            name='integer',
            initial_state=0,
            final_states={2},
            transitions={
                (0, '+'): 1, (0, '-'): 1,
                (0, '0'): 2, (0, '1'): 2, (0, '2'): 2, (0, '3'): 2, (0, '4'): 2,
                (0, '5'): 2, (0, '6'): 2, (0, '7'): 2, (0, '8'): 2, (0, '9'): 2,
                (1, '0'): 2, (1, '1'): 2, (1, '2'): 2, (1, '3'): 2, (1, '4'): 2,
                (1, '5'): 2, (1, '6'): 2, (1, '7'): 2, (1, '8'): 2, (1, '9'): 2,
                (2, '0'): 2, (2, '1'): 2, (2, '2'): 2, (2, '3'): 2, (2, '4'): 2,
                (2, '5'): 2, (2, '6'): 2, (2, '7'): 2, (2, '8'): 2, (2, '9'): 2
            }
        )
        
        # AFD para números reais
        afds['real'] = AFD(
            name='real',
            initial_state=0,
            final_states={4},
            transitions={
                (0, '+'): 1, (0, '-'): 1,
                (0, '0'): 2, (0, '1'): 2, (0, '2'): 2, (0, '3'): 2, (0, '4'): 2,
                (0, '5'): 2, (0, '6'): 2, (0, '7'): 2, (0, '8'): 2, (0, '9'): 2,
                (1, '0'): 2, (1, '1'): 2, (1, '2'): 2, (1, '3'): 2, (1, '4'): 2,
                (1, '5'): 2, (1, '6'): 2, (1, '7'): 2, (1, '8'): 2, (1, '9'): 2,
                (2, '0'): 2, (2, '1'): 2, (2, '2'): 2, (2, '3'): 2, (2, '4'): 2,
                (2, '5'): 2, (2, '6'): 2, (2, '7'): 2, (2, '8'): 2, (2, '9'): 2,
                (2, '.'): 3,
                (3, '0'): 4, (3, '1'): 4, (3, '2'): 4, (3, '3'): 4, (3, '4'): 4,
                (3, '5'): 4, (3, '6'): 4, (3, '7'): 4, (3, '8'): 4, (3, '9'): 4,
                (4, '0'): 4, (4, '1'): 4, (4, '2'): 4, (4, '3'): 4, (4, '4'): 4,
                (4, '5'): 4, (4, '6'): 4, (4, '7'): 4, (4, '8'): 4, (4, '9'): 4
            }
        )
        
        # AFD para strings - reconhece strings completas entre aspas
        afds['string'] = AFD(
            name='string',
            initial_state=0,
            final_states={2},
            transitions={
                (0, '"'): 1,
                (1, '"'): 2,
                # Estado 1 aceita qualquer caractere exceto aspas
                # Isso será tratado dinamicamente na simulação
            }
        )
        
        # AFD para comentários - reconhece comentários completos até quebra de linha
        afds['comment'] = AFD(
            name='comment',
            initial_state=0,
            final_states={2},
            transitions={
                (0, '#'): 1,
                (1, '\n'): 2,
                # Estado 1 aceita qualquer caractere exceto quebra de linha
                # Isso será tratado dinamicamente na simulação
            }
        )
        
        return afds
    
    def _longest_match(self, text: str, start_pos: int) -> Optional[Tuple[str, TokenType, int]]:
        """
        Implementa o princípio do match mais longo.
        Retorna (lexema, tipo, posição_final) do match mais longo encontrado.
        """
        best_match = None
        best_length = 0
        
        # Testa cada AFD
        for afd_name, afd in self.afds.items():
            result = afd.simulate(text, start_pos)
            if result:
                final_pos, _ = result
                length = final_pos - start_pos
                
                if length > best_length:
                    lexema = text[start_pos:final_pos]
                    token_type = self._determine_token_type(lexema, afd_name)
                    best_match = (lexema, token_type, final_pos)
                    best_length = length
        
        # Testa operadores e símbolos (match exato)
        for op in sorted(self.operators, key=len, reverse=True):
            if text.startswith(op, start_pos):
                length = len(op)
                if length > best_length:
                    best_match = (op, TokenType.OPERATOR, start_pos + length)
                    best_length = length
        
        for sym in self.symbols:
            if text.startswith(sym, start_pos):
                length = len(sym)
                if length > best_length:
                    best_match = (sym, TokenType.SYMBOL, start_pos + length)
                    best_length = length
        
        return best_match
    
    def _determine_token_type(self, lexema: str, afd_name: str) -> TokenType:
        """Determina o tipo de token baseado no lexema e AFD que o reconheceu"""
        if afd_name == 'identifier':
            if lexema in {'verdadeiro', 'falso'}:
                return TokenType.BOOLEAN
            elif lexema in self.keywords:
                return TokenType.KEYWORD
            else:
                return TokenType.IDENTIFIER
        elif afd_name == 'integer':
            return TokenType.INTEGER
        elif afd_name == 'real':
            return TokenType.REAL
        elif afd_name == 'string':
            return TokenType.STRING
        elif afd_name == 'comment':
            return TokenType.COMMENT
        else:
            return TokenType.INVALID
    
    def _update_position(self, char: str):
        """Atualiza a posição (linha e coluna) baseada no caractere"""
        if char == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1
    
    def tokenize(self, source_code: str) -> List[Token]:
        """
        Realiza a análise léxica do código-fonte usando o princípio do match mais longo.
        Retorna uma lista de tokens.
        """
        self.source = source_code
        self.position = 0
        self.line = 1
        self.column = 1
        tokens = []
        
        while self.position < len(source_code):
            # Pula espaços em branco
            if source_code[self.position].isspace():
                start_line = self.line
                start_col = self.column
                whitespace = ""
                
                while (self.position < len(source_code) and 
                       source_code[self.position].isspace()):
                    char = source_code[self.position]
                    whitespace += char
                    self._update_position(char)
                    self.position += 1
                
                # Adiciona token de espaço em branco (opcional, para debug)
                if whitespace:
                    tokens.append(Token(
                        TokenType.WHITESPACE, 
                        whitespace, 
                        start_line, 
                        start_col
                    ))
                continue
            
            # Aplica o princípio do match mais longo
            match = self._longest_match(source_code, self.position)
            
            if match:
                lexema, token_type, final_pos = match
                start_line = self.line
                start_col = self.column
                
                # Atualiza posição
                for i in range(self.position, final_pos):
                    self._update_position(source_code[i])
                
                # Cria token
                token = Token(token_type, lexema, start_line, start_col)
                tokens.append(token)
                
                self.position = final_pos
            else:
                # Caractere não reconhecido
                char = source_code[self.position]
                tokens.append(Token(
                    TokenType.INVALID, 
                    char, 
                    self.line, 
                    self.column
                ))
                self._update_position(char)
                self.position += 1
        
        # Adiciona token de fim de arquivo
        tokens.append(Token(TokenType.EOF, "", self.line, self.column))
        
        return tokens
    
    def get_next_token(self) -> Token:
        """Interface para análise sintática - retorna o próximo token"""
        if not hasattr(self, '_token_stream') or self._token_stream is None:
            self._token_stream = iter(self.tokenize(self.source))
            self._current_token = None
        
        if self._current_token is None:
            try:
                self._current_token = next(self._token_stream)
            except StopIteration:
                self._current_token = Token(TokenType.EOF, "", self.line, self.column)
        
        return self._current_token
    
    def consume_token(self) -> Token:
        """Consome o token atual e retorna o próximo"""
        current = self.get_next_token()
        self._current_token = None
        return current
    
    def peek_token(self) -> Token:
        """Retorna o próximo token sem consumir"""
        return self.get_next_token()
    
    def reset(self, source_code: str):
        """Reinicia o lexer com novo código-fonte"""
        self.source = source_code
        self.position = 0
        self.line = 1
        self.column = 1
        self._token_stream = None
        self._current_token = None

# Interface para integração com análise sintática
class LexerInterface:
    """Interface padronizada entre lexer e parser"""
    
    def __init__(self, lexer: ApolloLexer):
        self.lexer = lexer
        self.token_buffer = deque()
        self.buffer_size = 10
    
    def next_token(self) -> Token:
        """Retorna o próximo token"""
        if self.token_buffer:
            return self.token_buffer.popleft()
        return self.lexer.get_next_token()
    
    def peek_token(self, offset: int = 0) -> Token:
        """Retorna o token na posição offset sem consumir"""
        while len(self.token_buffer) <= offset:
            token = self.lexer.get_next_token()
            self.token_buffer.append(token)
        
        return self.token_buffer[offset]
    
    def backtrack(self, count: int = 1):
        """Retrocede count tokens (implementação simplificada)"""
        # Em uma implementação completa, seria necessário manter
        # um histórico de tokens consumidos
        pass
    
    def get_position(self) -> Tuple[int, int]:
        """Retorna a posição atual (linha, coluna)"""
        return (self.lexer.line, self.lexer.column)
