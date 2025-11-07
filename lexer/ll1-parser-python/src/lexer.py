class Lexer:
    def __init__(self, input_string):
        self.input_string = input_string
        self.position = 0
        self.current_char = self.input_string[self.position] if self.input_string else None
        self.tokens = []

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        """Move to the next character in the input string."""
        self.position += 1
        if self.position < len(self.input_string):
            self.current_char = self.input_string[self.position]
        else:
            self.current_char = None

    def skip_whitespace(self):
        """Skip whitespace characters."""
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        """Return a multi-digit integer from the input string."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return ('INTEGER', int(result))

    def operator(self):
        """Return an operator token."""
        token = self.current_char
        self.advance()
        return ('OPERATOR', token)

    def parenthesis(self):
        """Return a parenthesis token."""
        token = self.current_char
        self.advance()
        return ('PARENTHESIS', token)

    def get_next_token(self):
        """Lexical analyzer that breaks down the input string into tokens."""
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            if self.current_char.isdigit():
                return self.integer()
            if self.current_char in ('+', '-', '*', '/'):
                return self.operator()
            if self.current_char in ('(', ')'):
                return self.parenthesis()
            self.error()
        return ('EOF', None)

    def tokenize(self):
        """Tokenize the entire input string."""
        while True:
            token = self.get_next_token()
            self.tokens.append(token)
            if token[0] == 'EOF':
                break
        return self.tokens