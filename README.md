# 🧠 Transformada Wavelet — Iniciação Científica

Este projeto reúne códigos, estudos e materiais produzidos no contexto de uma Iniciação Científica sobre o uso da Transformada Wavelet no processamento de sinais, com ênfase em aplicações em Ressonância Magnética (RM).

---

# 📂 Estrutura do Projeto

📁 Documentos Institucionais/              # Relatórios e documentos formais da IC
│   ├── 📁 Materiais Produzidos/           # Relatórios e apresentações produzidos
│   └── 📁 Relatórios/                     # Relatórios detalhados (parte prática e teórica)
│
📁 Material/                               # Referências teóricas e artigos utilizados
│   ├── 📁 Aplicações Biomédicas/
│   ├── 📁 Imagens por Ressonância Magnética Funcional (fMRI)/
│   ├── 📁 Instrumentação e Aquisição de Dados/
│   ├── 📁 Transformada Wavelet - Conceitos Básicos/
│   ├── 📁 Técnicas de Thresholding e Remoção de Ruído/
│   └── 📁 Wavelets Complexas e Multidimensionais/
│
📁 Trabalho/                               # Implementações práticas e códigos
│   ├── 📁 Problemas/                      # Evolução do projeto principal
│   │   ├── 📁 1_Simulacao_Sinal_FT/       # Fourier e simulação de S(t)
│   │   ├── 📁 2_Sinais_Multiplas_Fontes/  # Sinais com múltiplas fontes
│   │   ├── 📁 3_Sinais_Imagens_Ruido/     # Inclusão de imagens e ruído gaussiano
│   │   └── 📁 4_Implementacao_Wavelet/    # Wavelet 1D e 2D
│   │
│   └── 📁 Processamento_de_Imagens/       # Histórico e recursos da disciplina
│       ├── 📁 Biblioteca_my_image_lib/    # Versões antigas da biblioteca
│       ├── 📁 codigos_auxiliares/         # Scripts utilitários
│       ├── 📁 Materiais_de_apoio/         # Aulas, artigos e atividades
│       └── 📁 Trabalhos/                  # Trabalhos originais da disciplina
│
📄 requirements.txt                        # Dependências do projeto
📄 README.md                               # Documentação principal


## ⚙️ Requisitos

Instale os pacotes necessários com:

```bash
pip install -r requirements.txt
```

---

## ▶️ Como Executar

Execute o menu interativo com:

```bash
python main.py
```

Você poderá escolher/simular sinais, aplicar transformadas (Fourier ou Wavelet), adicionar ruído e visualizar os resultados.

---

## 📘 Documentação

- Todos os relatórios produzidos estão em [`Documentos_Institucionais/`](./Documentos_Institucionais)
- A biblioteca wavelet usada no projeto está em [`useful_lib.py`](./useful_lib.py)
- As versões da biblioteca `my_image_lib` usadas na disciplina estão em [`Trabalho/Processamento_de_Imagens/Biblioteca_my_image_lib`](./Trabalho/Processamento_de_Imagens/Biblioteca_my_image_lib)

---

## 📎 Materiais de Estudo

Os materiais teóricos e artigos utilizados durante a pesquisa estão em [`Material/`](./Material/).

---

## 🧠 Objetivos da Pesquisa

> Esta iniciação científica tem como objetivo estudar a aplicação da Transformada Wavelet em sinais simulados e imagens, explorando técnicas de denoising, thresholding e compressão, com foco em sinais de Ressonância Magnética.

---

## 🧑‍💻 Autor

- **Thiago Oliveira dos Santos**  
  Iniciação Científica — Instituto de Física de São Carlos (IFSC-USP)

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](./LICENSE).
