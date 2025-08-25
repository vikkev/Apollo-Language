# Apollo 

## Sobre o Projeto

Apollo é uma linguagem de programação criada com um objetivo claro: ser a porta de entrada para o mundo da programação para estudantes brasileiros. Acreditamos que aprender a programar não deveria ter a barreira do inglês. Por isso, toda a sintaxe do Apollo é em português, conectando o raciocínio lógico do dia a dia com os comandos que o computador entende

Este projeto está sendo desenvolvido por uma equipe de 3 estudantes ao longo de 8 semanas, como um trabalho prático e conceitual de criação de linguagens

## Características Principais

* **Sintaxe 100% em Português:** Escreva código de forma intuitiva e legível.
* **Foco no Aprendizado:** Mensagens de erro claras e educativas, que ajudam a entender o problema em vez de apenas apontá-lo

### Exemplo de Código

algoritmo calculadora_simples
escreva("Digite o primeiro número:")
numero1 = leia_numero()

escreva("Digite o segundo número:")
numero2 = leia_numero()

soma = numero1 + numero2
escreva("A soma é:", soma)
fim_algoritmo


## Status do Projeto
* Fase 1: Fundamentos e Planejamento (Semanas 1-2)**
* Fase 2: Mão na Massa - Desenvolvimento (Semanas 3-6)**
* Fase 3: Acabamento e Entrega (Semanas 7-8)**

## Nossa Equipe

O projeto é desenvolvido por uma equipe com papéis definidos para garantir o foco e a qualidade:

* **Líder de Projeto:** Lucas Valente
* **Responsável pela Implementação:** Benny , Vinicius Ibaraki, Lucas Valente

---

# Apollo - Detalhes

# Apollo - Especificação Formal da Linguagem

# Apollo - Especificação Formal da Linguagem

## 1. Conjuntos Formais (Σ)

### ΣLetras - Alfabeto Base
```
ΣLetras = {a, b, c, ..., z, A, B, C, ..., Z} ∪ {á, à, â, ã, é, è, ê, í, ì, î, ó, ò, ô, õ, ú, ù, û, ç, _, Á, À, Â, Ã, É, È, Ê, Í, Ì, Î, Ó, Ò, Ô, Õ, Ú, Ù, Û, Ç}
```

### ΣDígitos - Números
```
ΣDígitos = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
```

### ΣSímbolos - Operadores e Delimitadores
```
ΣSímbolos = {+, -, *, /, =, ==, !=, <, >, <=, >=, (, ), :, ,, ", #}
```

### ΣEspaços - Caracteres de Espaçamento
```
ΣEspaços = {' ', '\t', '\n', '\r'}
```

### ΣTipagem - Tipos de Dados
```
ΣTipagem = {inteiro, real, texto, logico}
```

## 2. Definições Formais

### ΣIdentificadores - Regras de Formação
```
ΣIdentificadores = letra · (letra ∪ dígito ∪ _)*

onde:
- letra ∈ ΣLetras
- dígito ∈ ΣDígitos
- Case-insensitive: NOME ≡ nome ≡ Nome
```

**Exemplos válidos:**
- `nome`, `idade`, `valor_total`, `número1`, `média_Alunos`

**Exemplos inválidos:**
- `1nome` (inicia com dígito)
- `valor-total` (hífen não permitido)
- `#comentário` (inicia com símbolo)

### ΣPalavrasChave - Palavras Reservadas
```
ΣPalavrasChave = {
    algoritmo, fim_algoritmo, se, senao, enquanto, para, faca,
    escreva, leia_numero, leia_texto, verdadeiro/falso,
    inteiro, real, texto, logico
}
```

### ΣNúmeros - Definição Formal
```
ΣInteiros = [+-]?[0-9]+
ΣReais = [+-]?[0-9]+\.[0-9]+

Exemplos:
- Inteiros: 42, -17, 0, +25
- Reais: 3.14, -2.5, 100.0, +0.001
```

### ΣStrings - Cadeias de Caracteres
```
ΣStrings = "([^"\n])*"

Exemplos:
- "Olá mundo"
- "Nome: João"
- "Resultado: 42"
```

