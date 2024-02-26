# 1. Faça uma função chamada somaImposto. A função possui dois parâmetros:
# a) taxaImposto, que é a porcentagem de imposto sobre vendas
# b) custo, que é o custo de um item antes do imposto.
# A função retorna o valor de custo alterado para incluir o imposto sobre vendas.

def soma_imposto(taxa_imposto, custo):
    return custo + custo * (taxa_imposto / 100)


teste = soma_imposto(50, 1000)
print(f'R$ {teste:.2f}')
