# 5. Inicialize uma lista de 20 números inteiros. Armazene os números pares em uma lista PAR e os números ímpares em
# uma lista IMPAR. Imprima as listas PAR e IMPAR.

L = list(range(60, 81))
PA, IM = [], []
for n in L:
    if n % 2 == 0:
        PA.append(n)
    else:
        IM.append(n)
print(f'Lista par: {PA}'
      f'\nLista ímpar: {IM}')
