# Documentação do Código - Linguagem Apollo
## Formato para Apresentação

---

## Visão Geral

**O que é?**
- Analisador léxico (lexer) que converte código-fonte em tokens
- Primeira fase de um compilador
- Implementado em Python

**Objetivo:**
- Reconhecer palavras-chave, identificadores, números, strings, operadores
- Ignorar espaços e comentários
- Reportar erros léxicos

---

## Arquitetura

### Estrutura Principal
```
lexer/
├── apollo_lexer.py      (Implementação principal)
├── executar_analisador.py
└── teste_*.py          (Scripts de teste)
```

---

## Componentes Principais

### 1. TokenType (Enum)
**Tipos de tokens:**
- `IDENTIFIER`, `KEYWORD`, `INTEGER`, `REAL`, `STRING`
- `BOOLEAN`, `OPERATOR`, `SYMBOL`, `EOF`, `INVALID`

### 2. Token (Dataclass)
**Informações armazenadas:**
- Tipo do token
- Valor literal
- Linha e coluna (posição)
- Comprimento

### 3. AFD (Autômato)
**Função:**
- Reconhece padrões de tokens
- Um AFD por tipo de token
- Simula autômato no texto

### 4. ApolloLexer (Classe Principal)
**Responsabilidades:**
- Cria AFDs para cada tipo
- Aplica princípio do match mais longo
- Tokeniza código-fonte completo

---

## Funcionamento

### Fluxo de Execução

**1. Inicialização**
```python
lexer = ApolloLexer()
```
- Cria AFDs
- Configura palavras-chave e operadores

**2. Tokenização**
```python
tokens = lexer.tokenize(codigo)
```
- Percorre código caractere por caractere
- Aplica match mais longo
- Retorna lista de tokens

**3. Resultado**
- Cada token com tipo, valor e posição
- Tokens inválidos marcados

---

## Princípios de Design

### 1. Match Mais Longo
- Resolve ambiguidades
- Exemplo: `x==10` → `==` (não `=` + `=`)

### 2. Modularidade
- Um AFD por tipo de token
- Fácil manutenção e extensão

### 3. Tokens Ricos
- Informações completas de contexto
- Facilita debugging

### 4. Buffer Circular
- Performance otimizada
- Suporta arquivos grandes

---

## Tipos de Tokens

| Tipo | Exemplos |
|------|----------|
| **Identificadores** | `variavel`, `nome123` |
| **Palavras-chave** | `algoritmo`, `se`, `enquanto` |
| **Inteiros** | `42`, `-17`, `+25` |
| **Reais** | `3.14`, `-2.5` |
| **Strings** | `"Olá mundo"` |
| **Operadores** | `+`, `-`, `==`, `<=` |
| **Símbolos** | `(`, `)`, `{`, `}`, `:`, `,` |
| **Booleanos** | `verdadeiro`, `falso` |
| **Comentários** | `# comentário` |

---

## Exemplo de Uso

```python
from lexer.apollo_lexer import ApolloLexer

codigo = """
algoritmo exemplo
    inteiro x = 42
    escreva("Olá")
fim_algoritmo
"""

lexer = ApolloLexer()
tokens = lexer.tokenize(codigo)

for token in tokens:
    print(f"{token.type.name}: '{token.value}'")
```

**Saída:**
```
KEYWORD: 'algoritmo'
IDENTIFIER: 'exemplo'
KEYWORD: 'inteiro'
IDENTIFIER: 'x'
OPERATOR: '='
INTEGER: '42'
KEYWORD: 'escreva'
SYMBOL: '('
STRING: '"Olá"'
...
```

---

## Métodos Principais

### `tokenize(source_code)`
- Método principal
- Retorna lista de tokens

### `_longest_match(text, start_pos)`
- Implementa match mais longo
- Testa todos os AFDs
- Retorna melhor match

### `_create_afds()`
- Cria AFDs para:
  - Identificadores
  - Números (inteiros e reais)
  - Strings
  - Comentários

---

## Integração com Parser

**Interface fornecida:**
```python
interface = LexerInterface(lexer)
token = interface.next_token()    # Próximo token
token = interface.peek_token(0)  # Visualiza sem consumir
```

**Benefícios:**
- Desacoplamento lexer/parser
- Flexibilidade para lookahead
- Facilita testes

---

## Dependências

- Python 3.7+
- Bibliotecas padrão:
  - `enum`, `typing`, `dataclasses`, `collections`

---

## Extensibilidade

**Como adicionar:**
1. **Novo tipo de token**: Adicione ao `TokenType` e crie AFD
2. **Nova palavra-chave**: Adicione ao conjunto `keywords`
3. **Novo operador**: Adicione ao conjunto `operators`
4. **Novo símbolo**: Adicione ao conjunto `symbols`

---

## Características Especiais

- **Simulação dinâmica** para strings e comentários
- **Operadores testados** do maior para menor comprimento
- **Espaços preservados** como tokens (opcional)
- **Erros não interrompem** a análise

---

## Resumo

| Aspecto | Descrição |
|--------|-----------|
| **Linguagem** | Python 3.7+ |
| **Arquivo principal** | `apollo_lexer.py` |
| **Classes principais** | `ApolloLexer`, `Token`, `AFD` |
| **Princípio chave** | Match mais longo |
| **Arquitetura** | Modular (um AFD por tipo) |
