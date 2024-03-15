# 9. Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve
# converter 14:25 em 2:25 P.M; 6:44 em 6:44 A.M. A entrada é dada em dois inteiros. O programa deve ler várias entradas
# e chamar uma função para convertê-las e em seguida imprimir a saída.

def converte_horas(horas_c):
    if horas_c == 0:
        return 12, 'A.M.'
    elif horas_c < 12:
        return horas_c, 'A.M.'
    elif horas_c == 12:
        return 12, 'P.M.'
    else:
        return horas_c - 12, 'P.M.'


horas = -1
minutos = -1

while True:
    horas = int(input('Digite as horas (formato 24h): '))
    if 0 <= horas < 24:
        break
    else:
        print('Hora inválida!')

while True:
    minutos = int(input('Digite os minutos: '))
    if 0 <= minutos < 60:
        break
    else:
        print('Minuto inválido!')

convertido, periodo = converte_horas(horas)
print(f'{convertido}:{minutos:02d} {periodo}')

