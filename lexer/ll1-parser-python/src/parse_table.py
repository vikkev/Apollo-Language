class ParseTable:
    def __init__(self, grammar):
        self.grammar = grammar
        self.parse_table = {}
        self.first_sets = {}
        self.follow_sets = {}
        self.build_first_follow_sets()
        self.build_parse_table()

    def build_first_follow_sets(self):
        from first_follow import FirstFollow

        ff = FirstFollow(self.grammar)
        self.first_sets = ff.first_sets
        self.follow_sets = ff.follow_sets

    def build_parse_table(self):
        for non_terminal in self.grammar:
            self.parse_table[non_terminal] = {}
            for production in self.grammar[non_terminal]:
                first_set = self.get_first_set(production)
                for terminal in first_set:
                    if terminal != 'ε':  # ε is the empty string
                        self.parse_table[non_terminal][terminal] = production
                if 'ε' in first_set:
                    follow_set = self.follow_sets[non_terminal]
                    for terminal in follow_set:
                        self.parse_table[non_terminal][terminal] = production

    def get_first_set(self, production):
        first_set = set()
        for symbol in production:
            if symbol in self.grammar:  # Non-terminal
                first_set.update(self.first_sets[symbol] - {'ε'})
                if 'ε' not in self.first_sets[symbol]:
                    break
            else:  # Terminal
                first_set.add(symbol)
                break
        return first_set

    def get_parse_table(self):
        return self.parse_table