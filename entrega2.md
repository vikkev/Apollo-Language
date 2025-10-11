# Apollo - Especificação Léxica com Expressões Regulares

## Tokens e Expressões Regulares

### Palavras-chave
```
algoritmo|fim_algoritmo|se|senao|enquanto|para|faca|inteiro|real|texto|logico|verdadeiro|falso|escreva|leia_numero|leia_texto
```
# Reconhece todas as palavras reservadas da linguagem

### Identificadores
```
[a-zA-ZÀ-ÿ_][a-zA-ZÀ-ÿ0-9_]*
```
# Identificadores: começam por letra ou _, podem conter letras, dígitos e acentos

### Números
```
[+-]?[0-9]+(\.[0-9]+)?
```
# Reconhece inteiros e reais, com sinal opcional

### Strings
```
"([^"\\]|\\.)*"
```
# Cadeias de caracteres entre aspas, permite escape

### Operadores
```
==|!=|<=|>=|[<>=+\-*/]
```
# Reconhece operadores aritméticos e relacionais

### Delimitadores
```
[(),:] 
```
# Símbolos de pontuação usados na linguagem

### Comentários
```
#.*$
```
# Ignora tudo após '#' até o fim da linha

### Espaços
```
[ \t\r\n]+
```
# Ignora espaços, tabulações e quebras de linha

## Resolução de Ambiguidades

### Identificadores vs Palavras-chave
- Primeiro verifica se o token é palavra-chave
- Se não for, trata como identificador
- Comparação sem diferenciar maiúsculas/minúsculas

### Números
- Inteiros: só dígitos
- Reais: exige dígitos após o ponto
- Exemplo: `42.` sem dígitos após o ponto é erro

### Operadores de dois caracteres
# Verifica primeiro operadores de dois caracteres
Ordem de verificação:
1. `<=`, `>=`, `==`, `!=` 
2. `<`, `>`, `=`

## Tratamento de Erros

### Caracteres inválidos
```
Erro: Caractere '%' não reconhecido na linha 5, coluna 12
Sugestão: Verifique se você quis usar um operador válido
```
# Mensagem de erro para símbolos não reconhecidos

### String não fechada
```
Erro: String iniciada na linha 8 não foi fechada
Sugestão: Adicione " no final da string
```
# Mensagem de erro para strings sem aspas finais

### Número mal formado
```
Erro: Número "42." incompleto na linha 3
Sugestão: Complete com dígitos após o ponto ou remova o ponto
```
# Mensagem de erro para números reais incompletos

### Identificador inválido
```
Erro: Identificador "2nome" inválido na linha 6
Sugestão: Identificadores não podem começar com número
```
# Mensagem de erro para identificadores mal formados

## Mensagens de Erro Educativas
# Mensagens de erro são claras, educativas e amigáveis
# Sempre informam local, descrição e sugestão de correção
# Exemplos:
- "Opa! Parece que você esqueceu de fechar uma string"
- "Este nome de variável não é válido. Que tal começar com uma letra?"
- "Não reconheço este símbolo. Você quis dizer '==' para comparar?"

## Considerações de Implementação

### Performance
# Expressões regulares e ordem de verificação pensadas para rapidez
# Palavras-chave são verificadas com cache

### Internacionalização  
# Suporte total a acentos e caracteres do português
# Encoding padrão é UTF-8
# Identificadores aceitam letras acentuadas

### Precedência dos Tokens
# Ordem de prioridade para reconhecimento dos tokens:
1. Comentários (ignorados)
2. Palavras-chave  
3. Números
4. Strings
5. Operadores (dois chars primeiro)
6. Identificadores
7. Delimitadores
8. Espaços (ignorados)