"""
Algoritmo de construção de subconjuntos para converter um AFN em AFD.
"""
from collections import deque, defaultdict

class AFN:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_finais):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes  # dict: (estado, simbolo) -> set(estados)
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais

    def epsilon_closure(self, estados):
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
        result = set()
        for estado in estados:
            result.update(self.transicoes.get((estado, simbolo), set()))
        return result

class AFD:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_finais):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes  # dict: (estado, simbolo) -> estado
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais


def afn_para_afd(afn):
    alfabeto = [s for s in afn.alfabeto if s != '']
    estado_inicial = frozenset(afn.epsilon_closure([afn.estado_inicial]))
    estados = [estado_inicial]
    fila = deque([estado_inicial])
    transicoes = dict()
    estados_finais = set()
    mapeamento = {estado_inicial: 'S0'}
    nome_estado = 1

    while fila:
        atual = fila.popleft()
        for simbolo in alfabeto:
            prox = frozenset(afn.epsilon_closure(afn.move(atual, simbolo)))
            if not prox:
                continue
            if prox not in mapeamento:
                mapeamento[prox] = f'S{nome_estado}'
                nome_estado += 1
                estados.append(prox)
                fila.append(prox)
            transicoes[(mapeamento[atual], simbolo)] = mapeamento[prox]

    for conjunto in estados:
        if any(e in afn.estados_finais for e in conjunto):
            estados_finais.add(mapeamento[conjunto])

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
