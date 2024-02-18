# • 1. Construa uma classe Produto, que deve ter os atributos codigo e preco (privados). Adicione também um atributo
# estático qtdProd, que deverá ser acrescentado toda vez que um novo objeto é criado.
# – Crie os métodos get e set e teste a classe.

class Produto:
    quantidade_produto = 0

    def __init__(self, codigo, preco):
        self.__codigo = codigo
        self.__preco = preco
        Produto.quantidade_produto += 1

    @staticmethod
    def mostra_quantidade():
        return Produto.quantidade_produto

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, novo_codigo):
        self.__codigo = novo_codigo

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_valor):
        self.__preco = novo_valor


produto_1 = Produto(123, 50)
produto_2 = Produto(987, 1000)

produto_1.codigo = 321
produto_2.codigo = 789
produto_1.preco = 100
produto_2.preco = 500

print(f'\nCódigo: {produto_1.codigo} - Preço: R$ {produto_1.preco}'
      f'\nCódigo: {produto_2.codigo} - Preço: R$ {produto_2.preco}'
      f'\nQuantidade de produtos: {produto_2.quantidade_produto}')
