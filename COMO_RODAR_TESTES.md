# 🧪 Como Rodar os Testes

## Testes Disponíveis

### 1. Teste Simples
```bash
python tests/lexer/teste_simples.py
```
**O que testa:**
- Reconhecimento básico de tokens
- Operadores (==, !=, <=, >=)
- Identificadores, números, strings
- Princípio do match mais longo

### 2. Teste Completo
```bash
python tests/lexer/teste_completo.py
```
**O que testa:**
- Todos os tipos de tokens
- Casos especiais e edge cases
- Código completo

### 3. Teste do Lexer
```bash
python tests/lexer/teste_lexer.py
```
**O que testa:**
- Funcionalidades completas do lexer
- Análise de código-fonte completo

## Rodar Todos os Testes

```bash
# Windows PowerShell
python tests/lexer/teste_simples.py
python tests/lexer/teste_completo.py
python tests/lexer/teste_lexer.py

# Linux/Mac
python tests/lexer/teste_simples.py && python tests/lexer/teste_completo.py && python tests/lexer/teste_lexer.py
```

## Resultado Esperado

Todos os testes devem mostrar:
```
============================================================
TODOS OS TESTES CONCLUÍDOS COM SUCESSO!
============================================================
```

## Verificar se Funciona

Execute o teste simples primeiro:
```bash
python tests/lexer/teste_simples.py
```

Se aparecer "TODOS OS TESTES CONCLUÍDOS COM SUCESSO!", está tudo funcionando! ✅

