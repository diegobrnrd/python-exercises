def quantidade_digitos(n):
    return len(str(n))


def verifica_numero(n):
    if n > 0:
        return 'P'
    else:
        return 'N'


def inverte_numero(n):
    numero = str(n)
    x = len(str(n)) - 1
    numero_invertido = ''
    while x >= 0:
        numero_invertido += numero[x]
        x -= 1
    return int(numero_invertido)
