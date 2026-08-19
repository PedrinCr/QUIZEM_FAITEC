# screens/progresso.py — Tela de progresso do usuário

import customtkinter as ctk
from config import CORES, FONTES, ARQUIVO_PROGRESSO

class TelaProgresso(ctk.CTkFrame):
    """
    Tela de progresso do usuário
    """

    def __init__(self, parent):
        super().__init__(parent, fg_color=CORES["fundo"])
