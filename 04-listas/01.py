# 1. Ler uma lista de 5 números inteiros e mostre cada número juntamente com a sua posição na lista.

L = []
for n in range(1, 6):
    numero = int(input(f'{n}ª número: '))
    L.append(numero)
posicao = 0
for n in L:
    print(f'Posição: {posicao} - Número: {n}')
    posicao += 1
