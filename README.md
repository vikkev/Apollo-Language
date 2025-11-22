# Apollo Language - Compilador Completo

Linguagem de programação educacional em português com compilador completo.

## 🚀 Uso Rápido

```bash
# Compilar exemplo
python apollo_compiler.py examples/exemplo_simples.apl -o exemplo.ll

# Modo verboso
python apollo_compiler.py examples/exemplo_simples.apl -o exemplo.ll -v

# Testes
python tests/lexer/teste_simples.py
python tests/lexer/teste_completo.py
python tests/lexer/teste_lexer.py
```

## 📁 Estrutura

```
Apollo-Language/
├── apollo_compiler.py      # Compilador principal
├── lexer/                   # Analisador léxico
├── parser/                  # Analisador sintático
├── semantic/                # Analisador semântico
├── codegen/                 # Gerador LLVM IR
├── examples/                # Exemplos
└── docs/                    # Documentação
```

## 💻 Exemplo

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

## 📚 Documentação

- [Manual de Instalação](docs/MANUAL_INSTALACAO.md)
- [Manual de Utilização](docs/MANUAL_UTILIZACAO.md)
- [Gramática Formal](docs/gramatica_apollo.md)

## ✅ Componentes

- ✅ Analisador Léxico (AFDs)
- ✅ Analisador Sintático (AST)
- ✅ Analisador Semântico
- ✅ Gerador de Código LLVM IR

---

**Status**: ✅ Completo e funcional
