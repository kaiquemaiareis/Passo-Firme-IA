# Passo Firme - Placar Preliminar

## Comparacao das tres configuracoes

| Metrica | Sem contexto | RAG simples | RAG + agente |
|---|---|---|---|
| Perguntas testadas | 15 | 15 | 15 |
| Chamadas da LLM | 15 | 9 | 10 |
| JSON bruto valido | 14/15 | 4/9 | 5/10 |
| Recusas corretas do sistema | Nao calculado | 5/5 | 5/5 |
| Recusas indevidas | Nao calculado | 1 | 0 |

## Busca de documentos

- Busca semantica: Recall@1 = 80%, Recall@3 = 90%.
- Busca hibrida sem filtro: Recall@1 = 90%, Recall@3 = 100%.
- Busca hibrida com limiar 0,26: 9/10 fontes esperadas recuperadas.
- Rejeicao pela busca com limiar 0,26: 5/5 perguntas sem resposta.

## Interpretacao

A estrategia com agente recuperou uma fonte que o RAG
simples havia rejeitado indevidamente.

A validade do JSON bruto nao melhorou em relacao
ao modelo sem contexto. A normalizacao de saida
foi implementada separadamente.

As recusas automaticas nao foram geradas pela LLM.

## Limitacoes

- Base inicial com apenas cinco trechos resumidos.
- Quinze perguntas usadas tambem no ajuste da busca.
- Sem avaliacao completa de precisao factual.
- Nem todas as respostas individuais foram recuperadas.
- Resultados preliminares, sem garantia de generalizacao.
