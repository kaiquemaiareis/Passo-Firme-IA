# Passo Firme — Relatório Técnico de IA Generativa

## 1. Identificação

Disciplina: Generative AI for Engineering

Projeto: Passo Firme — CitizenTech

Integrantes: PREENCHER NOMES COMPLETOS E RMs

## 2. Problema e objetivo

O Passo Firme busca apoiar a mobilidade acessível
em São Paulo, oferecendo informações sobre
responsabilidades e conservação de calçadas.

O componente de IA utiliza uma LLM aberta,
uma base documental e mecanismos de recuperação
de informações para responder a perguntas.

O objetivo experimental é comparar:
1. LLM sem contexto;
2. LLM com RAG;
3. LLM com RAG e agente de recuperação.

## 3. Arquitetura

Fluxo experimental:

Pergunta do usuário
→ Busca semântica ou híbrida
→ Seleção de documentos
→ LLM Qwen
→ Validação do JSON e das fontes
→ Resposta

O agente acrescenta uma ferramenta de busca
por termos específicos quando a busca principal
não encontra evidências suficientes.

A API FastAPI disponível no repositório possui
um modo provisório de consulta documental.
A integração real da Qwen à API está pendente.

## 4. Tecnologias

- Python e PyTorch
- Qwen2.5-1.5B-Instruct
- Hugging Face Transformers
- Sentence Transformers
- Embeddings multilíngues MiniLM
- TF-IDF e busca híbrida
- FastAPI
- Google Colab

## 5. Base de conhecimento

Base inicial: 5 trechos resumidos.

Fontes documentais:
- Lei Municipal 15.442/2011
- Decreto Municipal 59.671/2020

Formato: JSON

Os trechos são resumos usados para prototipação,
não transcrições literais.

É necessário verificar os textos consolidados,
o enquadramento jurídico, as licenças e a
correspondência entre artigos e resumos.

## 6. Conjunto de testes

15 perguntas com gabarito:
- 10 com respostas esperadas na base;
- 5 cuja resposta não consta na base.

Os testes iniciais também foram utilizados
para ajustar os pesos e os limiares da busca.

Portanto, as métricas são preliminares.

## 7. Resultados de recuperação

Busca semântica:
- Recall@1: 80%
- Recall@3: 90%

Busca híbrida sem filtro:
- Recall@1: 90%
- Recall@3: 100%

Busca híbrida com limiar 0,26:
- Fontes esperadas recuperadas: 9/10
- Perguntas sem resposta rejeitadas: 5/5

O limiar foi escolhido empiricamente nos
testes iniciais e não foi validado em uma
amostra independente.

## 8. Comparação das configurações

LLM sem contexto:
- 15 perguntas executadas
- 14/15 JSONs originalmente válidos

RAG simples:
- 15 perguntas avaliadas
- 9 chamadas à LLM
- 4/9 JSONs originalmente válidos
- 5/5 recusas corretas do sistema
- 1 recusa indevida

RAG com agente:
- 15 perguntas avaliadas
- 10 chamadas à LLM
- 5/10 JSONs originalmente válidos
- 5/5 recusas corretas do sistema
- 0 recusas indevidas

As recusas por filtro são decisões do sistema,
não respostas geradas pela LLM.

A normalização de JSON e fontes foi feita
em uma etapa separada.

Ainda não há avaliação factual completa
nem taxa definitiva de alucinação.

## 9. Análise de erros

Foram documentados cinco erros observados:
1. Informações não fundamentadas;
2. Fonte inventada;
3. JSON com formatação Markdown;
4. Citação fora do padrão;
5. Recusa indevida.

Detalhes, causas prováveis e correções estão em:
avaliacao/analise_5_erros.md

## 10. API

Endpoints implementados:
- GET /health
- POST /buscar
- POST /assistente

O endpoint /assistente opera atualmente
em modo de consulta documental sem LLM.

Testes locais realizados com FastAPI TestClient.

Não há comprovação de implantação pública
ou integração ao MVP principal nesta etapa.

## 11. Limitações

- Base documental pequena;
- Resumos legais pendentes de revisão;
- Testes utilizados durante calibração;
- Falta avaliação independente;
- Resultados individuais parcialmente perdidos
  após reinicialização do Google Colab;
- Integração real entre LLM, API e MVP pendente;
- Não foi comprovada uma redução geral da
  taxa de alucinação.

## 12. Conclusão técnica

O protótipo demonstrou o funcionamento de
uma LLM local, recuperação documental,
busca híbrida e um agente com ferramentas.

O agente recuperou a fonte da pergunta sobre
condomínios, que havia sido rejeitada pelo
RAG simples.

Os experimentos identificaram problemas
de recuperação, citação e formatação JSON.

A melhoria observada na recuperação não
comprova, isoladamente, maior precisão
factual ou menor alucinação.

## 13. Links

GitHub: PREENCHER
MVP: PREENCHER
Vídeo de demonstração: PREENCHER
