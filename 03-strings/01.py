# 1. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as
# duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

# Exemplo:
# Compara duas string
# String 1: Brasil Hexa 2006
# String 2: Brasil! Hexa 2006!
# Tamanho de "Brasil Hexa 2006": 16 caracteres
# Tamanho de "Brasil! Hexa 2006!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferentes.

string_1 = input('String 1: ')
string_2 = input('String 2: ')
print(f'String 1: {string_1}')
print(f'String 2: {string_2}')
print(f'Tamanho de "{string_1}": {len(string_1)} caracteres.')
print(f'Tamanho de "{string_2}": {len(string_2)} caracteres.')
if len(string_1) == len(string_2):
    print('As duas strings são de tamanhos iguais.')
else:
    print('As duas strings são de tamanhos diferentes.')
if string_1 == string_2:
    print('As duas strings possuem conteúdos iguais.')
else:
    print('As duas strings possuem conteúdos diferentes.')
