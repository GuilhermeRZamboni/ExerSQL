#importar a biblioteca sqlite3
import sqlite3

#Cria uma conexão com o banco de dados chamado "escola.db"
conexao = sqlite3.connect("biblioteca.db")

#Criar um objeto "cursor" server para executar os comandos SQL
cursor = conexao.cursor()

#Criar uma tabela no banco de dados
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER,
    disponivel TEXT
    )
""")
print("Tabela criada com sucesso!")

def cadastrar_livro():
    titulo = input("Digite o titulo do livro: ")
    autor = input("Digte o autor do livro: ")
    ano = int(input("Digite o ano de lançamento do livro: "))
    cursor.execute("""INSERT INTO biblioteca.db (titulo, autor, ano, disponivel)
                   VALUES (?, ?, ?, ?)
                   """, (titulo, autor, ano, "Sim"))


