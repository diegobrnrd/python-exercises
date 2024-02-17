# • 4. Considere um sistema onde os dados são armazenados em dicionários. Nesse sistema existe um dicionario principal
# e o dicionário de backup. Cada vez que o dicionário principal atinge tamanho 5, ele imprime os dados na tela e apaga
# o seu conteúdo. Crie um programa que insira dados em um dicionário, realizando o backup a cada dado e excluindo os
# dados do dicionário principal quando ele atingir tamanho 5.

d = {}
db = {}
while True:
    resposta = input('Digite C para cadastrar e S para sair: ')
    if resposta.upper() == 'S':
        break
    elif resposta.upper() != 'S' and resposta.upper() != 'C':
        print('Resposta inválida!')
    else:
        produto = input('Digite o nome do produto: ')
        preco = float(input('Digite o preço do produto: '))
        d[produto] = preco
        if len(d) == 5:
            for produto in list(d.keys()):
                db[produto] = d.pop(produto)
