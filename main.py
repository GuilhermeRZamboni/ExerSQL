#importar a biblioteca sqlite3
import sqlite3

#Cria uma conexão com o banco de dados chamado "biblioteca.db"
conexao = sqlite3.connect("biblioteca.db")

#Criar um objeto "cursor" server para executar os comandos SQL
cursor = conexao.cursor()

#Criar uma tabela no banco de dados
cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER,
    disponivel TEXT
    )
""")
print("Tabela criada com sucesso!")
#função para cadastrar livros
def cadastrar_livro():
    titulo = input("Digite o titulo do livro: ")
    autor = input("Digte o autor do livro: ")
    ano = int(input("Digite o ano de lançamento do livro: "))
    cursor.execute("""INSERT INTO biblioteca.db (titulo, autor, ano, disponivel)
                   VALUES (?, ?, ?, ?)
                   """, (titulo, autor, ano, "Sim"))
    conexao.commit()
#função para consultar livros
def consultar_livros():
    cursor.execute("SELECT * FROM livros")
    #fetchall traz todas as linhas da consulta
    for linha in cursor.fetchall():
        print(f"ID {linha[0]} | TITULO: {linha[1]} | AUTOR: {linha[2]} | ANO: {linha[3]} | DISPONIVEL: {linha[4]}")