### ΣComentários - Documentação
```
ΣComentários = #.*$

Onde:
- Inicia com #
- Continua até o final da linha
- Ignorado pelo compilador

Exemplos:
- # Este é um comentário
- soma = a + b  # Calcula a soma
```

## 3. Operadores e Lógicas Matemáticas

### Operadores Aritméticos
```
ΣAritméticos = {+, -, *, /}

Semântica:
- a + b: adição
- a - b: subtração  
- a * b: multiplicação
- a / b: divisão (real se a ou b for real)
```

### Operadores Relacionais
```
ΣRelacionais = {==, !=, <, >, <=, >=}

Lógica Formal:
- a == b ≡ (a = b)         # igualdade
- a != b ≡ ¬(a = b)        # diferença  
- a < b ≡ (a menor que b)   # menor
- a > b ≡ (a maior que b)   # maior
- a <= b ≡ (a < b) ∨ (a = b) # menor ou igual
- a >= b ≡ (a > b) ∨ (a = b) # maior ou igual
```

### Precedência de Operadores
```
1. ( ) - parênteses (maior precedência)
2. * / - multiplicação e divisão
3. + - - adição e subtração  
4. < > <= >= - relacionais
5. == != - igualdade
6. = - atribuição (menor precedência)
```

## 4. CamelCase e Convenções

### Identificadores CamelCase
```
ΣCamelCase = letraMinúscula · (letra ∪ dígito)*
           | letraMaiúscula · (letra ∪ dígito)*

Convenções:
- Variáveis: camelCase (minúscula inicial)
- Constantes: SNAKE_CASE (maiúsculas)
- Funções: camelCase

Exemplos:
- nomeCompleto, idadeUsuario, valorTotal
- PI, MAX_VALOR, NOME_SISTEMA
- calcularMedia, obterNome, mostrarResultado
```

## 5. Estrutura Formal do Programa

### Gramática Básica
```
Programa ::= 'algoritmo' Identificador Corpo 'fim_algoritmo'
Corpo ::= (Declaracao | Comando)*
Declaracao ::= Tipo Identificador ('=' Expressao)?
Comando ::= Atribuicao | Entrada | Saida | Controle
Expressao ::= Termo (OperadorBinario Termo)*

Exemplo de Derivação:
algoritmo → calculadora
Corpo → Comando*
Comando → escreva("Digite número:")
Comando → numero = leia_numero()
```

## 6. Exemplo Prático com Notação Formal

```apollo
algoritmo exemploFormal
  # ΣComentários: documentação do programa
  
  # ΣTipagem: declarações de tipos
  inteiro numero1, numero2, resultado
  real media
  texto nome
  logico aprovado
  
  # ΣEntrada: leitura de dados
  escreva("Digite seu nome:")
  nome = leia_texto()
  
  escreva("Digite primeiro número:")
  numero1 = leia_numero()
  
  escreva("Digite segundo número:")  
  numero2 = leia_numero()
  
  # ΣAritméticos: operações matemáticas
  resultado = numero1 + numero2
  media = resultado / 2.0
  
  # ΣRelacionais: lógica de comparação
  se media >= 7.0 faca
    aprovado = verdadeiro
    escreva(nome, ", você foi aprovado!")
  senao
    aprovado = falso
    escreva(nome, ", você foi reprovado.")
  
  # ΣSaída: exibição dos resultados
  escreva("Soma:", resultado)
  escreva("Média:", media)
  escreva("Status:", aprovado)
fim_algoritmo
```

## 7. Validação Formal

### Regras de Validação
```
∀ identificador ∈ Programa:
  identificador ∈ ΣIdentificadores ∧ 
  identificador ∉ ΣPalavrasChave

∀ expressão ∈ Programa:
  tipo(expressão) ∈ ΣTipagem ∧
  precedência(operadores) ∈ {1,2,3,4,5,6}

∀ string ∈ Programa:
  string ∈ ΣStrings ∧ 
  comprimento(string) ≥ 2
```
