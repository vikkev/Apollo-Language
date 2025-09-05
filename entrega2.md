# Apollo - Especificação Léxica com Expressões Regulares

## Tokens e Expressões Regulares

### Palavras-chave
```
algoritmo|fim_algoritmo|se|senao|enquanto|para|faca|inteiro|real|texto|logico|verdadeiro|falso|escreva|leia_numero|leia_texto
```

### Identificadores
```
[a-zA-ZÀ-ÿ_][a-zA-ZÀ-ÿ0-9_]*
```

### Números
```
[+-]?[0-9]+(\.[0-9]+)?
```

### Strings
```
"([^"\\]|\\.)*"
```

### Operadores
```
==|!=|<=|>=|[<>=+\-*/]
```

### Delimitadores
```
[(),:] 
```

### Comentários
```
#.*$
```

### Espaços
```
[ \t\r\n]+
```

## Resolução de Ambiguidades

### Identificadores vs Palavras-chave
- Primeira verificação: se o token está na lista de palavras-chave
- Caso contrário: trata como identificador
- Comparação case-insensitive

### Números
- Inteiros: apenas dígitos
- Reais: obrigatório ter dígitos após o ponto
- `42.` sem dígitos = erro

### Operadores de dois caracteres
Ordem de verificação:
1. `<=`, `>=`, `==`, `!=` 
2. `<`, `>`, `=`

## Tratamento de Erros

### Caracteres inválidos
```
Erro: Caractere '%' não reconhecido na linha 5, coluna 12
Sugestão: Verifique se você quis usar um operador válido
```

### String não fechada
```
Erro: String iniciada na linha 8 não foi fechada
Sugestão: Adicione " no final da string
```

### Número mal formado
```
Erro: Número "42." incompleto na linha 3
Sugestão: Complete com dígitos após o ponto ou remova o ponto
```

### Identificador inválido
```
Erro: Identificador "2nome" inválido na linha 6
Sugestão: Identificadores não podem começar com número
```

## Mensagens de Erro Educativas

As mensagens seguem o padrão:
- **Local do erro**: linha e coluna específicas
- **Descrição clara**: o que foi encontrado de errado
- **Sugestão**: como corrigir o problema
- **Tom amigável**: linguagem que não intimida iniciantes

Exemplos de mensagens em português:
- "Opa! Parece que você esqueceu de fechar uma string"
- "Este nome de variável não é válido. Que tal começar com uma letra?"
- "Não reconheço este símbolo. Você quis dizer '==' para comparar?"

## Considerações de Implementação

### Performance
- Expressões regulares otimizadas para velocidade
- Ordem de verificação baseada na frequência de uso
- Cache para palavras-chave já verificadas

### Internacionalização  
- Suporte completo a caracteres acentuados portugueses
- Encoding UTF-8 como padrão
- Identificadores podem usar ç, á, ã, etc.

### Precedência dos Tokens
1. Comentários (ignorados)
2. Palavras-chave  
3. Números
4. Strings
5. Operadores (dois chars primeiro)
6. Identificadores
7. Delimitadores
8. Espaços (ignorados)