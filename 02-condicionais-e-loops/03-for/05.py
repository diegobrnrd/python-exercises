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

print(f'''
Maior temperatura: {maior_temperatura}
Menor temperatura: {menor_temperatura}
Média das temperaturas: {soma / 100}''')
