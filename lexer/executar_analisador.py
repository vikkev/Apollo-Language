from lexer import ApolloLexer, TokenType  # Importa o analisador léxico e tipos de token

arquivo_para_analisar = "exemplo.apl"  # Nome do arquivo de código fonte a ser analisado

print(f"--- Iniciando análise léxica do arquivo: {arquivo_para_analisar} ---")  # Mensagem inicial

try:
    with open(arquivo_para_analisar, 'r', encoding='utf-8') as f:
        codigo = f.read()  # Lê o conteúdo do arquivo
except FileNotFoundError:
    print(f"ERRO: O arquivo '{arquivo_para_analisar}' não foi encontrado!")  # Mensagem de erro se não encontrar o arquivo
    exit()

lexer = ApolloLexer()  # Cria o analisador léxico

tokens = lexer.tokenize(codigo)  # Realiza a análise léxica e obtém os tokens

tem_erro = False  # Flag para indicar se houve erro léxico
for token in tokens:
    if token.type == TokenType.INVALID:
        # Se encontrar token inválido, exibe erro e interrompe
        print(f"\nERRO LÉXICO: Caractere inválido '{token.value}' encontrado na linha {token.line}, coluna {token.column}")
        tem_erro = True
        break

if not tem_erro:
    # Se não houve erro, exibe tabela de tokens reconhecidos
    print("\nAnálise concluída com sucesso! Tabela de Tokens:")
    print("-" * 45)
    print(f"{'Token (Valor)':<30} | {'Tipo'}")
    print("-" * 45)
    for token in tokens:
        if token.type != TokenType.EOF:
            print(f"{token.value:<30} | {token.type.name}")
    print("-" * 45)