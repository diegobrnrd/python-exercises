# 3. Escreva um programa que lê um arquivo contendo endereços IPs, da seguinte forma:

# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 257.32.4.5
# 85.345.1.2
# 1.2.3.4
# 9.8.234.5
# 192.168.0.256

# • O programa deve mostrar os IPS indicando os que são validos e inválidos (um endereço ip válido não pode ter uma de
# suas partes maior que 254).

with open('ips.txt', 'r') as arquivo:
    for linha in arquivo:
        print(f'Analisando IP: {linha.strip()}')
        ip = linha.strip().split('.')
        valido = True
        for parte in ip:
            if int(parte) > 254:
                valido = False
                break
        if valido:
            print('IP válido.')
        else:
            print('IP inválido.')
