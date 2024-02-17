# 2. Ler uma lista de 10 números reais e mostre-os na ordem inversa.

L = []
for n in range(1, 11):
    numero = float(input(f'{n}ª número: '))
    L.append(numero)
L.reverse()
print(f'Números na ordem inversa: {L}')
