# 2. Ler uma lista de 10 números reais e mostre-os na ordem inversa.

L = list(range(10, 21))
LR = L[:]
LR.sort(reverse=True)
print(f'Ordem original: {L}'
      f'\nOrdem inversa: {LR}')
