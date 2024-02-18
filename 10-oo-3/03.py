# • 3. Crie um programa que implemente o seguinte diagrama de classe:

class Atleta:
    def __init__(self, peso, ocupacao='Aposentado'):
        self.ocupacao = ocupacao
        self.peso = peso
        self.aposentado = False
        if self.ocupacao == 'Aposentado':
            self.aposentado = True
        self.aquecido = False

    def aposentar(self):
        self.aposentado = True

    def aquecer(self):
        self.aquecido = True


class Corredor(Atleta):
    def __init__(self, peso):
        super().__init__(peso)
        self.correndo = False

    def correr(self):
        self.correndo = True


class Nadador(Atleta):
    def __init__(self, peso):
        super().__init__(peso)
        self.nadando = False

    def nadar(self):
        self.nadando = True


class Ciclista(Atleta):
    def __init__(self, peso):
        super().__init__(peso)
        self.pedalando = False

    def pedalar(self):
        self.pedalando = True


class TriAtleta(Corredor, Nadador, Ciclista):
    def __init__(self, peso):
        Corredor.__init__(self, peso)
        Nadador.__init__(self, peso)
        Ciclista.__init__(self, peso)


triatleta = TriAtleta(70)
