# 🧠 Transformada Wavelet — Iniciação Científica

Este projeto reúne códigos, estudos e materiais produzidos no contexto de uma Iniciação Científica sobre o uso da Transformada Wavelet no processamento de sinais, com ênfase na detecção de bordas em imagens de Ressonância Magnética (RM).

---
## 📦 Organização do Repositório
```text
📁 Documentos Institucionais/             # Relatórios e documentos formais da IC
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
│   └── 📁 Processamento_de_Imagens/       # Conteúdo da disciplina de Processamento de Imagens
│       ├── 📁 Biblioteca_my_image_lib/    # Versões de desenvolvimento da biblioteca
│       ├── 📁 Utilitarios/                 # Scripts úteis para a IC
│       └── 📁 Historico_Disciplina/        # Trabalhos e materiais originais da disciplina
│
📄 requirements.txt                        # Dependências do projeto
📄 README.md                               # Documentação principal
```

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

## 🧠 Objetivos da Pesquisa

> Esta iniciação científica tem como objetivo estudar a aplicação da Transformada Wavelet em sinais e imagens, explorando técnicas de denoising e thresholding, com foco em sinais de Ressonância Magnética.

---

## 🧑‍💻 Autor e Orientação

- **Autor:** Thiago Oliveira dos Santos  
- Iniciação Científica —- Instituto de Física de São Carlos (IFSC-USP)

- **Orientador:** Prof. Dr. Fernando Fernandes Paiva 
- Departamento de Física e Ciência Interdisciplinar — IFSC-USP

## 📄 Licença

Este projeto está licenciado sob a [MIT License](./LICENSE).
