import main
import streamlit as st
import sqlite3
conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER,
    disponivel TEXT
    )
""")
try:
    #Criar um objeto "cursor" server para executar os comandos SQL
   
    main.menu()
except sqlite3.OperationalError:
    pass