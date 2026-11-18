
import re


def validar_evidencia(trecho, documento):
    if not isinstance(trecho, str):
        return None

    trecho = trecho.strip().strip('"“”').strip()

    if len(trecho) < 4:
        return None

    texto = documento["texto"]

    frases = re.split(r"(?<=[.!?])\s+", texto)

    for frase in frases:
        if trecho.casefold() in frase.casefold():
            return {
                "evidencia": frase.strip(),
                "fonte": documento["id"],
                "validada": True
            }

    return None
