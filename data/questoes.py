# data/questoes.py — Banco de questões do Quizem
#
# INSTRUÇÕES PARA PREENCHIMENTO:
#
# Cada submatéria é uma chave do dicionário QUESTOES.
# Cada submatéria contém um dicionário de conteúdos.
# Cada conteúdo é um dict com:
#   - "titulo":      nome exibido na tela
#   - "explicacao":  texto resumido exibido antes do quiz
#   - "questoes":    lista de dicts com as perguntas
#
# Formato de cada questão:
#   {
#       "pergunta":     "Enunciado da questão",
#       "alternativas": ["A) ...", "B) ...", "C) ...", "D) ..."],
#       "correta":      0,           # índice (0=A, 1=B, 2=C, 3=D)
#       "explicacao":   "Justificativa da resposta correta.",
#       "dificuldade":  "facil",     # "facil" | "medio" | "dificil"
#   }

QUESTOES = {

    "Estequiometria": {
        "Balanceamento de Equações": {
            "titulo":     "Balanceamento de Equações",
            "explicacao": (
                "Balancear uma equação química significa igualar o número de átomos "
                "de cada elemento nos reagentes e nos produtos, respeitando a Lei de "
                "Lavoisier (conservação da massa)."
            ),
            "questoes": [
                # Adicione as questões aqui
            ],
        },
        "Mol e Massa Molar": {
            "titulo":     "Mol e Massa Molar",
            "explicacao": (
                "O mol é a unidade de medida da quantidade de matéria. "
                "1 mol de qualquer substância contém 6,022 × 10²³ partículas "
                "(Número de Avogadro). A massa molar (g/mol) é numericamente "
                "igual à massa atômica ou molecular da substância."
            ),
            "questoes": [
                # Adicione as questões aqui
            ],
        },
        "Cálculos Estequiométricos": {
            "titulo":     "Cálculos Estequiométricos",
            "explicacao": (
                "Os cálculos estequiométricos permitem determinar as quantidades "
                "de reagentes e produtos em uma reação, usando as proporções "
                "indicadas pelos coeficientes da equação balanceada."
            ),
            "questoes": [
                # Adicione as questões aqui
            ],
        },
    },

    "Ligações Químicas": {
        "Ligação Iônica": {
            "titulo":     "Ligação Iônica",
            "explicacao": (
                "A ligação iônica ocorre pela transferência de elétrons entre "
                "átomos de metais e não-metais, formando íons com cargas opostas "
                "que se atraem eletrostaticamente."
            ),
            "questoes": [],
        },
        "Ligação Covalente": {
            "titulo":     "Ligação Covalente",
            "explicacao": (
                "A ligação covalente ocorre pelo compartilhamento de pares de "
                "elétrons entre não-metais. Pode ser simples, dupla ou tripla, "
                "dependendo do número de pares compartilhados."
            ),
            "questoes": [],
        },
        "Ligação Metálica": {
            "titulo":     "Ligação Metálica",
            "explicacao": (
                "A ligação metálica ocorre em metais, onde elétrons livres "
                "(mar de elétrons) circulam entre os cátions metálicos, "
                "conferindo propriedades como condutividade e maleabilidade."
            ),
            "questoes": [],
        },
    },

    "Funções Inorgânicas": {
        "Ácidos": {
            "titulo":     "Ácidos",
            "explicacao": (
                "Segundo Arrhenius, ácidos são substâncias que em solução aquosa "
                "liberam H⁺ como único cátion. São caracterizados pelo pH < 7 "
                "e pela capacidade de reagir com metais, bases e óxidos."
            ),
            "questoes": [],
        },
        "Bases": {
            "titulo":     "Bases",
            "explicacao": (
                "Segundo Arrhenius, bases são substâncias que em solução aquosa "
                "liberam OH⁻ como único ânion. Possuem pH > 7, sabor amargo "
                "e textura escorregadia."
            ),
            "questoes": [],
        },
        "Sais": {
            "titulo":     "Sais",
            "explicacao": (
                "Sais são compostos iônicos formados pela reação de neutralização "
                "entre um ácido e uma base. Possuem cátion diferente de H⁺ e "
                "ânion diferente de OH⁻."
            ),
            "questoes": [],
        },
        "Óxidos": {
            "titulo":     "Óxidos",
            "explicacao": (
                "Óxidos são compostos binários formados por oxigênio e outro "
                "elemento. Classificam-se em ácidos, básicos, anfóteros, neutros "
                "e mistos, conforme sua reação com água, ácidos ou bases."
            ),
            "questoes": [],
        },
    },

    "Soluções": {
        "Concentração e Molaridade": {
            "titulo":     "Concentração e Molaridade",
            "explicacao": (
                "A concentração comum (g/L) indica a massa de soluto por litro "
                "de solução. A molaridade (mol/L) indica o número de mols de "
                "soluto por litro de solução."
            ),
            "questoes": [],
        },
        "Diluição e Mistura": {
            "titulo":     "Diluição e Mistura",
            "explicacao": (
                "Na diluição, adiciona-se solvente à solução, mantendo a "
                "quantidade de soluto constante (C₁V₁ = C₂V₂). Na mistura, "
                "combinam-se soluções de diferentes concentrações."
            ),
            "questoes": [],
        },
    },

    "Termoquímica": {
        "Entalpia e Calor de Reação": {
            "titulo":     "Entalpia e Calor de Reação",
            "explicacao": (
                "A entalpia (H) representa o conteúdo energético de uma substância. "
                "A variação de entalpia (ΔH) indica se uma reação é exotérmica "
                "(ΔH < 0, libera calor) ou endotérmica (ΔH > 0, absorve calor)."
            ),
            "questoes": [],
        },
        "Lei de Hess": {
            "titulo":     "Lei de Hess",
            "explicacao": (
                "A Lei de Hess afirma que a variação de entalpia de uma reação "
                "é a mesma, independentemente do caminho percorrido. Isso permite "
                "calcular ΔH de reações a partir de equações intermediárias."
            ),
            "questoes": [],
        },
    },

    "Química Orgânica": {
        "Hidrocarbonetos": {
            "titulo":     "Hidrocarbonetos",
            "explicacao": (
                "Hidrocarbonetos são compostos orgânicos formados apenas por "
                "carbono e hidrogênio. Incluem alcanos (ligações simples), "
                "alcenos (dupla), alcinos (tripla) e aromáticos (anel benzênico)."
            ),
            "questoes": [],
        },
        "Funções Oxigenadas": {
            "titulo":     "Funções Oxigenadas",
            "explicacao": (
                "Funções oxigenadas possuem oxigênio em sua estrutura. "
                "Exemplos: álcoois (-OH), aldeídos (-CHO), cetonas (C=O), "
                "ácidos carboxílicos (-COOH) e ésteres (-COO-)."
            ),
            "questoes": [],
        },
        "Isomeria": {
            "titulo":     "Isomeria",
            "explicacao": (
                "Isômeros são compostos com a mesma fórmula molecular, mas "
                "estruturas diferentes. Divide-se em isomeria plana (constitucional) "
                "e isomeria espacial (estereoisomeria)."
            ),
            "questoes": [],
        },
    },

    "Eletroquímica": {
        "Pilhas e Células Galvânicas": {
            "titulo":     "Pilhas e Células Galvânicas",
            "explicacao": (
                "Pilhas convertem energia química em energia elétrica por meio de "
                "reações de oxirredução espontâneas. O eletrodo negativo é o ânodo "
                "(oxidação) e o positivo é o cátodo (redução)."
            ),
            "questoes": [],
        },
        "Eletrólise": {
            "titulo":     "Eletrólise",
            "explicacao": (
                "A eletrólise é uma reação de oxirredução não-espontânea, "
                "forçada por corrente elétrica externa. É utilizada na galvanoplastia, "
                "produção de cloro, alumínio e hidrogênio."
            ),
            "questoes": [],
        },
        "Potencial de Redução": {
            "titulo":     "Potencial de Redução",
            "explicacao": (
                "O potencial de redução (E°) indica a tendência de uma espécie "
                "em ganhar elétrons. O potencial de célula é calculado por "
                "E°célula = E°cátodo − E°ânodo. Valores positivos indicam reação espontânea."
            ),
            "questoes": [],
        },
    },
}
