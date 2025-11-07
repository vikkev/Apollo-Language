class Grammar:
    def __init__(self):
        self.productions = {
            'E': [['E', 'T'], ['T']],
            'T': [['T', 'F'], ['F']],
            'F': [['(', 'E', ')'], ['id'], ['num']]
        }
        self.first_sets = {}
        self.follow_sets = {}
        self.start_symbol = 'E'

    def add_production(self, non_terminal, production):
        if non_terminal in self.productions:
            self.productions[non_terminal].append(production)
        else:
            self.productions[non_terminal] = [production]

    def compute_first(self):
        for non_terminal in self.productions:
            self.first_sets[non_terminal] = set()
        changed = True
        while changed:
            changed = False
            for non_terminal, productions in self.productions.items():
                for production in productions:
                    for symbol in production:
                        if symbol.islower() or symbol in ['num', 'id']:  # Terminal
                            if symbol not in self.first_sets[non_terminal]:
                                self.first_sets[non_terminal].add(symbol)
                                changed = True
                            break
                        else:  # Non-terminal
                            first_of_symbol = self.first_sets.get(symbol, set())
                            if first_of_symbol - self.first_sets[non_terminal]:
                                self.first_sets[non_terminal].update(first_of_symbol)
                                changed = True
                            if 'ε' not in first_of_symbol:
                                break
                    else:
                        self.first_sets[non_terminal].add('ε')
                        changed = True

    def compute_follow(self):
        for non_terminal in self.productions:
            self.follow_sets[non_terminal] = set()
        self.follow_sets[self.start_symbol].add('$')  # End of input symbol
        changed = True
        while changed:
            changed = False
            for non_terminal, productions in self.productions.items():
                for production in productions:
                    for i, symbol in enumerate(production):
                        if symbol in self.productions:  # Non-terminal
                            if i + 1 < len(production):
                                next_symbol = production[i + 1]
                                first_of_next = self.first_sets.get(next_symbol, set())
                                self.follow_sets[symbol].update(first_of_next - {'ε'})
                                if 'ε' in first_of_next:
                                    self.follow_sets[symbol].update(self.follow_sets[non_terminal])
                            else:
                                self.follow_sets[symbol].update(self.follow_sets[non_terminal])
                            if self.follow_sets[symbol] - self.follow_sets[symbol]:
                                changed = True

    def get_first_sets(self):
        return self.first_sets

    def get_follow_sets(self):
        return self.follow_sets

    def get_productions(self):
        return self.productions