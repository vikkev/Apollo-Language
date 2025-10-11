"""
Algoritmo de construção de subconjuntos para converter um AFN em AFD.
"""
from collections import deque, defaultdict

class AFN:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_finais):
        # Inicializa o AFN com seus componentes
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes  # dict: (estado, simbolo) -> set(estados)
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais

    def epsilon_closure(self, estados):
        """Retorna o fechamento-ε (epsilon closure) de um conjunto de estados."""
        stack = list(estados)
        closure = set(estados)
        while stack:
            estado = stack.pop()
            for prox in self.transicoes.get((estado, ''), set()):
                if prox not in closure:
                    closure.add(prox)
                    stack.append(prox)
        return closure

    def move(self, estados, simbolo):
        """Retorna o conjunto de estados alcançáveis a partir de 'estados' com o símbolo dado."""
        result = set()
        for estado in estados:
            result.update(self.transicoes.get((estado, simbolo), set()))
        return result

class AFD:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_finais):
        # Inicializa o AFD com seus componentes
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes  # dict: (estado, simbolo) -> estado
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais


def afn_para_afd(afn):
    """
    Converte um AFN em um AFD usando o algoritmo de construção de subconjuntos.
    """
    alfabeto = [s for s in afn.alfabeto if s != '']  # Remove epsilon do alfabeto
    estado_inicial = frozenset(afn.epsilon_closure([afn.estado_inicial]))  # Fechamento-ε do estado inicial
    estados = [estado_inicial]  # Lista de conjuntos de estados do AFD
    fila = deque([estado_inicial])  # Fila para processar novos estados
    transicoes = dict()  # Transições do AFD
    estados_finais = set()  # Estados finais do AFD
    mapeamento = {estado_inicial: 'S0'}  # Mapeia conjuntos de estados para nomes
    nome_estado = 1

    # Processa cada conjunto de estados
    while fila:
        atual = fila.popleft()
        for simbolo in alfabeto:
            # Calcula o próximo conjunto de estados para cada símbolo
            prox = frozenset(afn.epsilon_closure(afn.move(atual, simbolo)))
            if not prox:
                continue  # Ignora se não há transição
            if prox not in mapeamento:
                # Se o conjunto é novo, adiciona à fila e ao mapeamento
                mapeamento[prox] = f'S{nome_estado}'
                nome_estado += 1
                estados.append(prox)
                fila.append(prox)
            # Adiciona a transição ao AFD
            transicoes[(mapeamento[atual], simbolo)] = mapeamento[prox]

    # Define os estados finais do AFD
    for conjunto in estados:
        if any(e in afn.estados_finais for e in conjunto):
            estados_finais.add(mapeamento[conjunto])

    # Retorna o AFD construído
    return AFD(
        estados=list(mapeamento.values()),
        alfabeto=alfabeto,
        transicoes=transicoes,
        estado_inicial=mapeamento[estado_inicial],
        estados_finais=estados_finais
    )

# Exemplo de uso:
# afn = AFN(...)
# afd = afn_para_afd(afn)
