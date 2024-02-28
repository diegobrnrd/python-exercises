# 5. O Departamento Estadual de Meteorologia te contratou para desenvolver um programa que leia um conjunto de 100
# temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

maior_temperatura = -1000
menor_temperatura = 1000
soma = 0

for t in range(1, 101):
    temperatura = float(input(f'{t}ª temperatura: '))
    soma += temperatura
    if temperatura > maior_temperatura:
        maior_temperatura = temperatura
    if temperatura < menor_temperatura:
        menor_temperatura = temperatura

print(f'\nMaior temperatura: {maior_temperatura}'
      f'\nMenor temperatura: {menor_temperatura}'
      f'\nMédia das temperaturas: {soma / 100}')
