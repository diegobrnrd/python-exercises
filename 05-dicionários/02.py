# 2. Crie um dicionário que é uma agenda e coloque nele os seguintes dados: chave (cpf), nome, idade, telefone.
# O programa deve ler um número indeterminado de dados, criar a agenda e imprimir todos os itens do dicionário
# no formato chave: nome-idade-fone.

agenda = {}

while True:
    cpf = input('Digite o cpf para cadastrar (S para sair): ')
    if cpf.lower() == 's':
        break
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    telefone = input('Digite seu telefone: ')
    agenda[cpf] = {'nome': nome, 'idade': idade, 'telefone': telefone}

print('\nAgenda:')

for cpf, dados in agenda.items():
    print(f'{cpf}: {dados["nome"]}-{dados["idade"]}-{dados["telefone"]}')
