# 3. Fazer uma função que recebe um argumento inteiro. A função retorna o valor de caractere ‘P’, se seu argumento for
# positivo, e ‘N’, se seu argumento for zero ou negativo.

from funcoes import verifica_numero

numero = int(input('Digite um número inteiro: '))
retorno = verifica_numero(numero)
print(retorno)
