# 5. Inicialize uma lista de 20 números inteiros. Armazene os números pares em uma lista PAR e os números ímpares em
# uma lista IMPAR. Imprima as listas PAR e IMPAR.

L = list(range(60, 81))
P, I = [], []
for n in L:
    if n % 2 == 0:
        P.append(n)
    else:
        I.append(n)
print(f'Lista par: {P}'
      f'\nLista ímpar: {I}')
