# 1. Classe Triangulo: Crie uma classe que modele um triangulo:

# – Atributos: LadoA, LadoB, LadoC
# – Métodos: calcular Perímetro, getMaiorLado;

# • Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidas de um triangulo.
#   Depois, deve criar um objeto com as medidas e imprimir sua área e maior lado.

class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    def calcula_perimetro(self):
        return self.lado_a + self.lado_b + self.lado_c

    def get_maior_lado(self):
        return max(self.lado_a, self.lado_b, self.lado_c)


ladoA = float(input('Informe o primeiro lado do triângulo: '))
ladoB = float(input('Informe o segundo lado do triângulo: '))
ladoC = float(input('Informe o terceiro lado do triângulo: '))

triangulo = Triangulo(ladoA, ladoB, ladoC)

print(f'''
O perímetro do triângulo é: {triangulo.calcula_perimetro()}
O maior lado do triângulo é: {triangulo.get_maior_lado()}''')
