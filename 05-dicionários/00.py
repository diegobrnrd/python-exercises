# • Crie um dicionário d e coloque nele os dados fornecidos pelo usuário: nome, idade, telefone,endereço.

d = {}

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
telefone = input('Digite seu telefone: ')
endereco = input('Digite seu endereço: ')

d['nome'] = nome
d['idade'] = idade
d['telefone'] = telefone
d['endereço'] = endereco

# • Também usando d, imprima todos os itens do dicionário no formato chave : valor, ordenado pela chave

for chave, valor in d.items():
    print(f'{chave}: {valor}')
