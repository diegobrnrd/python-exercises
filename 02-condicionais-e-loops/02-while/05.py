# 5. Faça um algoritmo que peça dois números – base e expoente – calcule e mostre o primeiro número elevado ao
# segundo número. Não utilize a função de potência da linguagem.

base = float(input('Digite a base: '))
expoente = int(input('Digite o expoente (inteiro positivo): '))
expo = expoente
resultado = 1

while expo > 0:
    resultado *= base
    expo -= 1

print(f'{base}^{expoente} = {resultado}')
