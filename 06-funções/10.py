# 10. Faça um programa que permita ao usuário digitar o seu nome e em seguida o programa chama uma função que retorna
# o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome,
# o usuário pode digitar letras maiúsculas ou minúsculas.

def inverte_nome_m(nome):
    x = len(nome) - 1
    nome_invertido = ''
    while x >= 0:
        nome_invertido += nome[x]
        x -= 1
    return nome_invertido.upper()


nome = input('Digite seu nome: ')
nome_invertido_m = inverte_nome_m(nome)
print(nome_invertido_m)
