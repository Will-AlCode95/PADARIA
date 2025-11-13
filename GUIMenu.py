# GUIMenu.py

import tkinter as tk
from GUICadastroProdutos import CadastroProdutos
from GUIManutencaoProduto import ManutencaoProdutos


class MenuGUI(tk.Tk):
    def __init__(self):
        super().__init__()  # Inicializa a classe base tk.Tk
        self.title("Sistema de Gerenciamento de cadastro")
        self.geometry("450x400")

        menu_principal = tk.Menu(self)
        self.config(menu=menu_principal)

        # Adicionando os itens de menu
        menu_arq = tk.Menu(menu_principal)
        menu_principal.add_cascade(label='Cadastro', menu=menu_arq)

        # Adicionando submenus ao Menu
        menu_arq.add_command(label='Clientes')
        menu_arq.add_command(label='Colaboradores')
        menu_arq.add_command(label='Fornecedores')
        menu_arq.add_separator()
        menu_arq.add_command(label='Produtos', command=self.abrir_CadProdutos)

        # Adicionando outro Menu e submenus
        menu_Manutencao = tk.Menu(menu_principal)
        menu_principal.add_cascade(label='Manutenção', menu=menu_Manutencao)
        menu_Manutencao.add_command(label='Clientes')
        menu_Manutencao.add_command(label='Colaboradores')
        menu_Manutencao.add_command(label='Fornecedores')
        menu_Manutencao.add_separator()
        menu_Manutencao.add_cascade(
            label='Produtos', command=self.abrir_ManuProdutos)

        menu_sair = tk.Menu(menu_principal)
        menu_principal.add_cascade(label='Sair', command=self.sair)

    # Criando o Menu

    def abrir_CadProdutos(self):
        menu_window = tk.Toplevel(self)
        CadastroProdutos(menu_window)

    def abrir_ManuProdutos(self):
        menu_window = tk.Toplevel(self)
        ManutencaoProdutos(menu_window)

    def sair(self):
        self.destroy()


if __name__ == "__main__":
    app = MenuGUI()
    app.mainloop()
