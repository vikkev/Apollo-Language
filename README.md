# EduScript - Especificação Léxica

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