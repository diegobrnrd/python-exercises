# • Crie as classes Biblioteca e Livro.
# – A Biblioteca deverá conter uma lista de livros disponíveis e lista de livros alugados
# – A biblioteca deverá possuir um método para alugar um livro. Caso o livro já esteja alugado a pessoa não poderá
#   alugar.
# – A biblioteca deverá possuir um método para devolver o livro.
# – Adapte o código para poder informar o nome do livro mais alugado.

class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.alugado = False


class Biblioteca:
    def __init__(self):
        self.livros_disponiveis = []
        self.livros_alugados = []

    def adicionar_livro(self, livro):
        self.livros_disponiveis.append(livro)

    def alugar_livro(self, titulo):
        for livro in self.livros_disponiveis:
            if livro.titulo == titulo and not livro.alugado:
                livro.alugado = True
                self.livros_alugados.append(livro)
                self.livros_disponiveis.remove(livro)
                return True
        return False

    def devolver_livro(self, titulo):
        for livro in self.livros_alugados:
            if livro.titulo == titulo:
                livro.alugado = False
                self.livros_disponiveis.append(livro)
                self.livros_alugados.remove(livro)
                return True
        return False

    def livro_mais_alugado(self):
        if not self.livros_alugados:
            return None

        contagem_livros = {}
        for livro in self.livros_alugados:
            if livro.titulo in contagem_livros:
                contagem_livros[livro.titulo] += 1
            else:
                contagem_livros[livro.titulo] = 1

        mais_alugado = max(contagem_livros, key=contagem_livros.get)
        return mais_alugado


biblioteca = Biblioteca()

livro_1 = Livro('Do Inferno')
livro_2 = Livro('Watchmen')

biblioteca.adicionar_livro(livro_1)
biblioteca.adicionar_livro(livro_2)

biblioteca.alugar_livro('Do Inferno')
biblioteca.alugar_livro('Watchmen')
biblioteca.alugar_livro('Watchmen')

biblioteca.devolver_livro('Do Inferno')
biblioteca.alugar_livro('Do Inferno')

print(f'Livro mais alugado: {biblioteca.livro_mais_alugado()}')
