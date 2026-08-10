# models/jogador.py — Modelo do jogador (sessão atual)

class Jogador:
    """Armazena o estado do jogador durante uma sessão de quiz."""

    def __init__(self):
        self.pontuacao:  int = 0
        self.acertos:    int = 0
        self.erros:      int = 0
        self.total:      int = 0

    def registrar_acerto(self, pontos: int):
        self.pontuacao += pontos
        self.acertos += 1
        self.total += 1

    def registrar_erro(self):
        self.erros += 1
        self.total += 1

    def adicionar_bonus(self, bonus: int):
        self.pontuacao += bonus

    @property
    def porcentagem(self) -> float:
        if self.total == 0:
            return 0.0
        return (self.acertos / self.total) * 100

    def resetar(self):
        """Reinicia os dados para um novo quiz."""
        self.pontuacao = 0
        self.acertos   = 0
        self.erros     = 0
        self.total     = 0

    def __repr__(self):
        return (
            f"<Jogador | Pontos: {self.pontuacao} | "
            f"Acertos: {self.acertos}/{self.total} | "
            f"{self.porcentagem:.1f}%>"
        )
