# Primeira Versão da Gramática Formal da Linguagem

## 1. Introdução
Este documento apresenta a primeira versão da gramática formal da linguagem em desenvolvimento, seguindo os conceitos da hierarquia de Chomsky. O objetivo é estruturar os principais elementos sintáticos da linguagem, classificá-la dentro da hierarquia formal e analisar possíveis ambiguidades.

---

## 2. Primeira Versão da Gramática Formal

A gramática da linguagem pode ser definida pelo conjunto *G = (N, Σ, P, S)*, em que:

- *N*: conjunto de variáveis não-terminais.  
- *Σ*: conjunto de símbolos terminais.  
- *P*: conjunto de produções.  
- *S*: símbolo inicial.

### Definições
- *N = {Programa, Decl, Cmd, Expr, Termo, Fator}*  
- *Σ = {id, num, =, +, -, *, /, ;, print, ( , )}*  
- *S = Programa*

### Produções
1. Programa → Decl Cmd  
2. Decl → id = Expr ; | ε  
3. Cmd → print ( Expr ) ; | id = Expr ; | Cmd Cmd  
4. Expr → Expr + Termo | Expr - Termo | Termo  
5. Termo → Termo * Fator | Termo / Fator | Fator  
6. Fator → ( Expr ) | id | num  

---

## 3. Classificação na Hierarquia de Chomsky
A gramática proposta é uma *Gramática Livre de Contexto (GLC), ou seja, de **Tipo 2* na hierarquia de Chomsky.  
- Justificativa: todas as regras de produção possuem apenas um não-terminal no lado esquerdo e uma sequência de símbolos (terminais e/ou não-terminais) no lado direito.

---

## 4. Exemplos de Derivações

### Exemplo 1: Declaração de variável
Decl ⇒ id = Expr ;
⇒ id = Termo ;
⇒ id = Fator ;
⇒ id = num ;

### Exemplo 2: Atribuição com expressão aritmética
Cmd ⇒ id = Expr ;
⇒ id = Expr + Termo ;
⇒ id = Termo + Termo ;
⇒ id = num + id ;

### Exemplo 3: Impressão
Cmd ⇒ print ( Expr ) ;
⇒ print ( Termo ) ;
⇒ print ( num ) ;

---

## 5. Análise de Ambiguidades Potenciais

A gramática, na forma atual, apresenta ambiguidades em expressões aritméticas devido à ausência de regras claras de *precedência* e *associatividade*. Por exemplo:

Expr ⇒ Expr + Expr * Expr

Pode ser derivado como:
1. (Expr + Expr) * Expr  
2. Expr + (Expr * Expr)

### Estratégias de Resolução
- Estabelecer níveis hierárquicos entre *Expr, **Termo* e *Fator*, como já iniciado, para refletir precedência.  
- Definir regras de associatividade (por exemplo, associatividade à esquerda para + e -).  
- Eventualmente, aplicar algoritmos de eliminação de ambiguidades (como fatoração ou uso de gramáticas não ambíguas equivalentes).

---

## 6. Conclusão
A primeira versão da gramática formal permite representar estruturas básicas da linguagem proposta, garantindo uma classificação como gramática do *Tipo 2* da hierarquia de Chomsky. Apesar disso, ainda existem ambiguidades potenciais, especialmente em expressões aritméticas, que deverão ser refinadas em versões futuras.

---