# Como executar um programa Apollo (versão simplificada)

Este guia mostra, passo a passo, como transformar um arquivo `.apl` em um executável e rodá-lo.

## Pré-requisitos
- Python 3.7+ (recomendado `python3`)
- Opcional: LLVM/Clang para transformar o LLVM IR em executável

## 1) Preparar o ambiente

Linux / macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt    # opcional, para rodar testes
```

Windows (PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Observação: você também pode executar `./scripts/setup.sh` que cria o `.venv` e instala dependências.

## 2) Gerar o arquivo LLVM IR a partir do código Apollo

```bash
python3 apollo_compiler.py examples/exemplo_simples.apl -o exemplo_simples.ll
```

Isso cria `exemplo_simples.ll` (LLVM IR).

## 3) (Opcional) Gerar executável a partir do `.ll` — requer Clang

Verifique se o `clang` está disponível:

```bash
clang --version
```

Se estiver instalado, gere o executável:

Linux / macOS:
```bash
clang exemplo_simples.ll -o exemplo_simples
```

Windows (PowerShell / cmd):
```powershell
clang exemplo_simples.ll -o exemplo_simples.exe
```

Alternativa em 2 passos (usar `llc`):

```bash
llc -filetype=obj exemplo_simples.ll -o exemplo_simples.o
clang exemplo_simples.o -o exemplo_simples
```

## 4) Executar o programa gerado

Linux / macOS:
```bash
./exemplo_simples
```

Windows:
```powershell
.\exemplo_simples.exe
```

O programa pedirá entradas, por exemplo:

```
Digite o primeiro número:
Digite o segundo número:
A soma é: 42
```

## 5) Ver o LLVM IR (se não quiser compilar)

Linux / macOS:
```bash
cat exemplo_simples.ll | less
```

Windows (PowerShell):
```powershell
Get-Content exemplo_simples.ll
```

## 6) Rodar os testes/ exemplos de inspeção

Scripts demonstrativos (executam exemplos do lexer/parser):
```bash
python3 tests/lexer/teste_simples.py
python3 tests/lexer/teste_completo.py
python3 tests/lexer/teste_lexer.py
```

Se você instalou `pytest` no `.venv`, pode rodar:

```bash
.venv/bin/pytest -q
```

## Solução de problemas rápida
- `Erro: Arquivo 'programa.apl' não encontrado`: verifique o caminho do arquivo.
- `clang: command not found`: instale LLVM/Clang (ex.: `sudo apt install clang` no Ubuntu, Homebrew no macOS).
- Permissão negada ao executar: rode `chmod +x exemplo_simples` no Linux/macOS.

## Observações finais
- O compilador Apollo gera LLVM IR. Para executar, é necessário converter esse IR em um executável com ferramentas como `clang`.
- Use `-v` no `apollo_compiler.py` para ver detalhes da compilação (tokens, AST, análise semântica).

Se quiser, consulte também o README ou outros manuais em `docs/` para mais detalhes.