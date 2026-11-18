
import re
import unicodedata

STOPWORDS = {
    "a", "o", "as", "os", "de", "da", "do",
    "das", "dos", "em", "na", "no", "nas",
    "nos", "um", "uma", "e", "ou", "que",
    "qual", "quais", "quem", "como", "por",
    "para", "com", "sao", "ser", "pode",
    "podem", "pelas", "pelos", "pela", "pelo",
    "esta", "estao", "isso"
}


def palavras_relevantes(texto):
    texto = unicodedata.normalize(
        "NFKD", texto.lower()
    )
    texto = "".join(
        c for c in texto
        if not unicodedata.combining(c)
    )

    palavras = set(re.findall(r"\b\w+\b", texto))

    return {
        p for p in palavras
        if len(p) >= 4 and p not in STOPWORDS
    }


def buscar_evidencia(pergunta, documento):
    termos_pergunta = palavras_relevantes(pergunta)

    frases = re.split(
        r"(?<=[.!?])\s+",
        documento["texto"]
    )

    melhor_frase = None
    maior_pontuacao = 0

    for frase in frases:
        termos_frase = palavras_relevantes(frase)

        coincidencias = len(
            termos_pergunta & termos_frase
        )

        if coincidencias > maior_pontuacao:
            maior_pontuacao = coincidencias
            melhor_frase = frase

    # Exige pelo menos dois termos relevantes coincidentes
    if maior_pontuacao < 2:
        return None

    return {
        "resposta": "Trecho encontrado na base: " + melhor_frase,
        "evidencia": melhor_frase,
        "fontes": [documento["id"]],
        "tipo": "fallback_extrativo",
        "termos_coincidentes": maior_pontuacao
    }
