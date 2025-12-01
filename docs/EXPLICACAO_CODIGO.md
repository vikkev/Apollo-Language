# Explicação Breve do Código Apollo Compiler

Este documento resume a estrutura e funcionamento do compilador Apollo.

## Visão Geral
O projeto Apollo Compiler é um compilador educacional para uma linguagem de programação em português, com etapas clássicas de compilação:
- **Análise léxica (lexer):** Converte o texto fonte em tokens (palavras-chave, identificadores, números, operadores, etc).
- **Análise sintática (parser):** Organiza os tokens em uma estrutura de árvore (AST), validando a gramática da linguagem.
- **Análise semântica:** Verifica tipos, escopos e regras de uso, detectando erros lógicos.
- **Geração de código (codegen):** Traduz a AST para LLVM IR, permitindo compilar para executáveis reais.

## Estrutura dos Diretórios
- `apollo_compiler.py`: Script principal que orquestra todas as etapas.
- `lexer/`: Implementação do analisador léxico (AFDs, tokens, interface).
- `parser/`: Implementação do parser (AST, regras de sintaxe, blocos `{}`).
- `semantic/`: Analisador semântico (tipos, escopos, validação).
- `codegen/`: Geração de código LLVM IR, com suporte a tipos básicos.
- `examples/`: Exemplos de código Apollo e LLVM IR gerado.
- `tests/`: Testes unitários e de integração para cada etapa.
- `docs/`: Documentação, manuais e guias.

## Fluxo de Execução
1. **Lexer:** Recebe o código fonte e gera uma lista de tokens.
2. **Parser:** Consome os tokens e constrói a AST.
3. **Semantic Analyzer:** Analisa a AST, verifica tipos e escopos.
4. **Codegen:** Gera LLVM IR a partir da AST e da tabela de símbolos.
5. **Opcional:** LLVM IR pode ser compilado com `clang` para gerar executáveis.

## Principais Arquivos
- `apollo_compiler.py`: Entrada principal, aceita argumentos para fonte, saída e modo verboso.
- `lexer/apollo_lexer.py`: Lexer baseado em AFD, reconhece tokens e operadores compostos.
- `parser/parser.py`: Parser recursivo, suporta blocos `{}` e constrói AST.
- `semantic/semantic_analyzer.py`: Verifica tipos, escopos e regras semânticas.
- `codegen/llvm_generator.py`: Gera LLVM IR, diferenciando operações para inteiros e reais.

## Exemplos
Veja exemplos em `examples/exemplo_simples.apl` e `examples/exemplo_completo.apl` para entender a sintaxe da linguagem.

## Testes
Testes podem ser executados manualmente ou via `pytest` para garantir o funcionamento de cada etapa.

---
Este projeto é ideal para estudos de compiladores, análise de linguagens e geração de código real.