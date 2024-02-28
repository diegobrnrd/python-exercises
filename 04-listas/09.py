# 9. Faça um programa que leia um número indeterminado de notas. Após esta entrada de dados, faça o seguinte:

# • Mostre a quantidade de notas que foram lidas.
# • Exiba todas as notas na ordem em que foram informadas.
# • Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo do outra.
# • Calcule e mostre a soma das notas.
# • Calcule e mostre a média das notas.
# • Calcule e mostre a quantidade de notas acima da média calculada.

notas = []
while True:
    nota = float(input('Digite a nota (11 para sair): '))
    if nota < 0:
        print('Nota inválida!')
    elif 10 < nota < 11:
        print('Nota inválida!')
    elif nota > 11:
        print('Nota inválida!')
    elif nota == 11:
        break
    else:
        notas.append(nota)

print(f'\nQuantidade de notas lidas: {len(notas)} notas.'
      f'\nNotas na ordem que forma informadas: {notas}')
print('\nNotas na ordem inversa à que foram informadas: ')

notas_inversa = notas[:]
notas_inversa.reverse()

for n in notas_inversa:
    print(n)

print(f'\nSoma das notas: {sum(notas):.2f}'
      f'\nMédia das notas: {sum(notas) / len(notas):.2f}')

notas_acima_media = 0
for n in notas:
    if n > sum(notas) / len(notas):
        notas_acima_media += 1

print(f'Quantidade de notas acima da média: {notas_acima_media} notas.')
