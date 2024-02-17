# • 3. Crie um programa que cadastre informações de várias pessoas (nome, idade e cpf) e depois coloque em um
# dicionário. Depois remova todas as pessoas menores de 18 anos do dicionário e coloque em outro dicionário.

pessoas = []

while True:
    nome = input("Digite o nome da pessoa (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    idade = int(input("Digite a idade da pessoa: "))
    cpf = input("Digite o CPF da pessoa: ")

    pessoa = {"nome": nome, "idade": idade, "cpf": cpf}
    pessoas.append(pessoa)

menores_de_idade = [pessoa for pessoa in pessoas if pessoa['idade'] < 18]

pessoas = [pessoa for pessoa in pessoas if pessoa['idade'] >= 18]

print("\nPessoas menores de 18 anos:")
for pessoa in menores_de_idade:
    print(pessoa)

print("\nPessoas maiores de 18 anos:")
for pessoa in pessoas:
    print(pessoa)
