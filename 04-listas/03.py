# 3. Ler uma lista com 4 notas, em seguida o programa deve exibir as notas e a média.

N = []
for i in range(1, 5):
    nota = float(input(f'{i}ª nota: '))
    N.append(nota)
x = 1
print()
for nota in N:
    print(f'{x}ª nota: {nota}')
    x += 1
print(f'Média das notas: {sum(N) / 4:.2f}')
