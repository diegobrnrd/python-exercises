# 2. Classe Funcionário: Implemente a classe Funcionário. Um funcionário tem um nome e um salário. Escreva um
# construtor com dois parâmetros (nome e salário) e o método aumentarSalario (porcentualDeAumento) que aumente
# o salário do funcionário em uma certa porcentagem. Exemplo de uso:

# harry = funcionário("Harry",25000)
# harry.aumentarSalario(10)

# Faca um programa que teste o método da classe.

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self, porcentual):
        self.salario += self.salario * porcentual / 100
        return self.salario


funcionario1 = Funcionario('Diego', 2000)
funcionario1.aumentar_salario(10)

print(f'O novo salário de {funcionario1.nome} é: R$ {funcionario1.salario:.2f}')
