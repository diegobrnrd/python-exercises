# 3. Faça um programa que imprima o fatorial de um número. O valor de entrada deve ser menor ou igual a 20.

while True:
    numero = int(input('Digite um número inteiro entre 0 e 20: '))
    if numero < 0 or numero > 20:
        print('Número Inválido!')
    else:
        fat = 1
        x = 1
        while x <= numero:
            fat *= x
            x += 1
        else:
            break

print(f'{numero}! = {fat}')
