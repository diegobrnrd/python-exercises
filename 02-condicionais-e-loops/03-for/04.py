# 4. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade
# de números impares.

pares = 0
impares = 0

for n in range(1, 11):
    numero = int(input(f'{n}º número inteiro: '))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'\nQuantidade de números pares: {pares}'
      f'\nQuantidade de números ímpares: {impares}')
