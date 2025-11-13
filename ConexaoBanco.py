# ConexaoBanco.py

#  pip install mysql-connector-python

# python.exe -m pip install --upgrade pip

import mysql.connector
from mysql.connector import Error
from tkinter import messagebox

class ConexaoBanco:
    def get_conexao(self):
        conexao = None
        try:
            conexao = mysql.connector.connect(
                host='localhost',
                database='padaria',
                user='root',
                password=''
            )
            if conexao.is_connected():
                print("Conectado ao MySQL")
        except Error as e:
            messagebox.showerror("Erro", f"Erro ao conectar! {e}")
        return conexao
