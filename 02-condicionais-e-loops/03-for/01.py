# 1. Uma fábrica tem 10 representantes. Cada um recebe uma comissão calculada a partir do número de itens de um
# pedido, segundo os seguintes critérios:

# – para até 19 itens vendidos, a comissão é de 10% do valor total do pedido;
# – para pedidos de 20 e 49 itens, a comissão é de 15% do valor total do pedido;
# – para pedidos de 50 a 74 itens, a comissão é de 20% do valor total do pedido; e
# – para pedidos iguais ou superiores, a 75 itens a comissão é de 25%.

# Faça um programa que lê a quantidade de itens de pedidos de cada representante e imprime o percentual de comissão
# de cada um.

for v in range(1, 11):
    itens = int(input(f'Quantidade vendida ({v}º vendedor): '))
    if itens >= 75:
        print(f'Comissão do vendedor {v}: 25%.')
    elif itens >= 50:
        print(f'Comissão do vendedor {v}: 20%.')
    elif itens >= 20:
        print(f'Comissão do vendedor {v}: 15%.')
    else:
        print(f'Comissão do vendedor {v}: 10%.')
