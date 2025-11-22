algoritmo exemplo_completo
    # Programa exemplo completo da linguagem Apollo
    inteiro nota1, nota2
    real media
    
    escreva("Digite a primeira nota:")
    nota1 = leia_numero()
    
    escreva("Digite a segunda nota:")
    nota2 = leia_numero()
    
    media = (nota1 + nota2) / 2.0
    
    se media >= 7.0 faca
        escreva("Aprovado! Média:", media)
    senao
        escreva("Reprovado. Média:", media)
    
    # Exemplo de loop
    inteiro contador
    contador = 1
    
    enquanto contador <= 5 faca
        escreva("Contador:", contador)
        contador = contador + 1
fim_algoritmo

