# Manual de Utilização - Compilador Apollo

## Visão Geral

O compilador Apollo converte código-fonte escrito na linguagem Apollo em código LLVM IR, que pode ser compilado para executáveis nativos.

## Sintaxe Básica da Linguagem Apollo

### Estrutura de um Programa

```apl
algoritmo nome_do_programa
    # Declarações de variáveis
    inteiro x, y
    real media
    texto nome
    
    # Comandos
    x = 10
    escreva("Olá, mundo!")
fim_algoritmo
```

### Tipos de Dados

- `inteiro`: Números inteiros (ex: 42, -10, 0)
- `real`: Números reais (ex: 3.14, -2.5, 0.0)
- `texto`: Cadeias de caracteres (ex: "Olá")
- `logico`: Valores booleanos (verdadeiro, falso)

### Declaração de Variáveis

```apl
inteiro idade, ano
real altura, peso
texto nome, sobrenome
logico ativo, concluido
```

### Comandos Básicos

#### Atribuição
```apl
x = 10
y = x + 5
media = (nota1 + nota2) / 2.0
```

#### Escrita (escreva)
```apl
escreva("Digite seu nome:")
escreva("A soma é:", resultado)
```

#### Leitura (leia_numero / leia_texto)
```apl
escreva("Digite um número:")
numero = leia_numero()

escreva("Digite seu nome:")
nome = leia_texto()
```

### Estruturas de Controle

#### Condicional (se)
```apl
se media >= 7.0 faca
    escreva("Aprovado!")
senao
    escreva("Reprovado.")
```

#### Repetição (enquanto)
```apl
enquanto x < 10 faca
    escreva("x =", x)
    x = x + 1
```

### Operadores

#### Aritméticos
- `+` (adição)
- `-` (subtração)
- `*` (multiplicação)
- `/` (divisão)

#### Relacionais
- `==` (igual)
- `!=` (diferente)
- `<` (menor)
- `>` (maior)
- `<=` (menor ou igual)
- `>=` (maior ou igual)

#### Lógicos
- `&&` (e)
- `||` (ou)

## Uso do Compilador

### Sintaxe Básica

```bash
python apollo_compiler.py arquivo.apl
```

### Opções Disponíveis

#### Especificar Arquivo de Saída

```bash
python apollo_compiler.py programa.apl -o programa.ll
```

Isso gera o código LLVM IR no arquivo `programa.ll`.

#### Modo Verboso

```bash
python apollo_compiler.py programa.apl -v
```

Mostra informações detalhadas sobre cada fase da compilação:
- Tokens reconhecidos
- AST criada
- Análise semântica
- Geração de código

### Exemplos Práticos

#### Exemplo 1: Programa Simples

Crie o arquivo `ola.apl`:

```apl
algoritmo ola
    escreva("Olá, mundo!")
fim_algoritmo
```

Compile:

```bash
python apollo_compiler.py ola.apl -o ola.ll
```

#### Exemplo 2: Calculadora Simples

Crie o arquivo `calculadora.apl`:

```apl
algoritmo calculadora
    inteiro numero1, numero2, soma
    
    escreva("Digite o primeiro número:")
    numero1 = leia_numero()
    
    escreva("Digite o segundo número:")
    numero2 = leia_numero()
    
    soma = numero1 + numero2
    escreva("A soma é:", soma)
fim_algoritmo
```

Compile:

```bash
python apollo_compiler.py calculadora.apl -o calculadora.ll -v
```

#### Exemplo 3: Média com Condicional

Crie o arquivo `media.apl`:

```apl
algoritmo media
    real nota1, nota2, media
    
    escreva("Digite a primeira nota:")
    nota1 = leia_numero()
    
    escreva("Digite a segunda nota:")
    nota2 = leia_numero()
    
    media = (nota1 + nota2) / 2.0
    
    se media >= 7.0 faca
        escreva("Aprovado! Média:", media)
    senao
        escreva("Reprovado. Média:", media)
fim_algoritmo
```

Compile:

```bash
python apollo_compiler.py media.apl -o media.ll
```

## Compilando o Código LLVM IR

Após gerar o arquivo `.ll`, você pode compilá-lo para um executável:

```bash
llc -filetype=obj programa.ll -o programa.o
clang programa.o -o programa
```

Ou diretamente:

```bash
clang programa.ll -o programa
```

Execute:

```bash
./programa    # Linux/Mac
programa.exe  # Windows
```

## Mensagens de Erro

### Erros de Sintaxe

```
Erro de parsing: Esperado KEYWORD, encontrado IDENTIFIER na linha 5, coluna 10
```

**Solução**: Verifique a sintaxe do código, especialmente palavras-chave e símbolos.

### Erros Semânticos

```
Erro semântico na linha 8, coluna 15: Variável 'x' não foi declarada
```

**Solução**: Declare todas as variáveis antes de usá-las.

```
Erro semântico na linha 10, coluna 5: Tipo incompatível: esperado inteiro, encontrado texto
```

**Solução**: Verifique os tipos das variáveis nas atribuições.

### Erros de Compilação

```
Erro: Arquivo 'programa.apl' não encontrado
```

**Solução**: Verifique se o arquivo existe e o caminho está correto.

## Dicas e Boas Práticas

1. **Sempre declare variáveis**: Declare todas as variáveis antes de usá-las
2. **Use nomes descritivos**: `idade` é melhor que `x`
3. **Comente seu código**: Use `#` para adicionar comentários
4. **Teste incrementalmente**: Compile e teste pequenas partes do código
5. **Verifique tipos**: Certifique-se de que os tipos são compatíveis

## Exemplos Avançados

### Loop com Contador

```apl
algoritmo contador
    inteiro i
    i = 1
    
    enquanto i <= 10 faca
        escreva("Contador:", i)
        i = i + 1
fim_algoritmo
```

### Calculadora com Múltiplas Operações

```apl
algoritmo calculadora_completa
    inteiro a, b, resultado
    texto operacao
    
    escreva("Digite o primeiro número:")
    a = leia_numero()
    
    escreva("Digite o segundo número:")
    b = leia_numero()
    
    escreva("Digite a operação (+, -, *, /):")
    operacao = leia_texto()
    
    se operacao == "+" faca
        resultado = a + b
        escreva("Resultado:", resultado)
    senao
        escreva("Operação não suportada")
fim_algoritmo
```

## Recursos Adicionais

- Consulte a [Especificação Formal](../especificacao_formal.md) para detalhes técnicos
- Veja mais exemplos na pasta `examples/`
- Leia o [Diário Reflexivo](../diario_reflexivo.md) para entender o desenvolvimento

## Suporte

Para problemas ou dúvidas:
1. Verifique este manual
2. Consulte os exemplos
3. Abra uma issue no GitHub

