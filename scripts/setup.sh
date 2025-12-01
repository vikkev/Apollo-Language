#!/usr/bin/env bash
set -euo pipefail

# Script de setup: cria virtualenv e instala dependências do projeto
# Uso: ./scripts/setup.sh

PYTHON=${PYTHON:-python3}
VENV_DIR=.venv

echo "Usando Python: $($PYTHON --version 2>&1)"

if [ ! -d "$VENV_DIR" ]; then
  echo "Criando virtualenv em $VENV_DIR..."
  $PYTHON -m venv "$VENV_DIR"
fi

echo "Ativando virtualenv..."
# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate"

echo "Instalando dependências..."
pip install --upgrade pip
if [ -f requirements.txt ]; then
  pip install -r requirements.txt
else
  echo "Arquivo requirements.txt não encontrado; nada a instalar.";
fi

echo "Setup concluído. Ative o ambiente com: source $VENV_DIR/bin/activate"
