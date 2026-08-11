# 🧪 Quizem: O conhecimento em jogo

Jogo educacional de Química para estudantes do Ensino Médio, desenvolvido em Python com interface gráfica moderna.

---

## 📋 Sobre o Projeto

O **Quizem** é um aplicativo/jogo educacional que combina:
- 📚 Aprendizagem de conceitos de Química
- 🎯 Quiz de múltipla escolha
- ⚡ Feedback imediato
- 🎮 Elementos de gamificação

**Público-alvo:** Estudantes do Ensino Médio  
**Disciplina:** Química

---

## 🎯 Funcionalidades (em desenvolvimento)

- [x] Tela de menu inicial
- [ ] Seleção de conteúdos por submatéria
- [ ] Quiz interativo com feedback visual
- [ ] Sistema de pontuação
- [ ] Modo aleatório (perguntas mescladas)
- [ ] Acompanhamento de progresso
- [ ] Persistência de dados local (JSON)

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **CustomTkinter** - Interface gráfica moderna
- **JSON** - Armazenamento de progresso

---

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/PedrinCr/QUIZEM_FAITEC.git
cd QUIZEM_FAITEC
```

### 2. Instale as dependências

```bash
pip install customtkinter
```

---

## ▶️ Como Executar

```bash
python main.py
```

A janela do aplicativo será aberta com a tela de menu inicial.

---

## 📂 Estrutura do Projeto

```
QUIZEM_FAITEC/
├── main.py                    # Ponto de entrada do app
├── config.py                  # Configurações (cores, fontes, pontuação)
│
├── data/
│   └── questoes.py           # Banco de questões (a preencher)
│
├── models/
│   ├── questao.py            # Classe Questao
│   └── jogador.py            # Classe Jogador
│
├── screens/
│   └── menu.py               # Tela de menu inicial ✅
│   # (outras telas em desenvolvimento)
│
├── services/
│   ├── quiz_service.py       # Lógica do quiz
│   └── progresso_service.py  # Gerenciamento de progresso
│
└── README.md
```

---

## 🎨 Paleta de Cores

- **Primária:** Azul `#2563EB`
- **Secundária:** Roxo `#7C3AED`
- **Acerto:** Verde `#16A34A`
- **Erro:** Vermelho `#DC2626`
- **Fundo:** Escuro `#1E1E2E`

---

## 🎓 Desenvolvimento Acadêmico

Este é um **projeto acadêmico** da FAITEC, desenvolvido com foco em:
- Código simples e didático
- Estrutura organizada e escalável
- Facilidade de manutenção

---

## 📝 Status Atual

**Versão:** 1.0 (em desenvolvimento)  
**Última atualização:** Agosto 2026

### ✅ Concluído
- Estrutura base do projeto
- Sistema de configuração
- Modelos de dados (Questao, Jogador)
- Serviços (quiz, progresso)
- Tela de menu inicial com visual moderno

### 🚧 Em Desenvolvimento
- Telas de conteúdos, quiz e resultado
- Banco de questões
- Sistema de navegação entre telas

---

## 👥 Contribuindo

Este é um projeto acadêmico. Pull Requests são bem-vindos!

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'feat: adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

---

## 📄 Licença

Projeto acadêmico - FAITEC © 2026

---

## 📧 Contato

**Desenvolvedor:** Pedro Costa (PedrinCr)  
**Instituição:** FAITEC  
**Repositório:** [github.com/PedrinCr/QUIZEM_FAITEC](https://github.com/PedrinCr/QUIZEM_FAITEC)
