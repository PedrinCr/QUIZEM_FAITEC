# main.py — Ponto de entrada do Quizem

import customtkinter as ctk
from config import APP_TITULO, APP_LARGURA, APP_ALTURA, APP_TEMA, CORES
from screens.menu import TelaMenu
from screens.play import TelaPlay


class Quizem(ctk.CTk):
    """
    Classe principal do aplicativo Quizem.
    Gerencia a janela principal e navegação entre telas.
    """

    def __init__(self):
        super().__init__()

        # ── Configurações da janela ────────────────────────────────────────
        
        self.title(APP_TITULO)
        self.geometry(f"{APP_LARGURA}x{APP_ALTURA}")
        
        # Centraliza a janela na tela
        self._centralizar_janela()
        
        # Define o tema (dark ou light)
        ctk.set_appearance_mode(APP_TEMA)
        
        # Define a cor padrão dos widgets
        ctk.set_default_color_theme("green")
        
        # Impede redimensionamento (opcional, pode remover depois)
        self.resizable(True, True)

        # ── Container principal ────────────────────────────────────────────
        
        # Frame que ocupará toda a janela
        self.container = ctk.CTkFrame(self, fg_color=CORES["fundo"])
        self.container.pack(fill="both", expand=True)

        # ── Exibe a tela inicial ───────────────────────────────────────────
        self.tela_atual = None
        self.mostrar_tela_menu()

    def _centralizar_janela(self):
        """Centraliza a janela no centro da tela do usuário."""
        self.update_idletasks()
        
        # Dimensões da tela
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        
        # Calcula posição central
        x = (largura_tela // 2) - (APP_LARGURA // 2)
        y = (altura_tela // 2) - (APP_ALTURA // 2)
        
        self.geometry(f"{APP_LARGURA}x{APP_ALTURA}+{x}+{y}")

    def mostrar_tela_menu(self):
        """Exibe a tela de menu inicial."""
        self.trocar_tela(TelaMenu(self.container, self.mostrar_tela_play))

    def mostrar_tela_play(self):
        """Exibe a tela de play."""
        self.trocar_tela(TelaPlay(self.container, self.mostrar_tela_menu))

    def trocar_tela(self, nova_tela):
        """Troca a tela atual."""
        if self.tela_atual:
            self.tela_atual.pack_forget()
            self.tela_atual.destroy()  # libera memória
        self.tela_atual = nova_tela
        self.tela_atual.pack(fill="both", expand=True)
        


# ── Execução do aplicativo ─────────────────────────────────────────────────

if __name__ == "__main__":
    app = Quizem()
    app.mainloop()
