# 3. Entrar com um distância (km) e o tempo de viagem (horas) de um automóvel, e dizer se a velocidade média foi
# superior ao limite (110 km/h) ou não.

distancia = float(input('Distância (km): '))
tempo = float(input('Tempo de viagem (horas): '))
velocidade_media = distancia / tempo

if velocidade_media > 110:
    print('Você ultrapassou o limite máximo de 110km/h')
else:
    print('Você respeitou o limite de velocidade de 110km/h')
