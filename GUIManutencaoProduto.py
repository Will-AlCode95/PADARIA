# GUIManutencaoProduto.py

import tkinter as tk

from tkinter import ttk, messagebox
from ProdutoDAO import ProdutoDAO
from ProdutoVO import ProdutoVO
from decimal import Decimal # Necessário para conversão de valores

class ManutencaoProdutos:
    def __init__(self, janela):
        self.janela = janela # Criando a janela de exibição
        self.janela.title("Manutenção de Produtos")
        self.janela.geometry("700x400")


        # Frame para a janela
        frame_tabela = tk.Frame(janela)
        frame_tabela.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Criando os Widgets
        self.tree = ttk.Treeview(janela, columns=("nome", "valor", "quantidade"), show='headings')
        self.tree.heading("nome", text="Nome")
        self.tree.column("nome", width=250)
        self.tree.heading("valor", text="Valor")
        self.tree.column("valor", width=100, anchor=tk.E)
        self.tree.heading("quantidade", text="Quantidade")
        self.tree.column("quantidade", width=100, anchor=tk.CENTER)

        self.tree.pack(fill=tk.BOTH, expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.selecionar_produto) # Liga o evento de seleção

        # Frame para os campos de alteração
        frame_campos = tk.LabelFrame(janela, text="Dados do Produto Selecionado", padx=10, pady=10)
        frame_campos.pack(pady=10, padx=10, fill=tk.X) # faz preenchimento horizontal

        # Campo de entrada de Alteração
        tk.Label(frame_campos, text="Nome: ").grid(row= 0, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_nome = tk.Entry(frame_campos, width=30)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_campos, text="Valor: ").grid(row= 0, column=2, padx=5, pady=5, sticky=tk.W)
        self.entry_valor = tk.Entry(frame_campos, width=15)
        self.entry_valor.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frame_campos, text="Quantidade: ").grid(row= 0, column=4, padx=5, pady=5, sticky=tk.W)
        self.entry_quantidade = tk.Entry(frame_campos, width=15)
        self.entry_quantidade.grid(row=0, column=5, padx=5, pady=5)

        # Variável para armazenar o ID do produto selecionado
        self.produto_selecionado_id = None

        # Frame para os botões de ação
        frame_botoes = tk.Frame(janela)
        frame_botoes.pack(pady=10)


        # Botões
        btn_alterar = tk.Button(frame_botoes, text="Alterar Produto", command=self.alterar_produto)
        btn_alterar.pack(side=tk.LEFT, padx=10)

        btn_excluir = tk.Button(frame_botoes, text="Excluir Produto", command=self.excluir_produto)
        btn_excluir.pack(side=tk.LEFT, padx=10)

        


        self.pDAO = ProdutoDAO()
        self.preecher_tabela()


    # Função para limpar os campos
    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_valor.delete(0, tk.END)
        self.entry_quantidade.delete(0, tk.END)
        self.produto_selecionado_id = None


    # Função que preenche os campos com o item selecionado
    def selecionar_produto(self, event):
        self.limpar_campos()
        item_selecionado = self.tree.focus()
        if item_selecionado:
            valores = self.tree.item(item_selecionado, 'values')
            if valores:
                self.produto_selecionado_id = int(valores[0])
                self.entry_nome.insert(0, valores[1])
                self.entry_valor.insert(0, valores[2])
                self.entry_quantidade.insert(0, valores[3])


    def preecher_tabela(self):
        # Limpa a tabela antes de preencher novamente
        for i in self.tree.get_children():
            self.tree.delete(i)


        try:
            produtos = self.pDAO.buscar_produtos()
            for produto in produtos:
                self.tree.insert("", "end", values=(produto.idprodutos, produto.nome, produto.valor, produto.quantidade) )
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao preencher a tabela: {e}")

            
    def alterar_produto(self):
        if not self.produto_selecionado_id:
            messagebox.showwarning("Aviso", "Selecione um produto na tabela para alterar.")
            return
        
        try:
            nome = self.entry_nome.get().strip()
            # Converte para Decimal e int ( necessário para o banco de dados )
            valor = Decimal(self.entry_valor.get().strip())
            quantidade = int(self.entry_quantidade.get().strip())
        except:
            messagebox.showerror("Erro", "Verifique se Valor e Quantidade são números válidos.")
            return
        
        if not nome or not valor or not quantidade:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return
        
        # Cria um ProdutoVO com o ID selecionado
        pVO = ProdutoVO(nome, valor, quantidade, idprodutos=self.produto_selecionado_id)

        if self.pDAO.alterar_produto(pVO.to_dict()):
            messagebox.showinfo("Sucesso", f"Produto ID {self.produto_selecionado_id} alterado com sucesso!")
            self.preecher_tabela()
            self.limpar_campos()
        else:
            messagebox.showerror("Erro", "Falha ao alterar o produto ou nenhum dado foi modificado.")



    def excluir_produto(self):
        pass