# 1. Ler uma lista de 5 números inteiros e mostre cada número juntamente com a sua posição na lista.

L = list(range(1, 11, 2))
x = 0
for n in L:
    print(f'Número {n} - Posição {x}')
    x += 1
