# 4. Faça um programa que identifica os 15 primeiros números primos (utilizando a instrução break).

primos = 0
numero = 2
print('Os 15 primeiros números primos são: ', end='')
while primos < 15:
    eh_primo = True
    divisor = 2
    while divisor < numero:
        if numero % divisor == 0:
            eh_primo = False
            break
        divisor += 1
    if eh_primo:
        print(numero, end=' ')
        primos += 1
    numero += 1
