# screens/play.py — Tela de jogo

import customtkinter as ctk
from config import CORES, FONTES

class TelaPlay(ctk.CTkFrame):
    """
    Tela de jogo
    """

    def __init__(self, parent, ao_voltar=None):
        super().__init__(parent, fg_color=CORES["fundo"])

        self.ao_voltar = ao_voltar

        self.grid_rowconfigure(0, weight=1) # Espaço superior
        self.grid_rowconfigure(1, weight=0) # Título
        self.grid_rowconfigure(2, weight=1) # Opções
        self.grid_rowconfigure(3, weight=0) # Espaço inferior
        self.grid_columnconfigure(0, weight=1)

        self.icone = ctk.CTkLabel(
            self,
            text="🧪",
            font=("Segoe UI", 80),
            text_color=CORES["primaria"]
        )
        self.icone.grid(row=1, column=0, pady=(40, 10))

        # Título principal
        self.titulo = ctk.CTkLabel(
            self,
            text="QUIZEM",
            font=FONTES["titulo"],
            text_color=CORES["texto"]
        )
        self.titulo.grid(row=2, column=0, pady=(0, 5))

        # Subtítulo
        self.subtitulo = ctk.CTkLabel(
            self,
            text="O conhecimento em jogo",
            font=FONTES["corpo"],
            text_color=CORES["texto_secundario"]
        )
        self.subtitulo.grid(row=3, column=0, pady=(45, 30))

        #Botao de voltar
        self.botao_voltar = ctk.CTkButton(
            self,
            text="Voltar",
            font=FONTES["botao"],
            fg_color=CORES["primaria"],
            hover_color=CORES["primaria_hover"],
            text_color=CORES["texto"],
            command=self.voltar
        )
        self.botao_voltar.grid(row=4, column=0, pady=(0, 40))
    
    def voltar(self):
        """Volta para a tela de menu."""
        if self.ao_voltar:
            self.ao_voltar()
        
