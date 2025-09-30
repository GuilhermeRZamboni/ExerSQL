import main
import streamlit as st
import sqlite3
conexao = sqlite3.connect("biblioteca.db")

#Criar um objeto "cursor" server para executar os comandos SQL
cursor = conexao.cursor()
todos_id = cursor.execute("SELECT id FROM livros")
main.menu()