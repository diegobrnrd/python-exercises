# • 6. Escreva um programa que leia um arquivo em python (nome fornecido pelo usuário).
# – O programa deverá informar:
# • Quantas linhas o arquivo tem.
# • A quantidade de “print” que o codigo possui.

nome_arquivo = input('Digite o nome do arquivo: ')
contador_linhas = 0
contador_print = 0

try:
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            contador_linhas += 1
            contador_print += linha.count('print')
except FileNotFoundError:
    print('O arquivo especificado não foi encontrado.')
    exit()

print(f'''
O arquivo tem {contador_linhas} linhas.
O código possui {contador_print} ocorrência(s) da palavra "print".
''')
