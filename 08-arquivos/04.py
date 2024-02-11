# • 4. Escreva um programa que leia um arquivo com um conjunto de nomes (1 por linha). O programa deve ordenar os
# nomes e gerar um novo arquivo com os nomes ordenados.

arquivo_entrada = 'nomes.txt'
arquivo_saida = 'nomes_ordenados.txt'
with open(arquivo_entrada, 'r') as arquivo:
    nomes = arquivo.readlines()
nomes_ordenados = sorted(nomes)
with open(arquivo_saida, 'w') as arquivo:
    for nome in nomes_ordenados:
        arquivo.write(nome)
