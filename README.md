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
- Integrar a LLM Qwen à API e validar o funcionamento completo
- Validar a reprodução do notebook

## API FastAPI

A API possui três endpoints:

- `GET /health`: verifica o funcionamento.
- `POST /buscar`: recupera fontes usando TF-IDF.
- `POST /assistente`: responde com base nos documentos ou recusa perguntas sem evidência suficiente.

**Limitação:** atualmente, o endpoint `/assistente` funciona em modo de consulta documental, sem executar a LLM Qwen. Os experimentos com Qwen, RAG e agente estão no notebook.

### Executar localmente

Instale as dependências:

```bash
pip install -r requirements.txt
```

Na pasta raiz do projeto, execute:

```bash
uvicorn api.main:app --reload
```

A documentação interativa estará disponível em:

http://127.0.0.1:8000/docs

Os endpoints foram testados localmente com FastAPI TestClient.
