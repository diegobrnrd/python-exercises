# 8. Faça um programa que crie uma matriz M (com valores informados do usuário) e mostre a matriz com o dobro dos
# valores lidos (2*M).

num_linha = int(input('Digite a quantidade de linhas da matriz: '))
num_coluna = int(input('Digite a quantidade de colunas da matriz: '))

matriz = []

for i in range(num_linha):
    linha = []
    for j in range(num_coluna):
        valor = float(input(f'Digite o valor para a posição ({i + 1}, {j + 1}): '))
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    for valor in linha:
        print(f'{valor * 2:8.2f}', end=' ')
    print()
