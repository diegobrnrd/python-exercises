# 6. Ler o valor de um cheque e escrever o quanto vai ser recolhido de CPMF.
# Considere que imposto recolhe uma taxa de 0,3%. Imprimir o valor do imposto.

cheque = float(input('Valor do cheque: '))
cpmf = cheque * 0.3 / 100

print(f'Valor do cheque: R$ {cheque:.2f}'
      f'\nCPMF: R$ {cpmf:.2f}')
