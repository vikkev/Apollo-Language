# Compilador Apollo - Documentação Completa

## Visão Geral

O Compilador Apollo é um compilador completo para a linguagem de programação educacional Apollo, desenvolvido em Python. Ele realiza todas as fases de compilação: análise léxica, análise sintática, análise semântica e geração de código LLVM IR.

## Estrutura do Projeto

```
Apollo-Language/
├── apollo_compiler.py      # Compilador principal (ponto de entrada)
├── lexer/                   # Analisador léxico
│   ├── apollo_lexer.py      # Implementação do lexer
│   └── ...
├── parser/                  # Analisador sintático
│   ├── parser.py            # Parser recursivo descendente
│   └── ast.py               # Definição da AST
├── semantic/                # Analisador semântico
│   └── semantic_analyzer.py # Verificação semântica
├── codegen/                 # Gerador de código
│   └── llvm_generator.py    # Geração de LLVM IR
├── examples/                # Exemplos de código Apollo
│   ├── exemplo_simples.apl
│   └── exemplo_completo.apl
└── docs/                    # Documentação
    ├── MANUAL_INSTALACAO.md
    └── MANUAL_UTILIZACAO.md
```

## Componentes Implementados

### 1. Analisador Léxico (Lexer)
- **Arquivo**: `lexer/apollo_lexer.py`
- **Funcionalidades**:
  - Reconhecimento de tokens usando AFDs
  - Princípio do match mais longo
  - Suporte a identificadores, números, strings, operadores
  - Tratamento de comentários e espaços em branco

### 2. Analisador Sintático (Parser)
- **Arquivo**: `parser/parser.py`
- **Funcionalidades**:
  - Parser recursivo descendente
  - Criação da AST (Abstract Syntax Tree)
  - Suporte a declarações, comandos e expressões
  - Tratamento de estruturas de controle (se, enquanto)

### 3. Analisador Semântico
- **Arquivo**: `semantic/semantic_analyzer.py`
- **Funcionalidades**:
  - Verificação de tipos
  - Tabela de símbolos com escopos
  - Verificação de variáveis não declaradas
  - Compatibilidade de tipos em atribuições

### 4. Gerador de Código LLVM IR
- **Arquivo**: `codegen/llvm_generator.py`
- **Funcionalidades**:
  - Geração de código LLVM IR a partir da AST
  - Suporte a operações aritméticas e lógicas
  - Geração de código para estruturas de controle
  - Integração com funções padrão (printf, scanf)

## Uso Rápido

### Compilar um programa

```bash
python apollo_compiler.py programa.apl -o programa.ll
```

### Modo verboso

```bash
python apollo_compiler.py programa.apl -o programa.ll -v
```

### Compilar e executar

```bash
# Gerar LLVM IR
python apollo_compiler.py programa.apl -o programa.ll

# Compilar LLVM IR para executável
clang programa.ll -o programa

# Executar
./programa    # Linux/Mac
programa.exe  # Windows
```

## Exemplo de Código Apollo

```apl
algoritmo exemplo
    inteiro x, y, soma
    
    escreva("Digite o primeiro número:")
    x = leia_numero()
    
    escreva("Digite o segundo número:")
    y = leia_numero()
    
    soma = x + y
    escreva("A soma é:", soma)
fim_algoritmo
```

## Requisitos

- Python 3.7 ou superior
- LLVM (opcional, para compilar o código LLVM IR gerado)

## Documentação Completa

- [Manual de Instalação](docs/MANUAL_INSTALACAO.md) - Guia passo a passo para instalação
- [Manual de Utilização](docs/MANUAL_UTILIZACAO.md) - Como usar o compilador e a linguagem
- [Especificação Formal](especificacao_formal.md) - Definição matemática da linguagem
- [Diário Reflexivo](diario_reflexivo.md) - Processo de desenvolvimento

## Status do Projeto

✅ **Analisador Léxico** - Implementado e testado
✅ **Analisador Sintático** - Implementado e testado
✅ **Analisador Semântico** - Implementado e testado
✅ **Gerador de Código LLVM IR** - Implementado e testado
✅ **Manuais de Instalação e Utilização** - Completos

## Contribuindo

Este é um projeto acadêmico desenvolvido como trabalho de compiladores. Para contribuições, abra uma issue no repositório.

## Licença

Este projeto é desenvolvido para fins educacionais.

