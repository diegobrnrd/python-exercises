# • 3. Crie uma classe Livro que possui os atributos nome, qtdPaginas, autor e preço.
# – Crie os métodos getPreco para obter o valor do preco e o método setPreco para setar um novo valor do preco.
# • Crie um codigo de teste

class Livro:
    def __init__(self, nome, qtd_paginas, autor, preco):
        self.nome = nome
        self.qtd_paginas = qtd_paginas
        self.autor = autor
        self.preco = preco

    def get_preco(self):
        return self.preco

    def set_preco(self, novo_preco):
        self.preco = novo_preco
        return self.preco


livro1 = Livro('Do Inferno', '592', 'Alan Moore', 106.14)

print(f'Valor do livro {livro1.nome}: R$ {livro1.preco}')
