# models/questao.py — Modelo de dados de uma questão

class Questao:
    """Representa uma questão do quiz."""

    def __init__(self, dados: dict):
        self.pergunta:     str       = dados["pergunta"]
        self.alternativas: list[str] = dados["alternativas"]
        self.correta:      int       = dados["correta"]       # índice da alternativa correta
        self.explicacao:   str       = dados["explicacao"]
        self.dificuldade:  str       = dados.get("dificuldade", "medio")  # facil | medio | dificil
        self.conteudo:     str       = dados.get("conteudo", "")
        self.submateria:   str       = dados.get("submateria", "")

    def verificar_resposta(self, indice_escolhido: int) -> bool:
        """Retorna True se a alternativa escolhida está correta."""
        return indice_escolhido == self.correta

    def __repr__(self):
        return f"<Questao: {self.pergunta[:50]}...>"
