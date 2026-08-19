# screens/menu.py — Tela inicial do Quizem

import customtkinter as ctk
from config import CORES, FONTES


class TelaMenu(ctk.CTkFrame):
    """
    Tela inicial do jogo com logo e botões principais.
    """

    def __init__(self, parent, ao_comecar = None):
        super().__init__(parent, fg_color=CORES["fundo"])
        self.ao_comecar = ao_comecar

        # Configura o grid para centralizar tudo
        self.grid_rowconfigure(0, weight=1)  # Espaço superior
        self.grid_rowconfigure(1, weight=0)  # Logo
        self.grid_rowconfigure(2, weight=0)  # Subtítulo
        self.grid_rowconfigure(3, weight=0)  # Botões
        self.grid_rowconfigure(4, weight=1)  # Espaço inferior
        self.grid_columnconfigure(0, weight=1)

        # ── LOGO / TÍTULO ──────────────────────────────────────────────────
        
        # Ícone emoji de química (tubo de ensaio)
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
            text="QUIzEM",
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

        # ── BOTÕES ─────────────────────────────────────────────────────────

        # Container para os botões (centralizado)
        self.container_botoes = ctk.CTkFrame(self, fg_color="transparent")
        self.container_botoes.grid(row=4, column=0, pady=20)

        # Botão: Começar (destaque principal)
        self.btn_comecar = ctk.CTkButton(
            self.container_botoes,
            text="▶  Começar",
            font=FONTES["botao"],
            fg_color=CORES["card"],
            hover_color=CORES["primaria_hover"],
            width=300,
            height=50,
            corner_radius=10,
            command=self.ao_clicar_comecar
        )
        self.btn_comecar.pack(pady=8)

        # Botão: Conteúdos
        self.btn_conteudos = ctk.CTkButton(
            self.container_botoes,
            text="📚  Conteúdos",
            font=FONTES["botao"],
            fg_color=CORES["card"],
            hover_color=CORES["primaria"],
            text_color=CORES["texto"],
            width=300,
            height=50,
            corner_radius=10,
            command=self.ao_clicar_conteudos
        )
        self.btn_conteudos.pack(pady=8)

        # Botão: Meu Progresso
        self.btn_progresso = ctk.CTkButton(
            self.container_botoes,
            text="📊  Meu Progresso",
            font=FONTES["botao"],
            fg_color=CORES["card"],
            hover_color=CORES["primaria"],
            text_color=CORES["texto"],
            width=300,
            height=50,
            corner_radius=10,
            command=self.ao_clicar_progresso
        )
        self.btn_progresso.pack(pady=8)

        # Botão: Sair
        self.btn_sair = ctk.CTkButton(
            self.container_botoes,
            text="✕  Sair",
            font=FONTES["corpo"],
            fg_color="transparent",
            hover_color=CORES["erro"],
            text_color=CORES["texto_secundario"],
            width=300,
            height=40,
            corner_radius=10,
            border_width=1,
            border_color=CORES["borda"],
            command=self.ao_clicar_sair
        )
        self.btn_sair.pack(pady=15)

        # ── RODAPÉ ─────────────────────────────────────────────────────────

        # Versão / créditos
        self.rodape = ctk.CTkLabel(
            self,
            text="Versão 1.0 • Projeto Acadêmico FAITEC",
            font=FONTES["pequena"],
            text_color=CORES["texto_secundario"]
        )
        self.rodape.grid(row=5, column=0, sticky="s", pady=20)

    # ── FUNÇÕES DOS BOTÕES ─────────────────────────────────────────────────

    def ao_clicar_comecar(self):
        """Ação ao clicar no botão 'Começar'."""
        print("🎮 Botão 'Começar' clicado!")
        if self.ao_comecar:
            self.ao_comecar()

    def ao_clicar_conteudos(self):
        """Ação ao clicar no botão 'Conteúdos'."""
        print("📚 Botão 'Conteúdos' clicado!")
        # TODO: Navegar para a tela de conteúdos

    def ao_clicar_progresso(self):
        """Ação ao clicar no botão 'Meu Progresso'."""
        print("📊 Botão 'Progresso' clicado!")
        # TODO: Navegar para a tela de progresso

    def ao_clicar_sair(self):
        """Ação ao clicar no botão 'Sair'."""
        print("✕ Saindo do jogo...")
        self.master.quit()  # Fecha a aplicação
