# 4. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

from funcoes import inverte_numero

numero = int(input('Digite um número inteiro: '))
numero_invertido = inverte_numero(numero)
print(numero_invertido)
