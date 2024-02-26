# • Fazer uma função que receba como parametro um numero inteiro e retorne o fatorial desse numero (não usar
# recursividade).

def fatorial_while(n):
    fat = 1
    x = 1
    while x <= n:
        fat *= x
        x += 1
    return fat


teste_while = fatorial_while(7)
print(teste_while)


def fatorial_for(n):
    fat = 1
    for x in range(n):
        fat *= x+1
    return fat


teste_for = fatorial_for(7)
print(teste_for)
