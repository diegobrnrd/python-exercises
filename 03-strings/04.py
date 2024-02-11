# 4. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

# Exemplo
# F
# FU
# FUL
# FULA
# FULAN
# FULANO

nome = input('Digite seu nome: ')
x = ''
for letra in nome:
    x += letra
    print(x)
