#importar a biblioteca sqlite3
import sqlite3
import streamlit as st
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
st.success("Tabela criada com sucesso!")
#função para cadastrar livros
def cadastrar_livro():
    try:
        titulo = st.text_input("Digite o titulo do livro: ")
        autor = st.text_input("Digte o autor do livro: ")
        ano = st.text_input("Digite o ano de lançamento do livro: ")
        if st.button("Cadastrar"):
            if ano.isdigit():
                cursor.execute("""INSERT INTO livros (titulo, autor, ano, disponivel)
                            VALUES (?, ?, ?, ?)
                            """, (titulo, autor, ano, "sim",))
                conexao.commit()
                st.success("Livro cadastrado com sucesso!")
            else:
                st.error("Digite uma data válida")
    except Exception as erro:
        st.error(f"Não foi possivel cadastrar o livro, Erro: {erro}")
    finally:
        if conexao:
            conexao.close()
#função para consultar livros
def consultar_livros():
    cursor.execute("SELECT * FROM livros")
    #fetchall traz todas as linhas da consulta
    livros = cursor.fetchall()
    if len(livros) > 0:
        for linha in livros:
            st.write(f"ID {linha[0]} | TITULO: {linha[1]} | AUTOR: {linha[2]} | ANO: {linha[3]} | DISPONIVEL: {linha[4]}")
            #Pegar os id's existentes:
            global todos_id
            todos_id = []
            todos_id.append(linha[0])
    else:
        st.warning("Nenhum livro cadastrado!")
    conexao.commit()
    if conexao:
            conexao.close()
def alterar_disponibilidade():
    consultar_livros()
    try:
        id_livro = st.selectbox("Selecione o id do livro que deseja alterar a disponibilidade: ", todos_id)
        if id_livro.isdigit():
            int(id_livro)
        else:
            st.error("Selecione um id valido")
        cursor.execute("SELECT disponivel FROM livros WHERE id = ?", (id,))
        resultado = cursor.fetchone()
        if resultado is None:
            st.error("ID não encontrado.")
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
        st.success("Disponibilidade alterada")
    except Exception as erro:
        st.error(f"Erro ao alterar a disponibilidade, Erro: {erro}")
    finally:
        #Sempre fecha a conexão, com sucesso ou erro
        if conexao:
            conexao.close()

def remover_livros():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()
       
        id_livro = st.selectbox("Digite o id do livro que deseja deletar: ", todos_id)
        if id_livro.isdigit():
            int(id_livro)
        else:
            st.error("Digite um id valido")
        cursor.execute("DELETE FROM livros WHERE id = ?", (id_livro,))
        conexao.commit()
       
        #Verificar se o livro foi realmente deletado
        if cursor.rowcount > 0:
            st.success("livro removido com sucesso!")
        else:
            st.warning("Nenhum livro cadastrado com o ID fornecido")
    except Exception as erro:
        print(f"Erro ao tentar excluir o aluno {erro}")
    finally:
        #Sempre fecha a conexão, com sucesso ou erro
        if conexao:
            conexao.close()

def menu():
    st.sidebar.write("Menu")
    opcao = st.sidebar.radio("Escolha uma opção",["Todos Livros", "Cadastrar Livros", "Alterar disponibilidade", "Excluir Livro"])
    if opcao == "Todos Livros":
        consultar_livros()
    if opcao == "Cadastrar Livros":
        cadastrar_livro()
