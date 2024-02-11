# • 7. Uma string é utilizada para representar uma das fitas de uma cadeia de DNA. Para tanto, as bases Adenina,
# Guanina, Citosina, Timina e Uracila são representadas pelas letras A, G, C, T e U, respectivamente. Deseja-se
# construir um programa que dada uma sequência de DNA é fornecida a sequência de RNA-m equivalente de acordo com
# a transformação indicada na Tabela 1.

# DNA   RNA-m
# A     U
# G     C
# C     G
# T     A

dna = 'agct'
rna_m = ''
for letra in dna:
    if letra == 'a':
        letra = 'u'
        rna_m += letra
    elif letra == 'g':
        letra = 'c'
        rna_m += letra
    elif letra == 'c':
        letra = 'g'
        rna_m += letra
    elif letra == 't':
        letra = 'a'
        rna_m += letra
