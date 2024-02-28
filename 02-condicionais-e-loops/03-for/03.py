# 3. Em uma eleição presidencial com 15 eleitores existem 3 candidatos. Os votos são informados por meio de código.
# Os códigos utilizados são:

# – 1 – Candidato A, 2 -Candidato B, 3 – Candidato C, 4 - Voto Nulo e 5 - Voto em Branco

# Faça um programa que leia os votos de cada eleitor, calcule e mostre:

# – O total de votos para cada candidato
# – O total de votos nulos
# – O total de votos em branco
# – A percentagem de votos nulos sobre o total de votos;
# – A percentagem de votos em branco sobre o total de votos.

print('1 - Candidato A'
      '\n2 - Candidato B'
      '\n3 - Candidato C'
      '\n4 - Voto Nulo'
      '\n5 - Voto em Branco\n')

total_a, total_b, total_c = 0, 0, 0
total_nulo, total_branco = 0, 0

for v in range(1, 16):
    voto = int(input('Insira seu voto: '))
    if voto == 1:
        total_a += 1
    elif voto == 2:
        total_b += 1
    elif voto == 3:
        total_c += 1
    elif voto == 4:
        total_nulo += 1
    elif voto == 5:
        total_branco += 1

total_votos = total_a + total_b + total_c + total_nulo + total_branco

print(f'\nTotal votos candidato A: {total_a} voto(s).'
      f'\nTotal votos candidato B: {total_b} voto(s).'
      f'\nTotal votos candidato C: {total_c} voto(s).'
      f'\nTotal votos nulo: {total_nulo} votos(S).'
      f'\nTotal votos em branco: {total_branco} voto(s).'
      f'\nPercentagem de votos nulos sobre o total de votos: {total_nulo * 100 / total_votos:.2f}%'
      f'\nPercentagem de votos em branco sobre o total de votos: {total_branco * 100 / total_votos:.2f}%')
