import sqlite3
import streamlit as st

# Função auxiliar para pegar todos os IDs
def obter_ids():
    conexao = sqlite3.connect ("biblioteca.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT id FROM livros")
    ids = [linha[0] for linha in cursor.fetchall()]
    
    return ids

# Função para cadastrar livros
def cadastrar_livro():
    try:
        titulo = st.text_input("Digite o título do livro: ")
        autor = st.text_input("Digite o autor do livro: ")
        ano = st.text_input("Digite o ano de lançamento do livro: ")

        if st.button("Cadastrar"):
            if titulo:
                if autor:
                    if ano.isdigit():
                        int(ano)
                        conexao = sqlite3.connect("biblioteca.db")
                        cursor = conexao.cursor()
                        cursor.execute("""
                            INSERT INTO livros (titulo, autor, ano, disponivel)
                            VALUES (?, ?, ?, ?)
                        """, (titulo, autor, ano, "sim"))
                        conexao.commit()
                        
                        st.success("Livro cadastrado com sucesso!")
                    else:
                        st.error("Digite um ano válido")
                else:
                    st.error("Primeiro digite um autor")   
            else:
                st.error("Primeiro digite um titulo")
    except Exception as erro:
        st.error(f"Não foi possível cadastrar o livro. Erro: {erro}")

# Função para consultar livros
def consultar_livros():
    conexao = sqlite3.connect("biblioteca.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()

    if len(livros) > 0:
        tabela_livros = {
            "Id" : [linha[0] for linha in livros],
            "Titulo" : [linha[1] for linha in livros],
            "Autor ": [linha[2] for linha in livros],
            "Ano" : [linha[3] for linha in livros],
            "Disponivel" : [":green[Sim]" if linha [4] == "sim" else ":red[Não]" for linha in livros ]}
        st.table(tabela_livros, border = "horizontal")
    else:
        st.warning("Nenhum livro cadastrado!")

# Função para alterar disponibilidade
def alterar_disponibilidade():
    ids = obter_ids()
    if not ids:
        st.warning("Nenhum livro cadastrado para alterar!")
        return

    id_livro = st.selectbox("Selecione o ID do livro:", ids)

    if st.button("Alterar disponibilidade"):
        with sqlite3.connect('biblioteca.db') as conexao:
            cursor = conexao.cursor()
            conexao.commit()
        cursor.execute("SELECT disponivel FROM livros WHERE id = ?", (id_livro,))
        resultado = cursor.fetchone()

        if resultado:
            novo_status = "não" if resultado[0] == "sim" else "sim"
            cursor.execute("UPDATE livros SET disponivel = ? WHERE id = ?", (novo_status, id_livro))
            conexao.commit()
            st.success(f"Disponibilidade alterada para {novo_status}!")
        else:
            st.error("ID não encontrado.")
        

# Função para remover livros
def remover_livros():
    ids = obter_ids()
    if not ids:
        st.warning("Nenhum livro cadastrado para remover!")
        return

    id_livro = st.selectbox("Selecione o ID do livro que deseja deletar:", ids)

    if st.button("Deletar Livro"):
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM livros WHERE id = ?", (id_livro,))
        conexao.commit()
        
        st.success("Livro removido com sucesso!")

# Menu principal
def menu():
    st.sidebar.write("Menu")
    opcao = st.sidebar.radio("Escolha uma opção", ["Todos Livros", "Cadastrar Livros", "Alterar disponibilidade", "Excluir Livro"])
    
    if opcao == "Todos Livros":
        consultar_livros()
    elif opcao == "Cadastrar Livros":
        cadastrar_livro()
    elif opcao == "Alterar disponibilidade":
        alterar_disponibilidade()
    elif opcao == "Excluir Livro":
        remover_livros()

