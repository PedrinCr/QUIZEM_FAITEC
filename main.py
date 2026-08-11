# main.py — Ponto de entrada do Quizem

import customtkinter as ctk
from config import APP_TITULO, APP_LARGURA, APP_ALTURA, APP_TEMA, CORES
from screens.menu import TelaMenu


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
        ctk.set_default_color_theme("blue")
        
        # Impede redimensionamento (opcional, pode remover depois)
        self.resizable(False, False)

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
        # Remove a tela atual, se existir
        if self.tela_atual:
            self.tela_atual.pack_forget()
        
        # Cria e exibe a nova tela
        self.tela_atual = TelaMenu(self.container)
        self.tela_atual.pack(fill="both", expand=True)

    # TODO: Adicionar métodos para navegar para outras telas
    # def mostrar_tela_conteudos(self):
    # def mostrar_tela_quiz(self):
    # def mostrar_tela_resultado(self):
    # etc.


# ── Execução do aplicativo ─────────────────────────────────────────────────

if __name__ == "__main__":
    app = Quizem()
    app.mainloop()
