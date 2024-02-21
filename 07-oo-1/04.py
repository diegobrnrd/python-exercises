# • 4. Implemente uma classe Aluno, que deve ter os seguintes atributos: nome, curso, tempoSemDormir (em horas).
# Essa classe deverá ter os seguintes métodos:

# – estudar (que recebe como parâmetro a qtd de horas de estudo e acrescenta tempoSemDormir)
# – Dormir (que recebe como parâmetro a qtd de horas de sono e reduz tempoSemDormir)
# • Crie um código de teste da classe, criando um objeto da classe aluno e usando os métodos estudar e dormir.

# Ao final imprima quanto tempo o aluno está sem dormir.

class Aluno:
    def __init__(self, nome, curso, tempo_sem_dormir):
        self.nome = nome
        self.curso = curso
        self.tempo_sem_dormir = tempo_sem_dormir

    def estudar(self, horas_de_estudo):
        self.tempo_sem_dormir += horas_de_estudo

    def dormir(self, horas_de_sono):
        self.tempo_sem_dormir -= horas_de_sono


aluno_1 = Aluno('Diego', 'Sistemas de Informação', 16)
aluno_1.estudar(8)
aluno_1.dormir(6)

print(f'{aluno_1.nome} está {aluno_1.tempo_sem_dormir} hora(s) sem dormir.')
