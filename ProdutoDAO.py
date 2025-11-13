# ProdutoDAO.py

from ConexaoBanco import ConexaoBanco
from tkinter import messagebox
from mysql.connector import Error
from ProdutoVO import ProdutoVO


class ProdutoDAO:
    def __init__(self): # Método construtor
        self.conexao = ConexaoBanco().get_conexao() # obtendo a conexão no construtor
        #Verificando se a coneção é válida antes de tentar criar o cursor
        if self.conexao and self.conexao.is_connected():
            self.cursor = self.conexao.cursor()
        else:
            self.cursor = None

    def cadastrar_produtos(self, produto_dict):
        sql = "INSERT INTO produtos(nome, valor, quantidade) VALUES(%s, %s, %s)"
        valores = (produto_dict['nome'], produto_dict['valor'], produto_dict['quantidade'])
        try:
            self.cursor.execute(sql, valores)
            self.conexao.commit()
            # Depurando
            print(f"Produto {produto_dict['nome']} salvo com sucesso no banco de dados")
        except Error as e:
            messagebox.showerror("Erro de Cadastro", f"Erro ao cadastrar produto: {e}")
            self.conexao.rollback()
            

    def __del__(self): # Método Destrutor
        self.cursor.close()
        self.conexao.close()


    # Função BuscarProduto
    def buscar_produtos(self):
        try:
            if self.conexao.is_connected():
                sql = "SELECT * FROM produtos"
                self.cursor.execute(sql)
                rows = self.cursor.fetchall()

                produtos = []

                for row in rows:
                    pVO = ProdutoVO(
                        idprodutos=row[0],
                        nome=row[1],
                        valor=row[2],
                        quantidade=row[3]
                    )
                    produtos.append(pVO)

                return produtos
        
        except Error as e:
            messagebox.showerror("Erro", f"Erro ao buscar produto! {e}")
        finally:
            if self.conexao.is_connected():
                self.conexao.close()
    
    def alterar_produto(self, produto_dict):
        
        if not self.cursor: return
        sql = "UPDATE produtos SET nome = %s, valor = %s, quantidade = %s WHERE idprodutos = %s"
        valores = (produto_dict['nome'], produto_dict['valor'], produto_dict['quantidade'], produto_dict['idprodutos'])
        try:
            self.cursor.execute(sql, valores)
            self.conexao.commit()
            return self.cursor.rowcount > 0  #retorna true se alguma linha for alterada
        except Error as e:
            messagebox.showerror("Erro da Alteração", f"Erro ao alterar produto: {e}")
            self.conexao.rollback()
            return False



class ProdutoVO:
    def __init__(self, idprodutos, nome, valor, quantidade):
        self.idprodutos = idprodutos
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade