# 2. Tem-se um conjunto de dados contendo a altura e o sexo (M ou F) de 15 pessoas. Faça um programa que calcule e
# mostre:

# – a maior e a menor altura do grupo
# – a média de altura das mulheres
# – o número de homens
# – o sexo da pessoa mais alta

maior_altura = -1000
menor_altura = 1000
quantidade_homens = 0
quantidade_mulheres = 0
soma_altura_mulheres = 0
sexo_pessoa_mais_alta = None

for p in range(1, 16):
    altura = int(input('Digite a altura (cm): '))
    sexo = input('Digite o sexo (M ou F): ')
    if altura > maior_altura:
        maior_altura = altura
        sexo_pessoa_mais_alta = sexo
    if altura < menor_altura:
        menor_altura = altura
    if sexo == 'M' or sexo == 'm':
        quantidade_homens += 1
    elif sexo == 'F' or sexo == 'f':
        quantidade_mulheres += 1
        soma_altura_mulheres += altura

print(f'Maior altura: {maior_altura}cm.'
      f'\nMenor altura: {menor_altura}cm.')

if quantidade_mulheres == 0:
    print('Média de altura das mulheres: não há mulheres.')
else:
    print(f'Média de altura das mulheres: {soma_altura_mulheres / quantidade_mulheres}cm.')

print(f'Quantidade de homens: {quantidade_homens}')

if sexo_pessoa_mais_alta == 'M' or sexo_pessoa_mais_alta == 'm':
    print('Sexo da pessoa mais alta: Masculino.')
else:
    print('Sexo da pessoa mais alta: Feminino.')
