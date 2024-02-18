# 2. Escreva um programa que lê um arquivo contendo a identidade e o nome de várias pessoas, no seguinte formato

# 5384423 Manoel
# 4345566 Alberto
# 3235574 Mariana

# o programa deve gerar um dicionário onde as chaves são as identidades e os valores os nomes. Ao final o programa
# deve exibir o dicionário.

dicionario_identidades = {}
with open('identidades.txt', 'r') as arquivo:
    for linha in arquivo:
        identidade, nome = linha.split()
        dicionario_identidades[identidade] = nome
print(dicionario_identidades)
