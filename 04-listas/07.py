# 7. Faça um programa que crie uma matriz aleatoriamente. O tamanho da matriz deve ser informado pelo usuário.

import random

num_linhas = int(input('Informe a quantidade de linhas da matriz: '))
num_colunas = int(input('Informe a quantidade de colunas da matriz: '))

matriz = []

for _ in range(num_linhas):
    linha = []
    for _ in range(num_colunas):
        valor = random.uniform(1, 50)
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    for valor in linha:
        print(f'{valor:8.2f}', end=' ')
    print()
