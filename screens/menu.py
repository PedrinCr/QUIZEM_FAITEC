# screens/menu.py — Tela inicial do Quizem

import customtkinter as ctk
from config import CORES, FONTES, SIMBOLOS


class TelaMenu(ctk.CTkFrame):

    def __init__(self, parent, ao_comecar=None, ao_conteudos=None, ao_progresso=None):
        super().__init__(parent, fg_color=CORES["fundo"])
        self.ao_comecar = ao_comecar
        self.ao_conteudos = ao_conteudos
        self.ao_progresso = ao_progresso

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

        ctk.CTkLabel(centro, text="🧪", font=("Segoe UI", 90), text_color=CORES["primaria"]).pack()
        ctk.CTkLabel(centro, text="QUIzEM", font=FONTES["titulo"], text_color=CORES["texto"]).pack(pady=(0, 9))
        ctk.CTkLabel(centro, text="O conhecimento em jogo", font=FONTES["corpo"], text_color=CORES["texto_secundario"]).pack(pady=(0, 36))

        for texto, cmd, hover in [
            ("▶  Começar",        self.ao_clicar_comecar,   CORES["primaria_hover"]),
            ("📚  Conteúdos",     self.ao_clicar_conteudos, CORES["primaria"]),
            ("📊  Meu Progresso", self.ao_clicar_progresso, CORES["primaria"]),
        ]:
            ctk.CTkButton(
                centro, text=texto, font=FONTES["botao"],
                fg_color=CORES["card"], hover_color=hover,
                text_color=CORES["texto"], width=288, height=50,
                corner_radius=10, command=cmd
            ).pack(pady=9)

        ctk.CTkButton(
            centro, text="✕  Sair", font=FONTES["corpo"],
            fg_color="transparent", hover_color=CORES["erro"],
            text_color=CORES["texto_secundario"], width=288, height=41,
            corner_radius=10, border_width=1, border_color=CORES["borda"],
            command=self.ao_clicar_sair
        ).pack(pady=18)

        # ── RODAPÉ ─────────────────────────────────────────────────────────
        ctk.CTkLabel(
            self, text="Versão 1.0 • Projeto Acadêmico FAITEC",
            font=FONTES["pequena"], text_color=CORES["texto_secundario"]
        ).place(relx=0.5, rely=1.0, anchor="s", y=-15)

    # ── AÇÕES ──────────────────────────────────────────────────────────────

    def ao_clicar_comecar(self):
        if self.ao_comecar:
            self.ao_comecar()

    def ao_clicar_conteudos(self):
        if self.ao_conteudos:
            self.ao_conteudos()

    def ao_clicar_progresso(self):
        if self.ao_progresso:
            self.ao_progresso()

    def ao_clicar_sair(self):
        self.master.quit()
