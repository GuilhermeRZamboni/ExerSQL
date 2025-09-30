# 📚 Biblioteca - Streamlit + SQLite

Este repositório contém uma aplicação simples para **gerenciamento de livros** utilizando **Streamlit** como interface web e **SQLite** como banco de dados local.

---

## 🚀 Funcionalidades

- Listar todos os livros cadastrados
- Cadastrar novos livros
- Alterar a disponibilidade de um livro (sim / não)
- Excluir livros do banco de dados

---

## 🛠️ Tecnologias utilizadas

- Python 3
- Streamlit
- SQLite3

---

## 📦 Requisitos

- Python 3.7 ou superior
- Instalar dependências:

```bash
pip install -r requirements.txt
```

---

## ▶️ Como executar

1. Clone o repositório (ou extraia os arquivos enviados):
```bash
git clone https://github.com/GuilhermeRZamboni/ExerSQL.git
cd ExerSQL
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o app Streamlit:
```bash
streamlit run app.py
```

> Observação: certifique-se de que o arquivo `biblioteca.db` está presente na pasta do projeto. Se não existir, crie o banco ou execute o script que cria a tabela `livros`.

---

## 🗃️ Estrutura do banco de dados (tabela `livros`)

```sql
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER NOT NULL,
    disponivel TEXT DEFAULT 'sim'
);
```

---

## 📂 Arquivos principais

- `main.py` — Lógica do aplicativo (funções para cadastrar, consultar, alterar disponibilidade e remover livros).
- `app.py` — Inicializa o banco (caso necessário) e chama o menu da aplicação.
- `biblioteca.db` — Banco SQLite usado pela aplicação.
- `requirements.txt` — Dependências do projeto.

---

## ✅ Boas práticas e dicas

- Faça backup do arquivo `biblioteca.db` antes de testar operações que removam dados.
- Para adicionar novos campos (categoria, descrição), atualize o esquema do banco e as funções de CRUD no `main.py`.
- Considere adicionar validação mais robusta para entradas do usuário (por exemplo: ano entre 1000 e o ano atual).

---

## 🐛 Possíveis melhorias

- Paginação e busca por título/autor
- Filtro por disponibilidade
- Testes automatizados (unitários)
- Exportar/Importar dados (CSV/Excel)
- Interface visual mais elaborada com componentes customizados

---

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT**. Veja o arquivo `LICENSE` para o texto completo em português.

---

## 🙋‍♂️ Autor

Feito com 💻 por **Guilherme Zamboni** — contribuições são bem-vindas!