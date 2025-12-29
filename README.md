# PJ Docs

O **PJ Docs** é uma aplicação desktop desenvolvida em Python para a catalogação de documentos vinculados aos procedimentos da Promotoria de Justiça. 

O sistema usa IA Generativa para identificar assuntos e criar resumos automáticos dos registros.

## 🚀 Funcionalidades

* **Cadastro de Procedimentos:** Interface para registrar novos procedimentos com suas respectivas descrições.
* **Processamento de Arquivos:** Suporte para carregamento de documentos nos formatos `.pdf`, `.docx` e `.txt`.
* **Resumo Automático:** Integração com funções utilitárias para gerar títulos e resumos automáticos do conteúdo carregado.
* **Banco de Dados:** Persistência de dados utilizando SQLite para armazenar documentos e procedimentos.
* **Visualização e Filtros:** Tabela interativa para visualização dos registros com filtros por número de procedimento.
* **Relatórios:** Exportação de relatórios baseados na visão atual da tabela (dados filtrados).

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Interface Gráfica (GUI):** PySide6 (Qt for Python)
* **Banco de Dados:** SQLite
* **Estilo de Interface:** Fusion

## 📂 Estrutura de Pastas

Para o funcionamento correto, o projeto deve seguir esta estrutura:

```text
/
├── main.py                # Arquivo principal 
├── ui/
│   ├── tela_principal.py  # Interface gerada pelo Qt Designer
│   └── tela_cadastro.py   # Interface de diálogo de cadastro
├── utils.py               # Funções gerar_titulo_e_resumo e exportar_relatorio
└── data/
    └── pj_docs.db         # Banco de dados SQLite