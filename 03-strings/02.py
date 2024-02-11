# 2. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para
# frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras
# maiúsculas ou minúsculas.

nome = input('Digite seu nome: ')
x = len(nome) - 1
while x >= 0:
    letra = nome[x]
    x -= 1
    print(f'{letra.upper()}', end='')
