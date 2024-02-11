# • 1. Faça um programa que escreve uma frase digitada pelo usuário em um arquivo. Em seguida o programa deve ler e
# imprimir o conteúdo desse arquivo.

frase = input('Digite uma frase: ')
with open('frase.txt', 'w') as arquivo:
    arquivo.write(frase)
with open('frase.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(f"Conteúdo do arquivo 'frase.txt': {conteudo}")
