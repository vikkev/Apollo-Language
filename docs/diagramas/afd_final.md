# Diagrama Mermaid do AFD Final

```mermaid
graph TD
    %% Diagrama do AFD final gerado para tokens da linguagem Apollo
    S0[Início] -->|letra| S1  %% Identificador: começa com letra
    S1 -->|letra/dígito/_| S1  %% Identificador: continua com letra, dígito ou _
    S1 -->| | SF_ID  %% Estado final para identificador

    S0 -->|+/-| S2  %% Número: pode começar com sinal
    S0 -->|dígito| S3  %% Número: pode começar com dígito
    S2 -->|dígito| S3
    S3 -->|dígito| S3  %% Número inteiro: sequência de dígitos
    S3 -->|.| S4  %% Número real: ponto decimal
    S4 -->|dígito| S5  %% Número real: parte fracionária
    S5 -->|dígito| S5
    S3 -->| | SF_INT  %% Estado final para inteiro
    S5 -->| | SF_REAL  %% Estado final para real

    S0 -->|"| S6  %% String: abre aspas
    S6 -->|char| S6  %% String: qualquer caractere
    S6 -->|"| S7  %% String: fecha aspas
    S7 -->| | SF_STR  %% Estado final para string

    S0 -->|#| S8  %% Comentário: inicia com #
    S8 -->|char| S8  %% Comentário: qualquer caractere até fim da linha
    S8 -->|\n| S9  %% Comentário: termina com quebra de linha
    S9 -->| | SF_COM  %% Estado final para comentário

    S0 -->|==| SF_OP  %% Operador igual
    S0 -->|!=| SF_OP  %% Operador diferente
    S0 -->|<=| SF_OP  %% Operador menor ou igual
    S0 -->|>=| SF_OP  %% Operador maior ou igual
    S0 -->|<| SF_OP   %% Operador menor
    S0 -->|>| SF_OP   %% Operador maior
    S0 -->|=| SF_OP   %% Operador atribuição
    S0 -->|+| SF_OP   %% Operador soma
    S0 -->|-| SF_OP   %% Operador subtração
    S0 -->|*| SF_OP   %% Operador multiplicação
    S0 -->|/| SF_OP   %% Operador divisão

    S0 -->|(| SF_SYM  %% Símbolo: abre parêntese
    S0 -->|)| SF_SYM  %% Símbolo: fecha parêntese
    S0 -->|:| SF_SYM  %% Símbolo: dois pontos
    S0 -->|,| SF_SYM  %% Símbolo: vírgula

    %% Estados finais
    SF_ID((Identificador))
    SF_INT((Inteiro))
    SF_REAL((Real))
    SF_STR((String))
    SF_COM((Comentário))
    SF_OP((Operador))
    SF_SYM((Símbolo))
```

<!-- Diagrama gerado representa o AFD para todos os tipos de tokens da linguagem Apollo. 
Cada transição está comentada para indicar o tipo de token reconhecido. -->
