# 4. Ler um vetor com 20 idades e exibir a maior e menor.

idades = []
for i in range(1, 21):
    idade = int(input(f'{i}ª idade: '))
    idades.append(idade)
print(f'Maior idade: {max(idades)}'
      f'\nMenor idade: {min(idades)}')
