# 6. Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Em seguida, calcule a média anual das temperaturas e mostre a média calculada juntamente com todas as temperaturas
# acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 –Janeiro, 2 – Fevereiro, . . . ).

T = []
M = ['Janeiro', 'Fervereiro', 'Março', 'Abril',
     'Maio', 'Junho', 'Julho', 'Agosto',
     'Setembro', 'Outubro', 'Novembro', 'Dezembro']
for m in range(12):
    temperatura = float(input(f'Temperatura de {M[m]}: '))
    T.append(temperatura)
media = sum(T) / 12
print(f'Média anual das temperaturas: {media}')
print('Meses onde a temperatura foi acima da média anual: ', end='')
i = 0
qtde_temp_acima_media = 0
for t in T:
    if t > media:
        print(f'{i + 1} - {M[i]}', end=' ')
        qtde_temp_acima_media += 1
    i += 1
if qtde_temp_acima_media == 0:
    print('nenhuma ocorrência.')
