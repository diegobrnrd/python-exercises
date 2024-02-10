# 2. Escreva um programa que lê uma quantidade indeterminada de números inteiros e escreve todos os que forem ímpares
# positivos (use o ‘continue’). Considerar o valor 99 como fim da entrada.

impares = ''
while True:
    numero = int(input('Digite um número inteiro: '))
    if numero == 99:
        break
    elif numero < 0 or numero % 2 == 0:
        continue
    else:
        impares += f'{str(numero)} '
print(impares)
