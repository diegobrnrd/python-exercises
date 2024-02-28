# 5. Faça um programa que lê uma string e conta quantas vezes o substring “ado” aparece na string.

string = input('Digite uma frase: ')
string_maiuscula = string.upper()
vezes = string_maiuscula.count('ADO')

print(f'Quantidade de "ado" na string: {vezes}')
