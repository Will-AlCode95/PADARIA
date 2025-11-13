# GUICadastroProdutos.py


import tkinter as tk
from tkinter import messagebox
from decimal import Decimal
from ProdutoVO import ProdutoVO

class CadastroProdutos:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Produtos")
        self.root.geometry('300x150')

        #Labels e Enradas para os dados dos produtos
        tk.Label(self.root, text="Nome: ").grid(row=0, column=0)
        self.entry_nome = tk.Entry(self.root)
        self.entry_nome.grid(row=0, column=1)

        tk.Label(self.root, text="Valor: ").grid(row=1, column=0)
        self.entry_valor = tk.Entry(self.root)
        self.entry_valor.grid(row=1, column=1)

        tk.Label(self.root, text="Quantidade: ").grid(row=2, column=0)
        self.entry_quantidade = tk.Entry(self.root)
        self.entry_quantidade.grid(row=2, column=1)

        # Botão para Salvar
        btn_salvar = tk.Button(self.root, text="Salvar", command=self.salvar_produtos)
        btn_salvar.grid(row=3, column=1, pady=10)

        # Botão para limpar
        btn_limpar = tk.Button(self.root, text="Limpar", command=self.limpar_produtos)
        btn_limpar.grid(row=3, column=2, padx=10)


    def salvar_produtos(self):
        # Importação movida para dentro da função para evitar circularidade
        from ProdutoDAO import ProdutoDAO

        try:
            nome = self.entry_nome.get().strip()
            valor = Decimal(self.entry_valor.get().strip() )
            quantidade = int(self.entry_quantidade.get().strip() )
        except Exception:
            messagebox.showerror("Erro de Entrada", "Verifique se o valor e a quantidade estão preenchido corretamente.")
            return

        # Criando uma instância do ProdutoVO (Note que não passamos idprodutos)
        pVO = ProdutoVO(nome, valor, quantidade)

        # Salvando os produtos no Banco de Dados ou eibindo os dados
        pDAO = ProdutoDAO()
        pDAO.cadastrar_produtos(pVO.to_dict() )
        messagebox.showinfo("Produto Salvo",f"Produto {nome} salvo com sucesso!" )
        self.limpar_produtos() 


    def limpar_produtos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_valor.delete(0, tk.END)
        self.entry_quantidade.delete(0, tk.END)

