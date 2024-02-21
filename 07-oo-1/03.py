# • 3. Crie uma classe Livro que possui os atributos nome, qtdPaginas, autor e preço.
# – Crie os métodos getPreco para obter o valor do preco e o método setPreco para setar um novo valor do preco.
# • Crie um codigo de teste

class Livro:
    def __init__(self, nome, paginas, autor, preco):
        self.nome = nome
        self.paginas = paginas
        self.autor = autor
        self.preco = preco

    def get_preco(self):
        return self.preco

    def set_preco(self, novo_preco):
        self.preco = novo_preco


livro_1 = Livro('Do Inferno', '592', 'Alan Moore', 106.14)
livro_1.set_preco(100)

print(f'Valor do livro {livro_1.nome}: R$ {livro_1.preco:.2f}')
