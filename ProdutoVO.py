# ProdutoVO.py


class ProdutoVO:
    def __init__(self, nome, valor, quantidade, idprodutos=None):
        self.idprodutos = idprodutos
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade

    def to_dict(self):
        return {
            "idprodutos": self.idprodutos,
            "nome": self.nome,
            "valor": self.valor,
            "quantidade": self.quantidade
        }
