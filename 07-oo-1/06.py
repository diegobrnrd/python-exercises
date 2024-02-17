# • Crie uma classe Aluno, que possui como atributo um nome e cpf. Crie outra classe chamada Equipe, que possui como
#   atributo uma lista de participantes do tipo Aluno e outro atributo chamado projeto.
# • Crie uma terceira classe chamada GerenciadorEquipes. Essa classe possui como atributo uma lista de todas as equipes
#   formadas. Ela deverá possuir o método criarEquipe, que recebe uma lista de alunos de uma equipe e diz se a equipe
#   pode ser formada ou não. Caso não haja nenhum aluno da equipe a ser formada em uma outra equipe com o mesmo
#   projeto, então a equipe é criada e acrescentada à lista. Caso contrário é informada que a equipe não pode ser
#   criada.

class Aluno:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


class Equipe:
    def __init__(self, participantes, projeto):
        self.participantes = participantes
        self.projeto = projeto


class GerenciadorEquipes:
    def __init__(self):
        self.equipes = []

    def criar_equipe(self, participantes, projeto):
        for equipe in self.equipes:
            if equipe.projeto == projeto:
                for aluno in equipe.participantes:
                    if aluno in participantes:
                        return 'A equipe não pode ser criada.'
        nova_equipe = Equipe(participantes, projeto)
        self.equipes.append(nova_equipe)
        return 'A equipe foi criada com sucesso.'


aluno_1 = Aluno('João', "123.456.789-00")
aluno_2 = Aluno('Maria', "987.654.321-00")
aluno_3 = Aluno('Carlos', "111.222.333-44")
aluno_4 = Aluno('Ana', "999.888.777-66")

gerenciador = GerenciadorEquipes()

print(gerenciador.criar_equipe([aluno_1, aluno_2], 'Projeto 1'))

print(gerenciador.criar_equipe([aluno_3, aluno_4], 'Projeto 2'))

print(gerenciador.criar_equipe([aluno_1, aluno_3], 'Projeto 1'))
