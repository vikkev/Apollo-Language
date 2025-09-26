
# Analisador Léxico - Linguagem Apollo

Este diretório contém o analisador léxico (lexer) para a linguagem de programação educacional Apollo.

## Descrição

O analisador léxico é a primeira fase de um compilador. Ele lê o código-fonte como uma sequência de caracteres e o converte em uma sequência de tokens (as "palavras" da linguagem, como palavras-chave, identificadores, números, etc.).

Este lexer foi implementado em Python e é capaz de:
- Reconhecer todas as palavras-chave, identificadores, números (inteiros e reais), strings, operadores e símbolos da linguagem Apollo.
- Ignorar espaços em branco e comentários.
- Identificar e reportar tokens inválidos, indicando a linha e a coluna onde o erro ocorreu.

## Como Executar

Para executar o analisador, você precisará ter o Python 3 instalado.

### Passos

1. **Salve o Código:**
   - Salve o código do analisador em um arquivo chamado `lexer.py`.
   - Crie um arquivo com código na linguagem Apollo e salve-o, por exemplo, como `exemplo.apl`.

2. **Crie um Script de Execução:**
   - Para facilitar, crie um arquivo chamado `main.py` para ler o código-fonte e executar o lexer.

   ```python
   from lexer import ApolloLexer, TokenType

   def main():
       filename = "exemplo.apl" 

       try:
           with open(filename, 'r', encoding='utf-8') as f:
               code = f.read()
       except FileNotFoundError:
           print(f"Erro: Arquivo '{filename}' não encontrado.")
           return

       lexer = ApolloLexer()
       tokens = lexer.tokenize(code)

       has_error = False
       for token in tokens:
           if token.type == TokenType.INVALID:
               print(f"Erro: Token não reconhecido '{token.value}' na linha {token.line}, coluna {token.column}")
               has_error = True
               break
       
       if not has_error:
           print(f"{'Token':<30} | {'Tipo'}")
           print("-" * 45)
           for token in tokens:
               if token.type != TokenType.EOF:
                   print(f"{token.value:<30} | {token.type.name}")

   if __name__ == "__main__":
       main()
   ```

3. **Execute via Terminal:**
   - Abra um terminal na pasta onde você salvou os arquivos.
   - Execute o script principal com o seguinte comando:
     ```bash
     python main.py
     ```

4. **Saída:**
   - Se o código em `exemplo.apl` for válido, o programa imprimirá uma tabela formatada com cada token e seu respectivo tipo.
   - Se um token inválido for encontrado, o programa imprimirá uma mensagem de erro clara, apontando a localização exata do problema, e interromperá a análise. 