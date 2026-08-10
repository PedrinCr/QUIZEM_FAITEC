# config.py — Configurações globais do Quizem

APP_TITULO = "Quizem: O conhecimento em jogo"
APP_LARGURA = 900
APP_ALTURA = 650
APP_TEMA = "dark"  # "dark" ou "light"

# Paleta de cores
CORES = {
    "primaria":       "#2563EB",  # azul principal
    "primaria_hover": "#1D4ED8",
    "secundaria":     "#7C3AED",  # roxo
    "acerto":         "#16A34A",  # verde
    "erro":           "#DC2626",  # vermelho
    "fundo":          "#1E1E2E",  # fundo escuro
    "card":           "#2A2A3E",  # cartões
    "texto":          "#F1F5F9",  # texto claro
    "texto_secundario": "#94A3B8",
    "borda":          "#3F3F5A",
    "amarelo":        "#F59E0B",  # bônus/destaque
}

# Fontes
FONTES = {
    "titulo":     ("Segoe UI", 28, "bold"),
    "subtitulo":  ("Segoe UI", 18, "bold"),
    "corpo":      ("Segoe UI", 13),
    "corpo_bold": ("Segoe UI", 13, "bold"),
    "pequena":    ("Segoe UI", 11),
    "botao":      ("Segoe UI", 13, "bold"),
}

# Pontuação
PONTOS_ACERTO = 100
PONTOS_ERRO = 0
BONUS_DESEMPENHO = {
    100: 500,  # 100% de aproveitamento → +500
    80:  200,  # ≥ 80%                  → +200
    60:  100,  # ≥ 60%                  → +100
    0:   0,    # abaixo de 60%          → +0
}

# Arquivo de progresso
ARQUIVO_PROGRESSO = "progresso.json"
