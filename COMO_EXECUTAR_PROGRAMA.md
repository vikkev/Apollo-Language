# 🚀 Como Executar um Programa Apollo

## ⚠️ Importante

O compilador Apollo **gera código LLVM IR**, mas **não executa** o programa. Para ver o programa rodando e digitar os números, você precisa compilar o LLVM IR para um executável.

## 📋 Passo a Passo Completo

### 1️⃣ Compilar Apollo para LLVM IR

```bash
python apollo_compiler.py examples/exemplo_simples.apl -o exemplo_simples.ll
```

**Resultado:** Gera o arquivo `exemplo_simples.ll` (código LLVM IR)

### 2️⃣ Compilar LLVM IR para Executável

**Requisito:** Ter LLVM/Clang instalado

```bash
# Windows
clang exemplo_simples.ll -o exemplo_simples.exe

# Linux/Mac
clang exemplo_simples.ll -o exemplo_simples
```

### 3️⃣ Executar o Programa

```bash
# Windows
exemplo_simples.exe

# Linux/Mac
./exemplo_simples
```

**Agora sim você verá:**
```
Digite o primeiro número:
```
E poderá digitar os números!

## 🔍 Por que não aparece direto?

O compilador Apollo faz apenas a **tradução** do código Apollo para LLVM IR. É como traduzir um texto - você traduz, mas não executa.

Para executar, precisa:
1. ✅ Compilar Apollo → LLVM IR (já feito)
2. ⏭️ Compilar LLVM IR → Executável (precisa do Clang)
3. ⏭️ Executar o executável (aí aparece a interação)

## 🎯 Exemplo Completo

```bash
# 1. Gerar LLVM IR
python apollo_compiler.py examples/exemplo_simples.apl -o exemplo_simples.ll

# 2. Compilar para executável (se tiver Clang)
clang exemplo_simples.ll -o exemplo_simples.exe

# 3. Executar
exemplo_simples.exe
```

**Agora você verá:**
```
Digite o primeiro número: [você digita aqui]
Digite o segundo número: [você digita aqui]
A soma é: [resultado]
```

## 💡 Alternativa: Ver o Código LLVM IR

Se você não tiver Clang instalado, pode apenas ver o código gerado:

```bash
# Ver o código LLVM IR gerado
type exemplo_simples.ll
```

O código LLVM IR já é válido e mostra que o compilador está funcionando corretamente!

## ✅ Resumo

- **Compilador Apollo**: Gera código LLVM IR ✅ (já funcionando)
- **Clang**: Compila LLVM IR para executável (opcional)
- **Executável**: Roda o programa e pede entrada (opcional)

O importante é que o compilador está gerando código LLVM IR válido! 🎉

