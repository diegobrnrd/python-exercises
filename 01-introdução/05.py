# 5. Faça um programa para ler o salário de um funcionário e aumentá-lo em 20%. Imprima seu salário final.

salario = float(input('Informe seu salário: '))
aumento = salario * 20 / 100
salario_final = salario + aumento

print(f'''
Antigo salário: R$ {salario:.2f}
Novo salário: R$ {salario_final:.2f}
Aumento: R$ {aumento:.2f}
''')
