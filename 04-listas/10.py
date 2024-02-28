# 10. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#  "Telefonou para a vítima?"
#  "Esteve no local do crime?"
#  "Mora perto da vítima?"
#  “Tinha dívidas com a vítima?"
#  "Já trabalhou com a vítima?“
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder
# positivamente a 2 questões ela deve ser classificada como "Suspeita“; entre 3 e 4 como "Cúmplice" e; 5 como
# "Assassino".  Caso contrário, ele será classificado como "Inocente".

perguntas = ['Telefonou para a vítima?',
             'Esteve no local do crime?',
             'Mora perto da vítima?',
             'Tinha dívidas com a vítima?',
             'Já trabalhou com a vítima?']

print(f'Responda com S para sim e N para não.')

x = 0
resposta_positiva = 0
while x <= 4:
    resposta = input(f'{perguntas[x]}: ')
    if resposta.lower() != 's' and resposta.lower() != 'n':
        continue
    elif resposta.lower() == 's':
        resposta_positiva += 1
        x += 1
    elif resposta.lower() == 'n':
        x += 1

veredito = ['Inocente',
            'Suspeita',
            'Cúmplice',
            'Cúmplice',
            'Assassino']

print(f'Veredito: {veredito[resposta_positiva - 1]}')
