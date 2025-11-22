# Documentação de Erros - Linguagem Apollo
## Formato para Apresentação

---

## Visão Geral

**Objetivo:**
- Registrar erros e problemas enfrentados
- Documentar soluções implementadas
- Compartilhar lições aprendidas

**Total de problemas:** 14
- 5 erros críticos resolvidos
- 2 problemas menores
- 4 desafios de implementação
- 2 erros de design

---

## Erros Críticos

### 1. Falta de Formalização Matemática

**Problema:**
- Sem fundamentação teórica
- Alfabeto não definido formalmente
- Tokens não como conjuntos

**Solução:**
- Especificação formal completa
- Alfabeto: Σ = Σ_letras ∪ Σ_dígitos ∪ Σ_símbolos
- Tokens como conjuntos: ID, KW, INT, REAL, STR, OP

**Lição:** Teoria antes da prática

---

### 2. Strings Não Reconhecidas

**Problema:**
- AFD com transições estáticas
- Não aceitava caracteres variados
- Acentos e símbolos falhavam

**Causa:**
- Transições fixas para cada caractere
- Impossível para todos Unicode

**Solução:**
```python
# Simulação dinâmica
if self.name == 'string' and state == 1:
    if char == '"':
        state = 2  # Fecha string
    else:
        pos += 1  # Aceita qualquer caractere
```

**Resultado:** Strings funcionando perfeitamente

---

### 3. Comentários Incompletos

**Problema:**
- Não funcionavam no final de arquivo
- Esperava quebra de linha explícita

**Solução:**
```python
elif pos == len(text) - 1:
    state = 2  # Fim de arquivo = fim do comentário
```

**Resultado:** Comentários em todos os cenários

---

### 4. Booleanos Incorretos

**Problema:**
- `verdadeiro` e `falso` como `KEYWORD`
- Ordem de verificação errada

**Solução:**
```python
if lexema in {'verdadeiro', 'falso'}:
    return TokenType.BOOLEAN  # Prioriza sobre KEYWORD
```

**Resultado:** Booleanos corretos

---

### 5. Especificação Incompleta

**Problema:**
- Símbolos faltando: `{`, `}`, `[`, `]`, `;`
- Documentação desatualizada

**Solução:**
- Alfabeto expandido
- Revisão completa
- Sincronização código/documentação

**Resultado:** Especificação completa

---

## Problemas Menores

### 6. Emojis no Código
- **Problema:** Compatibilidade cross-platform
- **Solução:** Remoção completa
- **Status:** Resolvido

### 7. Comentário Isolado `#`
- **Status:** Caso específico, não crítico

### 8. Comentário com `\n`
- **Status:** Comportamento esperado

---

## Desafios de Implementação

### 9. Complexidade das Transições AFD

**Desafio:**
- Criar AFDs completos
- Gerenciar estados eficientemente

**Solução:**
- AFDs modulares (um por tipo)
- Simulação dinâmica para casos especiais

**Lição:** Modularidade facilita manutenção

---

### 10. Performance do Match Mais Longo

**Desafio:**
- Testar todos AFDs é custoso
- Prioridade em empates

**Solução:**
- Operadores testados do maior para menor
- AFDs otimizados

**Lição:** Ordenação resolve precedência

---

### 11. Gerenciamento de Estado

**Desafio:**
- Sincronizar posição, linha e coluna
- Buffer circular eficiente

**Solução:**
- Função centralizada `_update_position()`
- Aritmética modular

**Lição:** Centralização facilita manutenção

---

### 12. Integração de Componentes

**Desafio:**
- Desacoplar lexer e parser
- Interface flexível

**Solução:**
- `LexerInterface` padronizada
- Métodos: `next_token()`, `peek_token()`

**Lição:** Interfaces bem definidas facilitam integração

---

## Erros de Design

### 13. Planejamento Superficial

**Problema:**
- Foco só em implementação
- Sem formalização inicial

**Solução:**
- Diário reflexivo
- Documentação sistemática

**Lição:** Planejamento economiza tempo

---

### 14. Testes Insuficientes

**Problema:**
- Casos extremos não testados
- Cobertura incompleta

**Solução:**
- `teste_completo.py` criado
- Testes específicos por funcionalidade

**Lição:** Testes abrangentes são essenciais

---

## Métricas

| Categoria | Quantidade | Status |
|-----------|------------|--------|
| Erros Críticos | 5 | Resolvidos |
| Problemas Menores | 2 | Aceitáveis |
| Desafios | 4 | Resolvidos |
| Design | 2 | Corrigidos |

---

## Lições Aprendidas

### 1. Formalização
- Teoria antes da prática
- Especificações facilitam comunicação

### 2. Testes
- Cobrir casos extremos
- Validação sistemática

### 3. Modularidade
- Componentes independentes
- Separação de responsabilidades

### 4. Documentação
- Manter sincronizada
- Documentar decisões

### 5. Revisão
- Revisões periódicas
- Feedback valioso

---

## Resumo dos Erros

### Top 5 Erros Críticos
1. **Formalização** - Criada especificação matemática
2. **Strings** - Simulação dinâmica implementada
3. **Comentários** - Tratamento de fim de arquivo
4. **Booleanos** - Priorização de tipos corrigida
5. **Especificação** - Alfabeto completo

### Principais Soluções
- **Simulação dinâmica** para padrões variados
- **Modularidade** em AFDs
- **Ordenação** para precedência
- **Documentação** sistemática

---

## Status Final

**Todos os erros críticos resolvidos**

- Base teórica sólida
- Implementação robusta
- Testes abrangentes
- Documentação completa

**Próximos passos:**
- Análise sintática (parser)
- Tratamento de erros robusto
- Otimizações de performance
