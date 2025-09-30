📚 Biblioteca com Streamlit + SQLite

Este projeto é uma aplicação simples de gerenciamento de livros utilizando Streamlit
 como interface web e SQLite como banco de dados local.

🚀 Funcionalidades

📄 Listar todos os livros cadastrados

➕ Cadastrar novos livros

🔄 Alterar a disponibilidade de um livro

❌ Excluir livros do banco de dados

🛠️ Tecnologias utilizadas

Python 3

Streamlit

SQLite3

📦 Requisitos

Python 3.7+

Streamlit instalado:

pip install -r

▶️ Como executar

Clone o repositório:

git clone https://github.com/GuilhermeRZamboni/ExerSQL.git
cd ExerSQL


Execute o app com Streamlit:

streamlit run app.py


Certifique-se de que o arquivo biblioteca.db exista com a tabela livros. Se necessário, crie manualmente ou adicione um script de criação.

🗃️ Estrutura do banco de dados

A tabela livros deve conter os seguintes campos:

CREATE TABLE livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER NOT NULL,
    disponivel TEXT DEFAULT 'sim'
);

📂 Funcionalidades do código
cadastrar_livro()

Permite o cadastro de um novo livro com título, autor e ano de lançamento.

consultar_livros()

Exibe uma tabela com todos os livros cadastrados e seus status de disponibilidade.

alterar_disponibilidade()

Permite alternar o status de disponibilidade de um livro (sim ↔ não).

remover_livros()

Permite excluir permanentemente um livro do banco de dados.

obter_ids()

Auxiliar para retornar todos os IDs existentes na tabela de livros.

menu()

Controla a navegação entre as funcionalidades no menu lateral do Streamlit.

✅ Exemplo visual

📌 Interface simples usando a barra lateral para navegar entre ações:

Exemplo de cadastro de livro com validações

Exibição de livros com coloração condicional para disponibilidade

Atualização automática da base ao realizar ações

🐛 Possíveis melhorias

Adicionar campo de categoria/descrição para os livros

Melhorar o tratamento de erros

Adicionar paginação ou busca por título

Criar testes unitários

Exportar dados para CSV/Excel

📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE
 para mais detalhes.

🙋‍♂️ Autor

Feito com 💻 por Guilherme Zamboni
 — contribuições são bem-vindas!