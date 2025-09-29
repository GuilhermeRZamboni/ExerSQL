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
    try:
        titulo = input("Digite o titulo do livro: ")
        autor = input("Digte o autor do livro: ")
        ano = int(input("Digite o ano de lançamento do livro: "))
        cursor.execute("""INSERT INTO livros (titulo, autor, ano, disponivel)
                    VALUES (?, ?, ?, ?)
                    """, (titulo, autor, ano, "sim",))
        conexao.commit()
        print("Livro cadastrado com sucesso!")
    except Exception as erro:
        print(f"Não foi possivel cadastrar o livro, Erro: {erro}")
#função para consultar livros
def consultar_livros():
    cursor.execute("SELECT * FROM livros")
    #fetchall traz todas as linhas da consulta
    livros = cursor.fetchall()
    if len(livros) > 0:
        for linha in livros:
            print(f"ID {linha[0]} | TITULO: {linha[1]} | AUTOR: {linha[2]} | ANO: {linha[3]} | DISPONIVEL: {linha[4]}")
        conexao.commit()
    else:
        print("Nenhum livro cadastrado!")
def alterar_disponibilidade():
    consultar_livros()
    try:
        id = int(input("Digite qual ID você deseja alterar a disponibilidade: "))
        cursor.execute("SELECT disponivel FROM livros WHERE id = ?", (id,))
        resultado = cursor.fetchone()
        if resultado is None:
            print("ID não encontrado.")
            return
        if resultado[0] == "sim":
            cursor.execute("""
                UPDATE livros
                SET disponivel = ?
                WHERE id = ?
            """, ("não", id))
        else:
            cursor.execute("""
                UPDATE livros
                SET disponivel = ?
                WHERE id = ?
            """, ("sim", id))
        conexao.commit()
        print("Disponibilidade alterada")
    except Exception as erro:
        print(f"Erro ao alterar a disponibilidade, Erro: {erro}")

def remover_livros():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()
       
        id_livro = int(input("Digite o id do livro que deseja deletar: "))
        cursor.execute("DELETE FROM livros WHERE id = ?", (id_livro,))
        conexao.commit()
       
        #Verificar se o livro foi realmente deletado
        if cursor.rowcount > 0:
            print("livro removido com sucesso!")
        else:
            print("Nenhum livro cadastrado com o ID fornecido")
    except Exception as erro:
        print(f"Erro ao tentar excluir o aluno {erro}")
    finally:
        #Sempre fecha a conexão, com sucesso ou erro
        if conexao:
            conexao.close()

def menu():
    while True:
        print("-----------MENU------------\n1-Consultar Livros\n2-Cadastrar Livros\n3-Excluir Livro\n4-Alterar Disponibilidade\n5-Sair ")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            consultar_livros()
        elif opcao == 2:
            cadastrar_livro()
        elif opcao == 3:
            remover_livros()
        elif opcao == 4:
            alterar_disponibilidade()
        elif opcao == 5: 
            print("Obrigado por usar o programa, saindo...")
            break
        else:
            print("Opção inválida!")
