# AFDs - Linguagem Apollo

## 1. Identificadores
```mermaid
stateDiagram-v2
    [*] --> q0
    q0 --> q1 : letra
    q1 --> q1 : letra|dígito|_
    q1 --> [*]
```

## 2. Números Inteiros
```mermaid
stateDiagram-v2
    [*] --> q0
    q0 --> q1 : +|-
    q0 --> q2 : dígito
    q1 --> q2 : dígito
    q2 --> q2 : dígito
    q2 --> [*]
```

## 3. Números Reais
```mermaid
stateDiagram-v2
    [*] --> q0
    q0 --> q1 : +|-
    q0 --> q2 : dígito
    q1 --> q2 : dígito
    q2 --> q2 : dígito
    q2 --> q3 : .
    q3 --> q4 : dígito
    q4 --> q4 : dígito
    q4 --> [*]
```

## 4. Strings
```mermaid
stateDiagram-v2
    [*] --> q0
    q0 --> q1 : "
    q1 --> q1 : char
    q1 --> q2 : "
    q2 --> [*]
```

## 5. Operadores
```mermaid
stateDiagram-v2
    [*] --> q0
    q0 --> q1 : =
    q0 --> q2 : !
    q0 --> q3 : <
    q0 --> q4 : >
    q1 --> q5 : =
    q2 --> q6 : =
    q3 --> q7 : =
    q3 --> [*]
    q4 --> q8 : =
    q4 --> [*]
    q5 --> [*]
    q6 --> [*]
    q7 --> [*]
    q8 --> [*]
```

## 6. Comentários
```mermaid
stateDiagram-v2
    [*] --> q0
    q0 --> q1 : #
    q1 --> q1 : char
    q1 --> q2 : \n
    q2 --> [*]
```
