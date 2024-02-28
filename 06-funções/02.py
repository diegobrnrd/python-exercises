# 2. Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado pelo usuário.

from funcoes import quantidade_digitos

numero = int(input('Digite um número inteiro: '))
quantidade = quantidade_digitos(numero)

print(f'{numero} tem {quantidade} digito(s).')
