# • 6. Desenvolva um jogo da forca. Considere que o programa já  leu do arquivo uma palavra e está com essa palavra
# guardada  em uma variável. O jogo deve pedir ao usuário uma letra por vez. O jogador poderá errar 6 vezes antes de
# ser enforcado.

# Ex:
# • Digite uma letra: A
# • -> Você errou pela 1ª vez. Tente de novo!
# • Digite uma letra: O
# • A palavra é: _ _ _ _ O
# • Digite uma letra: E
# • A palavra é: _ E _ _ O
# • Digite uma letra: S
# • -> Você errou pela 2ª vez. Tente de novo!

palavra = "exemplo"
palavra_oculta = ['_' for letra in palavra]
tentativas = 0

while tentativas < 6:
    print('A palavra é: ', ' '.join(palavra_oculta))
    letra = input('Digite uma letra: ')

    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                palavra_oculta[i] = letra
    else:
        tentativas += 1
        print(f'-> Você errou pela {tentativas}ª vez. Tente de novo!')

    if '_' not in palavra_oculta:
        print('Parabéns, você ganhou! A palavra era: ', ''.join(palavra_oculta))
        break

if tentativas == 6:
    print('Você foi enforcado!')