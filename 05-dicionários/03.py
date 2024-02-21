# • 3. Crie um programa que cadastre informações de várias pessoas (nome, idade e cpf) e depois coloque em um
# dicionário. Depois remova todas as pessoas menores de 18 anos do dicionário e coloque em outro dicionário.

pessoas = {}
pessoas_menor = {}
while True:
    resposta = input('Digite C para cadastrar ou S para sair: ')
    if resposta.lower() == 's':
        break
    elif resposta.lower() != 's' and resposta.lower() != 'c':
        print('Reposta inválida!')
    else:
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        cpf = int(input('CPF: '))
        pessoas[cpf] = {'nome': nome, 'idade': idade}
cpfs = list(pessoas.keys())
for cpf in cpfs:
    if pessoas[cpf]['idade'] < 18:
        pessoas_menor[cpf] = pessoas[cpf]
        del pessoas[cpf]
