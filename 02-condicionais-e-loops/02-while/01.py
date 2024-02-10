# 1. Crie um programa que lê as idades e alturas de alguns alunos. A condição de parada é a altura = 0. Em seguida,
# o programa deve informar quantos alunos com mais de 13 anos possuem altura inferior à 1.5.

alunos_maior13_menor15 = 0
while True:
    altura = int(input('Altura do aluno (em cm): '))
    if altura == 0:
        break
    idade = int(input('Idade do aluno: '))
    if idade > 13 and altura < 150:
        alunos_maior13_menor15 += 1
print(f'Quantidade de alunos com mais de 13 anos e menor que 1.5: {alunos_maior13_menor15} aluno(s).')
