
import json
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer

app = FastAPI(
    title="Passo Firme - API de IA",
    version="0.1.0"
)

BASE = Path(__file__).resolve().parent.parent / "base" / "base_conhecimento.json"

with open(BASE, encoding="utf-8") as f:
    documentos = json.load(f)

textos = [d["fonte"] + " " + d["texto"] for d in documentos]

buscador = TfidfVectorizer(
    strip_accents="unicode",
    ngram_range=(1, 2)
)

matriz = buscador.fit_transform(textos)

class Pergunta(BaseModel):
    pergunta: str
    usar_llm: bool = False

@app.get("/health")
def health():
    return {
        "status": "ok",
        "documentos": len(documentos),
        "llm_integrada": False
    }

@app.post("/buscar")
def buscar(entrada: Pergunta):
    if not entrada.pergunta.strip():
        raise HTTPException(400, "Pergunta vazia")

    vetor = buscador.transform([entrada.pergunta])
    scores = (vetor @ matriz.T).toarray().ravel()

    indices = scores.argsort()[::-1][:3]

    return {
        "pergunta": entrada.pergunta,
        "resultados": [
            {
                "id": documentos[int(i)]["id"],
                "fonte": documentos[int(i)]["fonte"],
                "pontuacao": round(float(scores[i]), 3)
            }
            for i in indices if scores[i] > 0
        ]
    }


@app.post("/assistente")
def assistente(entrada: Pergunta):
    import re
    import unicodedata

    pergunta = entrada.pergunta.strip()

    if not pergunta:
        raise HTTPException(400, "Pergunta vazia")

    def normalizar(texto):
        texto = unicodedata.normalize("NFKD", texto.lower())
        return "".join(
            c for c in texto
            if not unicodedata.combining(c)
        )

    pergunta_normalizada = normalizar(pergunta)

    consulta_atual = bool(re.search(
        r"\b(ontem|hoje|atualmente)\b",
        pergunta_normalizada
    ))

    vetor = buscador.transform([pergunta])
    scores = (vetor @ matriz.T).toarray().ravel()

    indice = int(scores.argmax())
    pontuacao = float(scores[indice])

    if consulta_atual or pontuacao < 0.10:
        return {
            "resposta": "Não consta na base de conhecimento fornecida.",
            "fontes": [],
            "recusa": True,
            "modo": "consulta_documental_sem_llm"
        }

    documento = documentos[indice]

    if entrada.usar_llm:
        from .llm_local import gerar_resposta

        resposta_llm = gerar_resposta(
            pergunta,
            [documento]
        )

        if not resposta_llm:
            raise HTTPException(
                503,
                "A LLM não produziu uma resposta."
            )

        resposta_normalizada = normalizar(resposta_llm)

        recusou = (
            "nao consta" in resposta_normalizada
            or "nao ha informac" in resposta_normalizada
            or "nao tenho informac" in resposta_normalizada
        )

        return {
            "resposta": resposta_llm,
            "fontes": [] if recusou else [documento["id"]],
            "recusa": recusou,
            "modo": "qwen_com_contexto"
        }

    return {
        "resposta": documento["texto"],
        "fontes": [documento["id"]],
        "recusa": False,
        "modo": "consulta_documental_sem_llm"
    }
