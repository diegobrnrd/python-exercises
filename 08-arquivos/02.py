# 2. Escreva um programa que lê um arquivo contendo a identidade e o nome de várias pessoas, no seguinte formato

# 5384423 Manoel
# 4345566 Alberto
# 3235574 Mariana

# o programa deve gerar um dicionário onde as chaves são as identidades e os valores os nomes. Ao final o programa
# deve exibir o dicionário.

nome_do_arquivo = 'identidades.txt'
identidades_nomes = {}
with open(nome_do_arquivo, 'r') as arquivo:
    for linha in arquivo:
        identidade, nome = linha.split()
        identidades_nomes[identidade] = nome
print(f'Dicionário de identidade e nomes: {identidades_nomes}')
