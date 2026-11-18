
import unittest
from fastapi.testclient import TestClient
from api.main import app


class TestPassoFirmeAPI(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_health(self):
        resposta = self.client.get("/health")

        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.json()["status"], "ok")
        self.assertEqual(resposta.json()["documentos"], 5)

    def test_busca(self):
        resposta = self.client.post(
            "/buscar",
            json={"pergunta": "Quem cuida das calçadas?"}
        )

        self.assertEqual(resposta.status_code, 200)
        self.assertGreater(
            len(resposta.json()["resultados"]), 0
        )

    def test_resposta_com_fonte(self):
        resposta = self.client.post(
            "/assistente",
            json={
                "pergunta": "Condomínios são responsáveis pelas calçadas?"
            }
        )

        dados = resposta.json()

        self.assertEqual(resposta.status_code, 200)
        self.assertFalse(dados["recusa"])
        self.assertIn("lei_15442_art10", dados["fontes"])

    def test_recusa(self):
        resposta = self.client.post(
            "/assistente",
            json={
                "pergunta": "Quantas reclamações foram registradas ontem?"
            }
        )

        dados = resposta.json()

        self.assertEqual(resposta.status_code, 200)
        self.assertTrue(dados["recusa"])
        self.assertEqual(dados["fontes"], [])

    def test_pergunta_vazia(self):
        resposta = self.client.post(
            "/assistente",
            json={"pergunta": ""}
        )

        self.assertEqual(resposta.status_code, 400)


if __name__ == "__main__":
    unittest.main()
