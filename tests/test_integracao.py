import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient
from api.main import app


class TestIntegracaoQwen(unittest.TestCase):

    def test_chamada_da_llm(self):
        cliente = TestClient(app)

        with patch(
            "api.llm_local.gerar_resposta",
            return_value="Sim, condomínios podem ser responsáveis."
        ) as gerador:

            resposta = cliente.post(
                "/assistente",
                json={
                    "pergunta": "Condomínios são responsáveis pelas calçadas?",
                    "usar_llm": True
                }
            )

            self.assertEqual(resposta.status_code, 200)

            dados = resposta.json()

            self.assertEqual(
                dados["modo"],
                "qwen_com_contexto"
            )

            self.assertIn(
                "lei_15442_art10",
                dados["fontes"]
            )

            gerador.assert_called_once()

            argumentos = gerador.call_args.args
            self.assertEqual(
                len(argumentos[1]),
                1
            )


if __name__ == "__main__":
    unittest.main()
