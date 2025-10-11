algoritmo calcula_media
    # Este programa calcula a média de duas notas
    inteiro nota1, nota2  # Declaração de variáveis inteiras
    real media            # Declaração de variável real

    escreva("Digite a primeira nota:")  # Solicita ao usuário a primeira nota
    nota1 = leia_numero()                # Lê a primeira nota do usuário

    media = (nota1 + 10) / 2.0           # Calcula a média das notas

    se media >= 7.0 faca                 # Verifica se a média é suficiente para aprovação
        escreva("Aprovado!")            # Mensagem de aprovação
    senao
        escreva("Reprovado.")           # Mensagem de reprovação

fim_algoritmo  # Fim do programa