# • 4. Escreva um programa que leia um arquivo com um conjunto de nomes (1 por linha). O programa deve ordenar os
# nomes e gerar um novo arquivo com os nomes ordenados.

with open('nomes.txt', 'r') as arquivo:
    nomes = arquivo.readlines()
nomes_ordenados = sorted(nomes)

with open('nomes_ordenados.txt', 'w') as arquivo:
    for nome in nomes_ordenados:
        arquivo.write(nome)
