algoritmo calcula_media
    # Este programa calcula a média de duas notas
    inteiro nota1, nota2
    real media

    escreva("Digite a primeira nota:")
    nota1 = leia_numero()

    media = (nota1 + 10) / 2.0

    se media >= 7.0 faca
        escreva("Aprovado!")
    senao
        escreva("Reprovado.")

fim_algoritmo