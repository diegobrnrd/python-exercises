# • Crie um dicionário d e coloque nele os dados fornecidos pelo usuário: nome, idade, telefone,endereço.

dic = {}

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
telefone = input('Digite seu telefone: ')
endereco = input('Digite seu endereço: ')

dic['nome'] = nome
dic['idade'] = idade
dic['telefone'] = telefone
dic['endereço'] = endereco

# • Também usando d, imprima todos os itens do dicionário no formato chave : valor, ordenado pela chave

for chave, valor in dic.items():
    print(f'{chave}: {valor}')
