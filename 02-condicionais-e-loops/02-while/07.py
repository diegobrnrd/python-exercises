# 7. Faça o algoritmo de imprimir a tabuada de um número fornecido pelo usuário, usando while. Após mostrar a tabuada
# o programa deve perguntar se deseja imprimir a tabuada de um novo número.

while True:
    numero = int(input('Digite um número para ver sua tabuada: '))
    x = 1
    while x <= 10:
        print(f'{numero} x {x} = {numero * x}')
        x += 1
    continuar = input('Deseja imprimir a tabuada de um novo número? (S para sim): ')
    if continuar != 'S' and continuar != 's':
        break
