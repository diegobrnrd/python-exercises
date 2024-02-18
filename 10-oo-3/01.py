# • 1. Crie uma classe chamada Ingresso, que possui um valor em reais e um método imprimeValor()
# – Crie uma classe VIP, que herda de Ingresso e possui um valor adicional. Crie um método que retorne o valor do
#   ingresso VIP (com o adicional incluído)

class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprime_valor(self):
        return self.valor


class Vip(Ingresso):
    def __init__(self, valor, adicional):
        super().__init__(valor)
        self.valor += adicional

    def retorna_valor(self):
        return self.valor


ingresso_1 = Ingresso(50)
print(f'Valor ingresso: R$ {ingresso_1.imprime_valor():.2f}')
ingresso_2 = Vip(50, 20)
print(f'Valor ingresso VIP: R$ {ingresso_2.retorna_valor():.2f}')
