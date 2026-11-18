# Testes reais da Qwen — Passo Firme

## Ambiente

- Modelo: Qwen2.5-1.5B-Instruct
- Execução: Google Colab, CPU
- Geração: determinística (do_sample=False)
- Base: cinco trechos documentais

## Caso 1 — Recusa indevida

Pergunta:
Condomínios são responsáveis pelas calçadas?

Resposta observada:
"Não consta na base fornecida se condomínios
são responsáveis pelas calçadas."

Resultado: incorreto.

A base continha informação sobre condomínios
no documento lei_15442_art10.

## Caso 2 — Contradição na resposta

Ao receber o documento diretamente, a Qwen
respondeu "Não", mas explicou que condomínios
estavam entre os responsáveis.

Resultado: resposta contraditória.

## Caso 3 — Extração de evidência

A Qwen identificou a palavra "condomínios".

O validador recuperou a frase original:

"Entre os responsáveis pela manutenção estão
proprietários, possuidores e condomínios."

Resultado: evidência literal validada.

## Caso 4 — Qwen com fallback integrado

A API executou a Qwen real e acionou o
fallback extrativo após uma recusa.

Resultado observado:

- HTTP: 200
- Modo: fallback_extrativo
- Fonte: lei_15442_art10
- Evidência literal: validada
- Resposta conclusiva: não

## Conclusão

A integração técnica da LLM foi demonstrada.

Os testes identificaram erros reais de
interpretação e recusas indevidas.

O fallback recuperou evidência documental
em um caso concreto, mas não comprova
precisão factual geral.

Não foi estabelecida uma taxa confiável
de alucinação ou superioridade estatística
sobre o modelo sem contexto.
