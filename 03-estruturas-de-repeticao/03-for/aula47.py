import os
import time

"""
    Faça um jogo para o usuário adivinhar qual a palavra secreta.
    - Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
    - Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
        - Se a letra digitada estiver na palavra secreta; exiba a letra;
        - Se a letra digitada não estiver na palavra secreta; exiba *;.
    Faça a contagem de tentativas do seu usuário.
"""

palavra_secreta = input('Informe a palavra secreta: ')
palavra = ''
tentativas = 1
acertou = False

while not acertou:

    # os.system('cls')
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra.')
        time.sleep(2)
        continue

    if letra in palavra_secreta:

        for l in palavra_secreta:
            if letra == l:
                palavra += l
            else:
                palavra += '*'
        else:
            print(palavra)

    tentativas += 1
    