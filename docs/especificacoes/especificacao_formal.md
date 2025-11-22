# Especificação Formal da Linguagem Apollo

## 1. Fundamentos Matemáticos

### 1.1 Alfabeto da Linguagem

O alfabeto da linguagem Apollo é definido formalmente como:

**Σ = Σ_letras ∪ Σ_dígitos ∪ Σ_símbolos ∪ Σ_especiais**

Onde:

- **Σ_letras = {a, b, c, ..., z, A, B, C, ..., Z}** (conjunto das letras maiúsculas e minúsculas)
- **Σ_dígitos = {0, 1, 2, ..., 9}** (conjunto dos dígitos decimais)
- **Σ_símbolos = {+, -, *, /, =, <, >, !, (, ), {, }, [, ], :, ;, ,, ., ", ', #, &, |, ^, ~, %, @, $}** (conjunto dos símbolos especiais)
- **Σ_especiais = {\n, \t, \r, \s}** (conjunto dos caracteres de controle e espaços)

### 1.2 Conjuntos de Tokens

Os tokens da linguagem são definidos como subconjuntos de Σ* (fechamento de Kleene do alfabeto):

#### 1.2.1 Identificadores
**ID = {w ∈ Σ* | w = α(α ∪ β)* ∧ α ∈ Σ_letras ∪ {_}}**

Onde β = Σ_letras ∪ Σ_dígitos ∪ {_}

#### 1.2.2 Palavras-chave
**KW = {algoritmo, fim_algoritmo, se, senao, enquanto, para, faca, escreva, leia_numero, leia_texto, verdadeiro, falso, inteiro, real, texto, logico}**

#### 1.2.3 Números Inteiros
**INT = {w ∈ Σ* | w = (+|-)?β+ ∧ β ∈ Σ_dígitos}**

#### 1.2.4 Números Reais
**REAL = {w ∈ Σ* | w = (+|-)?β+.β+ ∧ β ∈ Σ_dígitos}**

#### 1.2.5 Strings
**STR = {"w" | w ∈ (Σ - {"})*}**

#### 1.2.6 Operadores
**OP = {==, !=, <=, >=, <, >, =, +, -, *, /}**

#### 1.2.7 Símbolos
**SYM = {(, ), {, }, [, ], :, ;, ,, .}**

### 1.3 Relações e Funções

#### 1.3.1 Relação de Precedência de Operadores
**PRECEDÊNCIA: OP → ℕ**

Definida como:
- PRECEDÊNCIA(*) = PRECEDÊNCIA(/) = 3
- PRECEDÊNCIA(+) = PRECEDÊNCIA(-) = 2
- PRECEDÊNCIA(<) = PRECEDÊNCIA(>) = PRECEDÊNCIA(<=) = PRECEDÊNCIA(>=) = PRECEDÊNCIA(==) = PRECEDÊNCIA(!=) = 1
- PRECEDÊNCIA(=) = 0

#### 1.3.2 Função de Tokenização
**tokenize: Σ* → Token***

Onde Token é uma estrutura definida como:
**Token = {tipo: TokenType, valor: Σ*, linha: ℕ, coluna: ℕ}**

#### 1.3.3 Relação de Dependência Sintática
**DEPENDÊNCIA ⊆ Token × Token**

Define dependências entre tokens para análise sintática.

## 2. Gramática Formal

A gramática da linguagem Apollo é definida como **G = (N, Σ, P, S)**:

### 2.1 Conjuntos da Gramática

- **N = {Programa, Bloco, Declaração, Comando, Expressão, Termo, Fator, Condicional, Loop, Atribuição, Impressão, Leitura}**
- **Σ = ID ∪ KW ∪ INT ∪ REAL ∪ STR ∪ OP ∪ SYM ∪ {;, {, }}**
- **S = Programa**

### 2.2 Produções

1. **Programa → algoritmo Bloco fim_algoritmo**
2. **Bloco → Declaração* Comando***
3. **Declaração → tipo ID ;**
4. **Comando → Atribuição | Impressão | Leitura | Condicional | Loop**
5. **Atribuição → ID = Expressão ;**
6. **Impressão → escreva ( Expressão ) ;**
7. **Leitura → leia_numero ( ID ) ; | leia_texto ( ID ) ;**
8. **Condicional → se ( Expressão ) { Comando* } senao { Comando* }**
9. **Loop → enquanto ( Expressão ) { Comando* } | para ( Atribuição ; Expressão ; Atribuição ) { Comando* }**
10. **Expressão → Expressão OP Termo | Termo**
11. **Termo → Termo * Fator | Termo / Fator | Fator**
12. **Fator → ( Expressão ) | ID | INT | REAL | STR | verdadeiro | falso**

## 3. Autômatos Finitos Determinísticos (AFDs)

### 3.1 AFD para Identificadores
**M_ID = (Q_ID, Σ_ID, δ_ID, q0_ID, F_ID)**

- **Q_ID = {q0, q1}**
- **Σ_ID = Σ_letras ∪ Σ_dígitos ∪ {_}**
- **δ_ID(q0, α) = q1** para α ∈ Σ_letras ∪ {_}
- **δ_ID(q1, β) = q1** para β ∈ Σ_letras ∪ Σ_dígitos ∪ {_}
- **q0_ID = q0**
- **F_ID = {q1}**

### 3.2 AFD para Números Inteiros
**M_INT = (Q_INT, Σ_INT, δ_INT, q0_INT, F_INT)**

- **Q_INT = {q0, q1, q2}**
- **Σ_INT = Σ_dígitos ∪ {+, -}**
- **δ_INT(q0, +) = δ_INT(q0, -) = q1**
- **δ_INT(q0, d) = δ_INT(q1, d) = q2** para d ∈ Σ_dígitos
- **δ_INT(q2, d) = q2** para d ∈ Σ_dígitos
- **q0_INT = q0**
- **F_INT = {q2}**

### 3.3 AFD para Números Reais
**M_REAL = (Q_REAL, Σ_REAL, δ_REAL, q0_REAL, F_REAL)**

- **Q_REAL = {q0, q1, q2, q3, q4}**
- **Σ_REAL = Σ_dígitos ∪ {+, -, .}**
- **δ_REAL(q0, +) = δ_REAL(q0, -) = q1**
- **δ_REAL(q0, d) = δ_REAL(q1, d) = q2** para d ∈ Σ_dígitos
- **δ_REAL(q2, d) = q2** para d ∈ Σ_dígitos
- **δ_REAL(q2, .) = q3**
- **δ_REAL(q3, d) = q4** para d ∈ Σ_dígitos
- **δ_REAL(q4, d) = q4** para d ∈ Σ_dígitos
- **q0_REAL = q0**
- **F_REAL = {q4}**

## 4. Propriedades da Linguagem

### 4.1 Classificação na Hierarquia de Chomsky
A linguagem Apollo é uma **Gramática Livre de Contexto (Tipo 2)** da hierarquia de Chomsky.

### 4.2 Propriedades de Fechamento
- **União**: L₁ ∪ L₂ é livre de contexto
- **Concatenação**: L₁L₂ é livre de contexto
- **Fechamento de Kleene**: L* é livre de contexto
- **Intersecção**: L₁ ∩ L₂ não é necessariamente livre de contexto
- **Complemento**: L' não é necessariamente livre de contexto

### 4.3 Análise de Ambiguidade
A gramática possui ambiguidades potenciais em:
- Expressões aritméticas (precedência de operadores)
- Estruturas condicionais aninhadas (problema do else pendente)

**Estratégias de resolução:**
- Implementar precedência explícita através de níveis hierárquicos
- Definir associatividade (esquerda para operadores aritméticos)
- Usar gramáticas não ambíguas equivalentes

## 5. Implementação do Analisador Léxico

### 5.1 Princípio do Match Mais Longo
Para cada posição i no código-fonte, o lexer deve encontrar o maior prefixo válido começando em i.

**Algoritmo:**
```
FUNÇÃO longest_match(código, posição):
    melhor_match = NULL
    melhor_comprimento = 0
    
    PARA cada AFD M:
        match = simular_afd(M, código, posição)
        SE match.comprimento > melhor_comprimento:
            melhor_match = match
            melhor_comprimento = match.comprimento
    
    RETORNAR melhor_match
```

### 5.2 Bufferização Eficiente
Implementação de buffer circular para leitura eficiente:

```
ESTRUTURA Buffer:
    dados: array[BUFFER_SIZE]
    início: inteiro
    fim: inteiro
    tamanho: inteiro
```

### 5.3 Integração com Análise Sintática
Interface entre lexer e parser:

```
INTERFACE LexerParser:
    próximo_token(): Token
    retroceder(): void
    obter_posição(): (linha, coluna)
```

## 6. Diário Reflexivo

### 6.1 Decisões de Design
- **Escolha da hierarquia de Chomsky**: Tipo 2 para flexibilidade e poder expressivo
- **Implementação de AFDs separados**: Facilita manutenção e extensibilidade
- **Estrutura de tokens rica**: Inclui posição para melhor tratamento de erros

### 6.2 Desafios Identificados
- Ambiguidade em expressões aritméticas
- Tratamento eficiente de espaços em branco e comentários
- Integração entre análise léxica e sintática

### 6.3 Soluções Implementadas
- Precedência explícita através de níveis gramaticais
- Princípio do match mais longo para resolução de ambiguidades
- Bufferização para eficiência na leitura

### 6.4 Próximos Passos
- Implementação completa do analisador sintático
- Sistema de tratamento de erros robusto
- Otimizações de performance
