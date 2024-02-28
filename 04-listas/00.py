# Mostre-me as seguintes listas, derivadas de:

#  [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#  Intervalo de 1 a 9
#  Intervalo de 8 a 13
#  Números pares
#  Números ímpares
#  Todos os múltiplos de 2, 3 e 4
#  Lista reversa
#  Razão entre a soma do intervalo de 10 a 15 pelo intervalo de 3 a 9 em float!

L = list(range(16))
PA = []
IM = []
M3 = []
M4 = []
LR = L[::-1]

for numero in L:
    if numero % 2 == 0:
        PA.append(numero)
    else:
        IM.append(numero)
for numero in L:
    if numero % 3 == 0:
        M3.append(numero)
    if numero % 4 == 0:
        M4.append(numero)

print(f'Intervalo de 1 a 9: {L[:10]}'
      f'\nIntervalo de 8 a 13: {L[8:14]}'
      f'\nNúmeros pares: {PA}'
      f'\nNúmeros ímpares: {IM}'
      f'\nMúltiplos de 2: {PA}'
      f'\nMúltiplos de 3: {M3}'
      f'\nMúltiplos de 4: {M4}'
      f'\nLista reversa: {LR}'
      f'\nRazão entre a soma do intervalo de 10 a 15 pelo intervalo de 3 a 9 em float: {sum(L[10:16]) / sum(L[3:10])}')
