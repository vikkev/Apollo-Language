# 📝 Como Compilar os Exemplos

## 🚀 Compilação Rápida

### Exemplo Simples

```bash
python apollo_compiler.py examples/exemplo_simples.apl -o examples/exemplo_simples.ll
```

### Exemplo Completo

```bash
python apollo_compiler.py examples/exemplo_completo.apl -o examples/exemplo_completo.ll
```

## 📋 Passo a Passo Detalhado

### 1️⃣ Compilar exemplo_simples.apl

```bash
# Compilar
python apollo_compiler.py examples/exemplo_simples.apl -o exemplo_simples.ll

# Ver resultado
type exemplo_simples.ll
```

**O que faz:**
- Lê três números do usuário
- Calcula a soma
- Mostra o resultado

### 2️⃣ Compilar exemplo_completo.apl

```bash
# Compilar
python apollo_compiler.py examples/exemplo_completo.apl -o exemplo_completo.ll

# Ver resultado
type exemplo_completo.ll
```

**O que faz:**
- Lê duas notas
- Calcula a média
- Verifica aprovação
- Faz um loop contando de 1 até 5

## 🔍 Modo Verboso (Ver Todas as Fases)

Para ver detalhes de cada fase da compilação:

```bash
# Exemplo simples com detalhes
python apollo_compiler.py examples/exemplo_simples.apl -o exemplo_simples.ll -v

# Exemplo completo com detalhes
python apollo_compiler.py examples/exemplo_completo.apl -o exemplo_completo.ll -v
```

**Saída esperada:**
```
=== Análise Léxica ===
Tokens reconhecidos: 61
  KEYWORD: 'algoritmo'
  ...

=== Análise Sintática ===
AST criada: Program(declarations=3, statements=6)

=== Análise Semântica ===
Análise semântica concluída sem erros

=== Geração de Código LLVM IR ===
Código LLVM IR gerado em: exemplo_simples.ll
```

## ✅ Verificar Compilação

Após compilar, você deve ver:
```
Código LLVM IR gerado em: exemplo_simples.ll
```

E os arquivos `.ll` devem ser criados na pasta `examples/` ou na raiz.

## 📁 Onde Ficam os Arquivos

- **Código Apollo**: `examples/exemplo_simples.apl` e `examples/exemplo_completo.apl`
- **Código LLVM IR gerado**: `exemplo_simples.ll` e `exemplo_completo.ll` (na raiz ou onde você especificar)

## 🎯 Comandos Completos

### Compilar Ambos os Exemplos

```bash
# Compilar exemplo simples
python apollo_compiler.py examples/exemplo_simples.apl -o exemplo_simples.ll

# Compilar exemplo completo
python apollo_compiler.py examples/exemplo_completo.apl -o exemplo_completo.ll

# Verificar arquivos gerados
dir *.ll
```

### Compilar com Detalhes

```bash
# Exemplo simples
python apollo_compiler.py examples/exemplo_simples.apl -o exemplo_simples.ll -v

# Exemplo completo
python apollo_compiler.py examples/exemplo_completo.apl -o exemplo_completo.ll -v
```

## 💡 Dicas

- Use `-v` para ver todas as fases da compilação
- Os arquivos `.ll` gerados são código LLVM IR válido
- Você pode abrir os arquivos `.ll` em qualquer editor de texto para ver o código gerado

## 🐛 Solução de Problemas

### Erro: "Arquivo não encontrado"
- Certifique-se de estar na pasta raiz do projeto
- Use o caminho correto: `examples/exemplo_simples.apl`

### Erro: "Módulo não encontrado"
- Verifique se está na pasta correta
- Execute: `python apollo_compiler.py --help` para testar

---

**Pronto! Agora você sabe como compilar os exemplos! 🎉**

