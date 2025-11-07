def first(grammar):
    first_sets = {non_terminal: set() for non_terminal in grammar}
    
    def first_of(symbol):
        if symbol in first_sets:
            return first_sets[symbol]
        if symbol.islower():  # terminal
            return {symbol}
        
        result = set()
        for production in grammar[symbol]:
            for sym in production:
                sym_first = first_of(sym)
                result.update(sym_first)
                if 'ε' not in sym_first:  # ε não está no conjunto FIRST
                    break
            else:  # se todos os símbolos da produção podem gerar ε
                result.add('ε')
        
        first_sets[symbol] = result
        return result
    
    for non_terminal in grammar:
        first_of(non_terminal)
    
    return first_sets


def follow(grammar, first_sets):
    follow_sets = {non_terminal: set() for non_terminal in grammar}
    follow_sets[list(grammar.keys())[0]].add('$')  # Adiciona símbolo de fim de entrada ao primeiro não-terminal
    
    def follow_of(non_terminal):
        for lhs, productions in grammar.items():
            for production in productions:
                for i, symbol in enumerate(production):
                    if symbol == non_terminal:
                        if i + 1 < len(production):
                            next_symbol = production[i + 1]
                            first_next = first_sets[next_symbol]
                            follow_sets[non_terminal].update(first_next - {'ε'})
                            if 'ε' in first_next:
                                follow_of(lhs)  # Adiciona FOLLOW do lado esquerdo
                        else:
                            follow_of(lhs)  # Adiciona FOLLOW do lado esquerdo
    
    for non_terminal in grammar:
        follow_of(non_terminal)
    
    return follow_sets


def compute_first_follow(grammar):
    first_sets = first(grammar)
    follow_sets = follow(grammar, first_sets)
    return first_sets, follow_sets