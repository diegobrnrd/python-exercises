# 4. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

# Exemplo
# F
# FU
# FUL
# FULA
# FULAN
# FULANO

nome = input('Digite seu nome: ')
letras = ''

for letra in nome:
    letras += letra
    print(letras.upper())
