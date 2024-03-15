# • 2. Crie uma classe chamada Forma, que possui os atributos area e perimetro.
# – Implemente as subclasses Retangulo e Triangulo, que devem conter os métodos calculaArea e  calculaPerimetro.
#   A classe Triangulo deve ter também o atributo altura.
# • No código de teste crie um objeto da classe Triangulo e outro da Classe Retangulo.
#   Verifique se os dois são mesmo instancias de Forma (use instanceof) , e calcule a área de cada um.

class Forma:
    def __init__(self):
        self.area = 0
        self.perimetro = 0


class Retangulo(Forma):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def calcula_area(self):
        self.area = self.base * self.altura

    def calcula_perimetro(self):
        self.perimetro = 2 * (self.base + self.altura)


class Triangulo(Forma):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def calcula_area(self):
        self.area = (self.base * self.altura) / 2

    def calcula_perimetro(self):
        pass


retangulo = Retangulo(4, 5)
triangulo = Triangulo(3, 6)

print(isinstance(retangulo, Forma))
print(isinstance(triangulo, Forma))

retangulo.calcula_area()
triangulo.calcula_area()

print(f'''
Área do retângulo: {retangulo.area})
print(f'Área do triângulo: {triangulo.area}
''')
