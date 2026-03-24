import sqlite3
import os

def criar_conexao():

    # pega o caminho da pasta src
    pasta_src = os.path.dirname(__file__)

    # volta uma pasta (raiz do projeto)
    raiz_projeto = os.path.abspath(os.path.join(pasta_src, ".."))

    # monta o caminho até o banco
    caminho_db = os.path.join(raiz_projeto, "data", "processed", "olist.db")

    # conecta
    conn = sqlite3.connect(caminho_db)

    return conn