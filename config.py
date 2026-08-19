# config.py — Configurações globais do Quizem

APP_TITULO = "Quizem: O conhecimento em jogo"
APP_LARGURA = 1280
APP_ALTURA = 720
APP_TEMA = "dark"  # "dark" ou "light"

# Paleta de cores
CORES = {
    "primaria":       "#46f06d",  # verde principal
    "primaria_hover": "#46f06d",
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
# Tente diferentes variações do nome da fonte Nasalization
FONTES = {
    "titulo":     ("Nasalization", 32, "bold"),
    "subtitulo":  ("Nasalization", 20, "bold"),
    "corpo":      ("Nasalization", 16),
    "corpo_bold": ("Nasalization", 16, "bold"),
    "pequena":    ("Nasalization", 14),
    "botao":      ("Nasalization", 16, "bold"),
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
