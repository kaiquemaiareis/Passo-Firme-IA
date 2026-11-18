
from functools import lru_cache

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODELO_ID = "Qwen/Qwen2.5-1.5B-Instruct"


@lru_cache(maxsize=1)
def carregar_modelo():
    dispositivo = (
        "cuda" if torch.cuda.is_available() else "cpu"
    )

    tokenizer = AutoTokenizer.from_pretrained(MODELO_ID)

    modelo = AutoModelForCausalLM.from_pretrained(
        MODELO_ID,
        dtype=(
            torch.float16
            if dispositivo == "cuda"
            else torch.float32
        )
    )

    modelo.to(dispositivo)
    modelo.eval()

    return tokenizer, modelo, dispositivo


def gerar_resposta(pergunta, documentos):
    tokenizer, modelo, dispositivo = carregar_modelo()

    contexto = "\n\n".join(
        f"Fonte: {doc['id']}\n{doc['texto']}"
        for doc in documentos
    )

    mensagens = [
        {
            "role": "system",
            "content": (
                "Você é o assistente do Passo Firme. "
                "Responda somente com as informações "
                "presentes nos documentos fornecidos. "
                "Se não houver evidência suficiente, "
                "responda 'Não consta na base fornecida'. "
                "Não invente fatos ou fontes."
            )
        },
        {
            "role": "user",
            "content": (
                f"Documentos:\n{contexto}\n\n"
                f"Pergunta: {pergunta}"
            )
        }
    ]

    texto = tokenizer.apply_chat_template(
        mensagens,
        tokenize=False,
        add_generation_prompt=True
    )

    entradas = tokenizer(
        texto,
        return_tensors="pt"
    ).to(dispositivo)

    with torch.inference_mode():
        saida = modelo.generate(
            **entradas,
            max_new_tokens=180,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id
        )

    tokens_resposta = saida[0][
        entradas["input_ids"].shape[1]:
    ]

    return tokenizer.decode(
        tokens_resposta,
        skip_special_tokens=True
    ).strip()
