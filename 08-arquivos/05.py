# • 5. Faça um programa que leia as linhas de 3 a 5 de um arquivo de texto (considere que tem mais do que 5 linhas).
# – Copie as linhas selecionadas em um novo arquivo.

arquivo_entrada = 'nomes_ordenados.txt'
arquivo_saida = 'linhas_selecionadas.txt'
with open(arquivo_entrada, 'r') as arquivo:
    lista_linhas = arquivo.readlines()
with open(arquivo_saida, 'w') as arquivo:
    for linha in range(2, 5):
        arquivo.write(lista_linhas[linha])
