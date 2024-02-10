# 5. Faça um Programa que leia três números e mostre-os em ordem decrescente.

numero_1 = float(input('1º Número: '))
numero_2 = float(input('2º Número: '))
numero_3 = float(input('3º Número: '))
if numero_1 >= numero_2 and numero_1 >= numero_3:
    if numero_2 >= numero_3:
        print(numero_1, numero_2, numero_3)
    else:
        print(numero_1, numero_3, numero_2)
elif numero_2 >= numero_1 and numero_2 >= numero_3:
    if numero_1 >= numero_3:
        print(numero_2, numero_1, numero_3)
    else:
        print(numero_2, numero_3, numero_1)
else:
    if numero_1 >= numero_2:
        print(numero_3, numero_1, numero_2)
    else:
        print(numero_3, numero_2, numero_1)
