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

## 1. Alfabeto da Linguagem
- **Letras:** a-z, A-Z (com acentos), _
- **Dígitos:** 0-9
- **Símbolos:** + - * / = == != < > <= >= ( ) : , " #
- **Espaços:** espaço, tab, quebra de linha

## 2. Tokens

### Palavras-Chave
```
algoritmo, fim_algoritmo, se, senao, enquanto, para, faca, 
escreva, leia_numero, verdadeiro, falso
```

### Identificadores
- Formato: `letra(letra|dígito|_)*`
- Case-insensitive
- Exemplos: `nome`, `idade`, `soma_total`, `número1`

### Números
- **Inteiros:** `42`, `-17`, `0`
- **Reais:** `3.14`, `-2.5`, `100.0`

### Strings
- Formato: `"texto"`
- Exemplos: `"Olá mundo"`, `"Nome: João"`

### Operadores
- **Aritméticos:** `+`, `-`, `*`, `/`
- **Relacionais:** `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Atribuição:** `=`

### Comentários
- Formato: `# texto até fim da linha`

## 3. Exemplo de Programa
```
algoritmo calculadora_simples
  # Programa básico
  escreva("Digite o primeiro número:")
  numero1 = leia_numero()
  
  escreva("Digite o segundo número:")  
  numero2 = leia_numero()
  
  soma = numero1 + numero2
  escreva("A soma é:", soma)
fim_algoritmo
```