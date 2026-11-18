# Passo Firme — Generative AI

## Sobre o projeto
Assistente de IA para orientar cidadãos sobre
responsabilidades e conservação de calçadas
na cidade de São Paulo.

## Tecnologias
- Qwen2.5-1.5B-Instruct
- Python e PyTorch
- RAG com embeddings multilíngues
- Busca semântica e híbrida
- Agente com ferramentas de recuperação

## Configurações avaliadas
1. LLM sem contexto
2. LLM com RAG
3. LLM com RAG e agente

## Estrutura
- notebooks/: experimentos executados no Colab
- base/: base inicial de conhecimento
- avaliacao/: testes, métricas e análise de erros

## Resultados
Consultar avaliacao/placar_preliminar.md.

Os resultados são preliminares.
A base legal ainda requer conferência dos
textos oficiais e avaliação independente.

## Como executar
1. Abrir o notebook no Google Colab.
2. Ativar GPU, se disponível.
3. Instalar as dependências.
4. Executar as células em ordem.

## Pendências
- Revisar e ampliar a base documental
- Consolidar avaliação factual e latência
- Implementar e testar a API
- Validar a reprodução do notebook
- Preencher nomes completos e RMs
