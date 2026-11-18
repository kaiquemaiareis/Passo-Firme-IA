import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient

from api.main import app, documentos


class TestFallback(unittest.TestCase):

    def setUp(self):
        self.cliente = TestClient(app)
        self.pergunta = {
            "pergunta": "Condomínios são responsáveis pelas calçadas?",
            "usar_llm": True
        }

    def test_fallback_recupera_evidencia(self):
        with patch(
            "api.llm_local.gerar_resposta",
            return_value="Não consta na base fornecida."
        ):
            resposta = self.cliente.post(
                "/assistente", json=self.pergunta
            )

        dados = resposta.json()

        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(dados["modo"], "fallback_extrativo")
        self.assertFalse(dados["resposta_conclusiva"])
        self.assertIn("lei_15442_art10", dados["fontes"])

        documento = next(
            d for d in documentos
            if d["id"] == dados["fontes"][0]
        )

        self.assertIn(dados["evidencia"], documento["texto"])

    def test_recusa_preservada(self):
        with patch(
            "api.llm_local.gerar_resposta",
            return_value="Não consta na base fornecida."
        ), patch(
            "api.fallback_extrativo.buscar_evidencia",
            return_value=None
        ):
            resposta = self.cliente.post(
                "/assistente", json=self.pergunta
            )

        dados = resposta.json()

        self.assertEqual(resposta.status_code, 200)
        self.assertTrue(dados["recusa"])
        self.assertEqual(dados["fontes"], [])


if __name__ == "__main__":
    unittest.main()
