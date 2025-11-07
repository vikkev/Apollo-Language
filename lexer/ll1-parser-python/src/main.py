# main.py

def main():
    from lexer import Lexer
    from parser import Parser

    # Recebe a entrada do usuário
    expression = input("Digite uma expressão matemática: ")

    # Cria o analisador léxico
    lexer = Lexer(expression)
    tokens = lexer.tokenize()

    # Cria o parser
    parser = Parser(tokens)

    # Realiza o parsing e exibe os resultados
    if parser.parse():
        print("Expressão reconhecida com sucesso!")
        print("Árvore sintática:", parser.get_syntax_tree())
    else:
        print("Erro ao reconhecer a expressão.")

if __name__ == "__main__":
    main()