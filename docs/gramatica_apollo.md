## Gramática formal da linguagem Apollo (inspirada em MicroJava)

Este documento apresenta a definição formal (EBNF) da gramática da linguagem *Apollo*, inspirada na explicação do professor e na gramática do MicroJava. O objetivo é fornecer uma especificação suficiente para implementar um parser (ou para gerar uma gramática para ferramentas de análise sintática).

Observações:
- Notação: usamos EBNF. Terminales (palavras reservadas, símbolos) aparecem entre aspas, não-terminais em letra capitalizada.
- Símbolos opcionais: [ ... ]
- Repetição: { ... }
- Start symbol: `Program`.

## Símbolos terminais (visão lexis)

- identificador: `IDENT` — letra seguida de letras/dígitos/_ (ex.: `x`, `soma1`).
- número inteiro: `NUMBER` — sequência de dígitos (ex.: `0`, `123`).
- caractere: `CHAR` — literal de caractere (ex.: `'a'`).
- string: `STRING` — literal entre aspas (ex.: "hello").
- palavras reservadas: `const`, `var`, `func`, `return`, `if`, `else`, `while`, `print`, `read`, `true`, `false`, `int`, `bool`, `char`, `void`.
- operadores e pontuação: `+ - * / % = == != < > <= >= && || ! ( ) { } [ ] , ;` e `.` (ponto, se necessário).

Comentários e espaçamento são ignorados pela análise léxica (espaços, tabs, novas linhas, comentários de linha `//` e comentários multi-linha `/* ... */`).

## 1. Declaração inicial e módulos

Program ::= { Declaration }

Declaration ::= ConstDecl | VarDecl | FuncDecl

ConstDecl ::= "const" ConstList ";"
ConstList ::= ConstDef { "," ConstDef }
ConstDef ::= IDENT "=" Literal

VarDecl ::= "var" VarList ";"
VarList ::= VarDef { "," VarDef }
VarDef ::= IDENT [ "[" NUMBER "]" ]

FuncDecl ::= "func" Type IDENT "(" [ ParamList ] ")" Block

Type ::= "int" | "bool" | "char" | IDENT | "void"
ParamList ::= Param { "," Param }
Param ::= Type IDENT [ "[" "]" ]

Block ::= "{" { VarDecl } { Statement } "}"

## 2. Sentenças (statements)

Statement ::= Block
           | ";"
           | Assignment ";"
           | IfStmt
           | WhileStmt
           | ReturnStmt ";"
           | PrintStmt ";"
           | ReadStmt ";"
           | ExprStmt ";"

Assignment ::= LValue "=" Expr
LValue ::= IDENT { "[" Expr "]" }

IfStmt ::= "if" "(" Expr ")" Statement [ "else" Statement ]
WhileStmt ::= "while" "(" Expr ")" Statement
ReturnStmt ::= "return" [ Expr ]
PrintStmt ::= "print" "(" [ ExprList ] ")"
ReadStmt ::= "read" "(" LValue ")"
ExprStmt ::= Expr

## 3. Expressões (precedência e associatividade)

Start: Expr

Expr ::= OrExpr

OrExpr ::= AndExpr { "||" AndExpr }
AndExpr ::= RelExpr { "&&" RelExpr }
RelExpr ::= AddExpr [ ("==" | "!=" | "<" | ">" | "<=" | ">=") AddExpr ]
AddExpr ::= MulExpr { ("+" | "-") MulExpr }
MulExpr ::= UnaryExpr { ("*" | "/" | "%") UnaryExpr }
UnaryExpr ::= [ ("!" | "-") ] Primary

Primary ::= Literal
          | IDENT [ FunctionCallOrIndex ]
          | "(" Expr ")"

FunctionCallOrIndex ::= "(" [ ExprList ] ")" | "[" Expr "]"

ExprList ::= Expr { "," Expr }

Literal ::= NUMBER | CHAR | STRING | "true" | "false"

Notas de precedência (maior para menor):
- unary ("!", "-") — associatividade direita
- multiplicativo ("*", "/", "%") — associatividade esquerda
- aditivo ("+", "-") — associatividade esquerda
- relacionais ("<", ">", "<=", ">=")
- igualdade ("==", "!=")
- lógico AND ("&&") — associatividade esquerda
- lógico OR ("||") — associatividade esquerda

## 4. Regras adicionais e restrições semânticas

- Uma `func` com tipo `void` não deve obrigatoriamente retornar um valor; funções com outro tipo devem garantir que `return` retorne um valor compatível.
- Índices de array devem ser valores inteiros não-negativos em tempo de execução; o analisador sintático apenas aceita sintaxe `IDENT "[" Expr "]"`.
- Não-terminais `IDENT` usados como chamadas de função e acessos a arrays são desambiguados por presença de '(' ou '[' na análise.

## 5. Exemplo de programa Apollo

```apl
const PI = 3;
var n, a[10];

func int soma(int m, int arr[]) {
  var i, s;
  s = 0;
  i = 0;
  while (i < m) {
    s = s + arr[i];
    i = i + 1;
  }
  return s;
}

func void main() {
  var total;
  total = soma(n, a);
  print(total);
}
```

## 6. Notas para implementação do parser

- A gramática foi escrita em EBNF simples; para gerar um parser com ferramentas LR/LL é recomendável transformar construções ambíguas e left-recursivas (se houver) conforme o requisito do gerador usado.
- Para análise semântica cuide de: tabelas de símbolos (escopos), tipos (compatibilidade em atribuições e retornos), e checagem de aridade de chamadas de função.
- Tokens léxicos devem distinguir `IDENT` e palavras reservadas; reconheça literais numéricos, caracteres e strings.

## 7. Próximos passos sugeridos

- Formalizar a gramática em um formato suportado por um gerador (por ex., ANTLR, bison) se desejar gerar um parser automaticamente.
- Criar testes de parsing (casos válidos e inválidos) para validar a gramática.

---
