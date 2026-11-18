# Passo Firme — Análise de 5 erros reais

## Erro 1 — Informações não fundamentadas

**Configuração:** LLM sem contexto.

**Evidência observada:**
Ao perguntar quem mantém as calçadas de São Paulo,
a IA afirmou que a Prefeitura era a principal
responsável e listou entidades como CITM e
Fundação Cultural São Paulo, sem apresentar fontes.

**Causa provável:**
O modelo respondeu usando conhecimento interno,
sem consultar a legislação municipal.

**Correção proposta:**
Usar RAG com documentos oficiais, exigir citações
verificáveis e rejeitar informações sem fundamento.

---

## Erro 2 — Fonte inventada

**Configuração:** Primeiro protótipo RAG.

**Evidência observada:**
A IA gerou um endereço do Planalto para a
Lei 15.442/2011 que não existia nos documentos
recuperados.

**Causa provável:**
O modelo gerou livremente um endereço de fonte.

**Correção proposta:**
Usar IDs de documentos e inserir URLs oficiais
pelo código Python, sem permitir links inventados.

---

## Erro 3 — JSON com formatação Markdown

**Configuração:** RAG simples.

**Evidência observada:**
A resposta sobre conservação de calçadas veio
envolvida em marcadores ```json e ```,
causando falha na leitura direta por json.loads().

**Causa provável:**
A LLM não respeitou a instrução de produzir JSON puro.

**Correção proposta:**
Usar saída estruturada quando disponível,
validar o formato e normalizar blocos Markdown.
Preservar a resposta original na avaliação.

---

## Erro 4 — Citação fora do padrão

**Configuração:** RAG simples.

**Evidência observada:**
Na resposta sobre buracos, a IA citou
"Decreto 59.671/2020 - Art. 34"
em vez do ID "decreto_59671_art34".

**Causa provável:**
A LLM utilizou o nome legível da fonte
em lugar do identificador exigido pelo sistema.

**Correção proposta:**
Criar correspondência entre nomes e IDs,
validar contra documentos recuperados e
normalizar citações antes da resposta final.

---

## Erro 5 — Recusa indevida

**Configuração:** RAG simples.

**Evidência observada:**
A pergunta "Condomínios podem ser responsáveis
pelas calçadas?" foi recusada, mesmo havendo
informação na base no artigo 10.

**Causa provável:**
O documento correto obteve pontuação baixa
e ficou abaixo do limiar de similaridade.

**Correção proposta:**
Utilizar uma segunda ferramenta de busca,
baseada em termos específicos.

**Resultado observado:**
No protótipo de agente, a busca específica
recuperou "lei_15442_art10" e a IA respondeu
corretamente segundo a base inicial.

---

## Limitações da análise

Os cinco casos foram observados em diferentes
etapas do desenvolvimento, não somente na
avaliação final das três configurações.

As causas são hipóteses técnicas fundamentadas
nos comportamentos observados.

A base de conhecimento ainda precisa de revisão
jurídica e os resultados exigem validação adicional.
