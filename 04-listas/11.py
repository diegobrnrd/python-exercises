# 11. Uma empresa de pesquisas precisa tabular os  resultados da seguinte enquete feita a um grande quantidade de
# organizações: "Qual o melhor Sistema  Operacional para uso em servidores?" As possíveis  respostas são:

# • 1 - Windows XP 2 - Unix 3 - Linux 4 - Netware 5 - Mac OS 6 - Outro
# • Você deve desenvolver um programa em Python que  leia as respostas da enquete e informe  ao final o resultado da
#   mesma. O programa deverá ler os valores  até ser informado o valor 0 (zero), que encerra a entrada dos dados.
#   Não deverão ser aceitos valores  além dos válidos para o programa (0 a 6).
# • Os valores referentes a cada uma das opções devem  ser armazenados em uma lista.
#   Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada uma das
#   respostas e informar o vencedor da enquete.
#   O formato da saída foi dado pela empresa, e é o seguinte:
#  Sistemas Operacionais - Votos %
#  Windows XP 1500 17%
#  Unix 3500 40%
#  Linux 3000 34%
#  Netware 500 5%
#  Mac OS 150 2%
#  Outro 150 2%
#  Total de 8800 votos
#  O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.

R = []

print(f'''
1 - Windows XP'
2 - Unix'
3 - Linux'
4 - Netware'
5 - Mac OS'
6 - Outro
''')

while True:
    r = int(input('Qual o melhor Sistema  Operacional para uso em servidores?'
                  '\n(Responda com o apenas o número correspondente)'
                  '\n(0 zero sai)'
                  '\nResposta: '))
    if r == 0:
        break
    elif r < 0 or r > 7:
        print('Resposta inválida! Digite uma resposta entre 0 e 6')
        continue
    else:
        R.append(r)

r1, r2, r3, r4, r5, r6 = 0, 0, 0, 0, 0, 0

for resposta in R:
    if resposta == 1:
        r1 += 1
    elif resposta == 2:
        r2 += 1
    elif resposta == 3:
        r3 += 1
    elif resposta == 4:
        r4 += 1
    elif resposta == 5:
        r5 += 1
    else:
        r6 += 1

tr = (r1 + r2 + r3 + r4 + r5 + r6)

pr1 = (r1 * 100) / tr
pr2 = (r2 * 100) / tr
pr3 = (r3 * 100) / tr
pr4 = (r4 * 100) / tr
pr5 = (r5 * 100) / tr
pr6 = (r6 * 100) / tr

opcao = {'1': 'Windows XP',
         '2': 'Unix',
         '3': 'Linux',
         '4': 'Netware',
         '5': 'Mac OS',
         '6': 'Outro'}

prpr = [pr1, pr2, pr3, pr4, pr5, pr6]
votos = [r1, r2, r3, r4, r5, r6]
maior_por = max(prpr)
indice_vencedor = prpr.index(maior_por)
vencedor = opcao[str(indice_vencedor + 1)]
quantidade_votos_vencedor = votos[indice_vencedor]

print(f'''
Sistemas Operacionais - Votos %
Windows XP {r1} votos {pr1:.2f}%
Unix {r2} votos {pr2:.2f}%
Linux {r3} votos {pr3:.2f}%
Netware {r4} votos {pr4:.2f}%
Mac OS {r5} votos {pr5:.2f}%
Outro {r6} votos {pr6:.2f}%
''')

print(f'O Sistema Operacional mais votado foi o {vencedor}, com {quantidade_votos_vencedor} votos, '
      f'correspondendo a {maior_por:.2f}% dos votos.')
