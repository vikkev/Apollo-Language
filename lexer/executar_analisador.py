from lexer import ApolloLexer, TokenType

arquivo_para_analisar = "exemplo.apl"

print(f"--- Iniciando análise léxica do arquivo: {arquivo_para_analisar} ---")

try:
    with open(arquivo_para_analisar, 'r', encoding='utf-8') as f:
        codigo = f.read()
except FileNotFoundError:
    print(f"ERRO: O arquivo '{arquivo_para_analisar}' não foi encontrado!")
    exit()

lexer = ApolloLexer()

tokens = lexer.tokenize(codigo)

tem_erro = False
for token in tokens:
    if token.type == TokenType.INVALID:
        print(f"\nERRO LÉXICO: Caractere inválido '{token.value}' encontrado na linha {token.line}, coluna {token.column}")
        tem_erro = True
        break

if not tem_erro:
    print("\nAnálise concluída com sucesso! Tabela de Tokens:")
    print("-" * 45)
    print(f"{'Token (Valor)':<30} | {'Tipo'}")
    print("-" * 45)
    for token in tokens:
        if token.type != TokenType.EOF:
            print(f"{token.value:<30} | {token.type.name}")
    print("-" * 45)