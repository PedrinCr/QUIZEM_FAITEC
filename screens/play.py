# screens/play.py — Tela de jogo

import customtkinter as ctk
from config import CORES, FONTES, SIMBOLOS   

class TelaPlay(ctk.CTkFrame):
    """
    Tela de jogo
    """

    def __init__(self, parent, ao_voltar=None):
        super().__init__(parent, fg_color=CORES["fundo"])
        self.ao_voltar = ao_voltar
        
        # ── SÍMBOLOS ESPALHADOS (background) ──────────────────────────────
        for simbolo, rx, ry, size in SIMBOLOS:
            ctk.CTkLabel(
                self, text=simbolo,
                font=("Segoe UI", size),
                text_color=CORES["primaria"],
                fg_color="transparent"
            ).place(relx=rx, rely=ry, anchor="center")


        # ── CONTEÚDO CENTRAL ──────────────────────────────────────────────
        centro = ctk.CTkFrame(self, fg_color="transparent")
        centro.place(relx=0.5, rely=0.5, anchor="center")


        ctk.CTkButton(
                centro, text="Voltar", font=FONTES["botao"],
                fg_color=CORES["card"], hover_color=CORES["primaria_hover"],
                text_color=CORES["texto"], width=288, height=50,
                corner_radius=10, command=self.voltar
            ).pack(pady=9)
    
    def voltar(self):
        """Volta para a tela de menu."""
        if self.ao_voltar:
            self.ao_voltar()
        
