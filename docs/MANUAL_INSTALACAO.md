# Manual de Instalação - Compilador Apollo

## Requisitos do Sistema

### Windows
- Python 3.7 ou superior
- LLVM (opcional, para compilar o código LLVM IR gerado)

### Linux/Mac
- Python 3.7 ou superior
- LLVM (opcional, para compilar o código LLVM IR gerado)

## Instalação Passo a Passo

### 1. Verificar Python

Abra o terminal (PowerShell no Windows, Terminal no Linux/Mac) e execute:

```bash
python --version
```

ou

```bash
python3 --version
```

Você deve ver algo como `Python 3.7.x` ou superior. Se não tiver Python instalado:

- **Windows**: Baixe em [python.org](https://www.python.org/downloads/)
- **Linux**: `sudo apt-get install python3` (Ubuntu/Debian) ou `sudo yum install python3` (CentOS/RHEL)
- **Mac**: `brew install python3` ou baixe em [python.org](https://www.python.org/downloads/)

### 2. Baixar o Projeto

#### Opção A: Clonar do GitHub
```bash
git clone https://github.com/seu-usuario/Apollo-Language.git
cd Apollo-Language
```

#### Opção B: Baixar ZIP
1. Acesse o repositório no GitHub
2. Clique em "Code" → "Download ZIP"
3. Extraia o arquivo ZIP
4. Abra o terminal na pasta extraída

### 3. Verificar Estrutura do Projeto

O projeto deve ter a seguinte estrutura:

```
Apollo-Language/
├── apollo_compiler.py      # Compilador principal
├── lexer/                   # Analisador léxico
│   └── apollo_lexer.py
├── parser/                  # Analisador sintático
│   ├── parser.py
│   └── ast.py
├── semantic/                # Analisador semântico
│   └── semantic_analyzer.py
├── codegen/                 # Gerador de código
│   └── llvm_generator.py
├── examples/                # Exemplos de código
└── docs/                    # Documentação
```

### 4. Testar Instalação

Execute o seguinte comando para verificar se tudo está funcionando:

```bash
python apollo_compiler.py --help
```

ou

```bash
python3 apollo_compiler.py --help
```

Você deve ver a mensagem de ajuda do compilador.

### 5. Instalar LLVM (Opcional - NÃO Obrigatório)

**⚠️ IMPORTANTE**: LLVM/Clang é **OPCIONAL**. O compilador Apollo funciona perfeitamente sem ele!

Você só precisa do LLVM se quiser compilar o código LLVM IR gerado em um executável para testar rodando o programa:

#### Windows
1. Baixe o instalador em [llvm.org](https://llvm.org/builds/)
2. Execute o instalador
3. Adicione LLVM ao PATH do sistema

#### Linux
```bash
sudo apt-get install llvm clang
```

#### Mac
```bash
brew install llvm
```

## Verificação Final

Crie um arquivo de teste `teste.apl`:

```apl
algoritmo teste
    inteiro x
    x = 10
    escreva("Olá, Apollo!")
fim_algoritmo
```

Compile o arquivo:

```bash
python apollo_compiler.py teste.apl -o teste.ll
```

Se tudo estiver correto, você verá:
- Uma mensagem de sucesso
- Um arquivo `teste.ll` com código LLVM IR

## Solução de Problemas

### Erro: "python não é reconhecido"
- **Windows**: Use `py` em vez de `python`, ou adicione Python ao PATH
- **Linux/Mac**: Use `python3` em vez de `python`

### Erro: "Módulo não encontrado"
- Certifique-se de estar na pasta raiz do projeto
- Verifique se todos os arquivos estão presentes

### Erro: "Permissão negada"
- **Linux/Mac**: Use `chmod +x apollo_compiler.py` para dar permissão de execução

## Próximos Passos

Após a instalação bem-sucedida, consulte o [Manual de Utilização](MANUAL_UTILIZACAO.md) para aprender a usar o compilador.

