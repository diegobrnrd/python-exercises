# 11. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por
# extenso. O programa deve chamar uma função que retorna o mês convertido. Exemplo:
# – Entrada - Data de Nascimento: 29/10/1973
# – Saída - Você nasceu em 29 de Outubro de 1973.

def data_nascimento_extenso(data_nascimento):
    data = data_nascimento.split('/')
    dia = int(data[0])
    mes = int(data[1])
    meses = ['Janeiro', 'Fervereiro', 'Março', 'Abril',
             'Maio', 'Junho', 'Julho', 'Agosto',
             'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    mes_escrito = meses[mes - 1]
    ano = int(data[2])
    return f'Você nasceu em {dia} de {mes_escrito} {ano}'


teste = input('Digite sua data de nascimento no formato (dd/mm/aaaa): ')
data_escrito = data_nascimento_extenso(teste)

print(data_escrito)
