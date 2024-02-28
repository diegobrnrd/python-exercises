# 6. Faça um programa que peça 5 valores positivos do usuário (usando while). Caso o usuário digite algum número
# negativo o programa deve terminar imediatamente. Caso termine normalmente informe que os dados foram inseridos
# com sucesso (use o else).

x = 1

print('Digite 5 valores positivos.')

while x <= 5:
    numero = float(input(f'{x}º número: '))
    if numero < 0:
        break
    x += 1
else:
    print('Os dados foram inseridos com sucesso!')
