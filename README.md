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


## Status da implementação

- Qwen2.5-1.5B-Instruct executada localmente.
- RAG e agente avaliados no Google Colab.
- API FastAPI implementada e testada.
- Integração opcional da Qwen com a API.
- Fallback extrativo para recusas da LLM.
- 8 testes automatizados aprovados, incluindo 
  2 testes de fallback com respostas simuladas.

## API FastAPI

Endpoints disponíveis:

- `GET /health`: diagnóstico da API.
- `POST /buscar`: recuperação documental por TF-IDF.
- `POST /assistente`: consulta ou geração com Qwen.

O endpoint `/assistente` aceita:

- `usar_llm=false`: consulta documental (padrão).
- `usar_llm=true`: geração utilizando a Qwen.

Quando a Qwen recusa uma pergunta, o sistema
pode apresentar um trecho relacionado da base
por meio do fallback extrativo.

A execução real da Qwen com fallback foi
validada na CPU do Google Colab.

**Limitações:** o fallback não garante
a relevância da evidência nem a precisão
factual da resposta. A avaliação é preliminar.

## Testes

Executar a partir da raiz do repositório:

```bash
python -m unittest discover -s tests -v
```

Os seis testes publicados foram executados
com sucesso. O teste de integração automatizado
utiliza uma resposta simulada da Qwen.

## Pendências

- Avaliação factual independente e latência.
- Revisão e ampliação da base documental.
- Integração da API ao MVP principal.
- Validação integral da reprodução do notebook.
- Inclusão dos links finais do MVP e do vídeo.

## Documentação

- [Relatório técnico](RELATORIO_TECNICO.md)
- [Fontes documentais](base/FONTES.md)
- [Placar preliminar](avaliacao/placar_preliminar.md)
- [Análise de cinco erros](avaliacao/analise_5_erros.md)


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
