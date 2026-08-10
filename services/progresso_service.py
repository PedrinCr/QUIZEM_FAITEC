# services/progresso_service.py — Salvar e carregar progresso em JSON

import json
import os
from config import ARQUIVO_PROGRESSO


class ProgressoService:
    """
    Gerencia o progresso do jogador, persistido em um arquivo JSON local.

    Estrutura do JSON:
    {
        "Estequiometria": {
            "Balanceamento de Equações": {
                "tentativas": 3,
                "melhor_porcentagem": 80.0,
                "concluido": false
            },
            ...
        },
        ...
    }
    """

    def __init__(self):
        self._dados: dict = self._carregar()

    # ── Carregamento / Salvamento ───────────────────────────────────────────

    def _carregar(self) -> dict:
        if os.path.exists(ARQUIVO_PROGRESSO):
            try:
                with open(ARQUIVO_PROGRESSO, "r", encoding="utf-8") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return {}
        return {}

    def _salvar(self):
        with open(ARQUIVO_PROGRESSO, "w", encoding="utf-8") as f:
            json.dump(self._dados, f, ensure_ascii=False, indent=2)

    # ── Atualização ────────────────────────────────────────────────────────

    def registrar_resultado(
        self,
        submateria:  str,
        conteudo:    str,
        porcentagem: float,
    ):
        """Atualiza o progresso após uma sessão de quiz."""
        if submateria not in self._dados:
            self._dados[submateria] = {}

        entrada_atual = self._dados[submateria].get(conteudo, {
            "tentativas":         0,
            "melhor_porcentagem": 0.0,
            "concluido":          False,
        })

        entrada_atual["tentativas"] += 1
        if porcentagem > entrada_atual["melhor_porcentagem"]:
            entrada_atual["melhor_porcentagem"] = porcentagem
        if porcentagem >= 100.0:
            entrada_atual["concluido"] = True

        self._dados[submateria][conteudo] = entrada_atual
        self._salvar()

    # ── Consulta ───────────────────────────────────────────────────────────

    def obter_progresso_conteudo(self, submateria: str, conteudo: str) -> dict:
        """Retorna o progresso de um conteúdo específico."""
        return self._dados.get(submateria, {}).get(conteudo, {
            "tentativas":         0,
            "melhor_porcentagem": 0.0,
            "concluido":          False,
        })

    def obter_progresso_submateria(self, submateria: str) -> dict:
        """Retorna todos os conteúdos e seu progresso dentro de uma submatéria."""
        return self._dados.get(submateria, {})

    def obter_tudo(self) -> dict:
        """Retorna o progresso completo."""
        return self._dados

    def status_label(self, submateria: str, conteudo: str) -> str:
        """
        Retorna uma string de status legível para exibir na tela de progresso.
        Exemplos: 'Concluído', '80%', 'Não iniciado'
        """
        prog = self.obter_progresso_conteudo(submateria, conteudo)
        if prog["tentativas"] == 0:
            return "Não iniciado"
        if prog["concluido"]:
            return "Concluído ✓"
        return f"{prog['melhor_porcentagem']:.0f}%"
