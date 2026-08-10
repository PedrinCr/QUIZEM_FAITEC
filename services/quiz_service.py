# services/quiz_service.py — Lógica do quiz e cálculo de pontuação

import random
from models.questao import Questao
from models.jogador  import Jogador
from config import PONTOS_ACERTO, PONTOS_ERRO, BONUS_DESEMPENHO


class QuizService:
    """Gerencia o fluxo de uma sessão de quiz."""

    def __init__(self, questoes_raw: list[dict], embaralhar: bool = True):
        self.questoes: list[Questao] = [Questao(q) for q in questoes_raw]
        if embaralhar:
            random.shuffle(self.questoes)

        self.jogador         = Jogador()
        self.indice_atual:   int  = 0
        self.finalizado:     bool = False

    # ── Navegação ──────────────────────────────────────────────────────────

    @property
    def questao_atual(self) -> Questao | None:
        if self.indice_atual < len(self.questoes):
            return self.questoes[self.indice_atual]
        return None

    @property
    def numero_atual(self) -> int:
        """Retorna o número da questão atual (1-based)."""
        return self.indice_atual + 1

    @property
    def total_questoes(self) -> int:
        return len(self.questoes)

    def tem_proxima(self) -> bool:
        return self.indice_atual < len(self.questoes) - 1

    def avancar(self):
        """Avança para a próxima questão."""
        if self.tem_proxima():
            self.indice_atual += 1
        else:
            self._finalizar()

    # ── Respostas ──────────────────────────────────────────────────────────

    def responder(self, indice_escolhido: int) -> bool:
        """
        Registra a resposta do jogador e atualiza a pontuação.
        Retorna True se acertou, False se errou.
        """
        questao = self.questao_atual
        if questao is None:
            return False

        acertou = questao.verificar_resposta(indice_escolhido)

        if acertou:
            self.jogador.registrar_acerto(PONTOS_ACERTO)
        else:
            self.jogador.registrar_erro()

        return acertou

    # ── Finalização ────────────────────────────────────────────────────────

    def _finalizar(self):
        """Calcula e aplica o bônus de desempenho ao encerrar o quiz."""
        self.finalizado = True
        bonus = self._calcular_bonus(self.jogador.porcentagem)
        self.jogador.adicionar_bonus(bonus)

    def _calcular_bonus(self, porcentagem: float) -> int:
        for limite in sorted(BONUS_DESEMPENHO.keys(), reverse=True):
            if porcentagem >= limite:
                return BONUS_DESEMPENHO[limite]
        return 0

    def obter_resultado(self) -> dict:
        """Retorna um resumo do resultado da sessão."""
        return {
            "pontuacao":   self.jogador.pontuacao,
            "acertos":     self.jogador.acertos,
            "erros":       self.jogador.erros,
            "total":       self.jogador.total,
            "porcentagem": self.jogador.porcentagem,
        }
