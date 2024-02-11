# 5. Faça um programa que lê uma string e conta quantas vezes o substring “ado” aparece na string.

string = 'ado ado ado cada um no seu quadrado'
vezes = 0
index = 0
while index != -1:
    index = string.find('ado', index)
    if index != -1:
        index += 1
        vezes += 1
print(f"Quantidade de 'ado' na string: {vezes}")
