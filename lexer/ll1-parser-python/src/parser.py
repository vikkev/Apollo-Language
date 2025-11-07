class Parser:
    def __init__(self, parse_table, tokens):
        self.parse_table = parse_table
        self.tokens = tokens
        self.stack = []
        self.current_token_index = 0

    def parse(self):
        self.stack.append('$')  # End of input symbol
        self.stack.append('E')  # Start symbol

        while self.stack:
            top = self.stack.pop()
            current_token = self.get_current_token()

            if top == current_token:
                self.current_token_index += 1  # Move to the next token
            elif top in self.parse_table:
                production = self.parse_table[top].get(current_token)
                if production:
                    for symbol in reversed(production):
                        if symbol != 'ε':  # ε represents an empty production
                            self.stack.append(symbol)
                else:
                    raise SyntaxError(f"Unexpected token: {current_token}")
            else:
                raise SyntaxError(f"Unexpected symbol on stack: {top}")

    def get_current_token(self):
        if self.current_token_index < len(self.tokens):
            return self.tokens[self.current_token_index]
        return '$'  # End of input

    def print_parse_tree(self):
        # This method can be implemented to display the parse tree
        pass

# Example usage:
# parse_table = {
#     'E': {'NUM': ['NUM'], '+': ['E', '+', 'E'], '(': ['(', 'E', ')']},
#     # Add other productions here
# }
# tokens = ['NUM', '+', 'NUM']
# parser = Parser(parse_table, tokens)
# parser.parse()