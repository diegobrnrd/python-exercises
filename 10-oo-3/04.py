# 4. Considere as classes ContaCorrente e Poupanca apresentadas em sala de aula. Crie uma classe ContaImposto que
# herda de conta e possui um atributo percentualImposto. Esta classe também possui um método calculaImposto() que
# subtrai do saldo, o valor do próprio saldo multiplicado pelo percentual do imposto. Crie um programa para criar
# objetos, testar todos os métodos e exibir atributos das 3 classes (ContaCorrente, Poupanca e ContaImposto).

class ContaCorrente:
    def __init__(self, numero):
        self.numero = numero
        self.saldo = 0

    def creditar(self, valor):
        self.saldo += valor

    def debitar(self, valor):
        self.saldo -= valor


class Poupanca(ContaCorrente):
    def __init__(self, numero, taxa):
        super().__init__(numero)
        self.taxa_juros = taxa

    def render_juros(self):
        self.saldo += self.taxa_juros * (self.saldo / 100)


class ContaImposto(ContaCorrente):
    def __init__(self, numero, imposto):
        super().__init__(numero)
        self.percentual_imposto = imposto

    def calcula_imposto(self):
        self.saldo -= self.percentual_imposto * (self.saldo / 100)


obj_1 = ContaCorrente(123)
obj_1.creditar(2000)
obj_1.debitar(1000)
print(f'''
Número da conta: {obj_1.numero}
Saldo: R$ {obj_1.saldo:.2f}''')

obj_2 = Poupanca(456, 50)
obj_2.creditar(2000)
obj_2.debitar(1000)
obj_2.render_juros()
print(f'''
Número da conta: {obj_2.numero}'
Saldo: R$ {obj_2.saldo:.2f}'
Taxa de juros: {obj_2.taxa_juros}%''')

obj_3 = ContaImposto(789, 50)
obj_3.creditar(2000)
obj_3.debitar(1000)
obj_3.calcula_imposto()
print(f'''
Número da conta: {obj_3.numero}
Saldo: R$ {obj_3.saldo:.2f}
Taxa de imposto: {obj_3.percentual_imposto}%''')
