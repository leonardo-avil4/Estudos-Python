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

palavra_secreta = input('Informe a palavra secreta: ').lower()
letras_acertadas = ''
tentativas = 0
acertou = False
palavra_formada = ''

while not acertou:

    os.system('cls')

    if palavra_formada:
        print(f'Palavra formada: {palavra_formada}')

    letra = input('Digite uma letra: ').lower()

    if len(letra) > 1:
        print('Digite apenas uma letra.')
        time.sleep(2)
        continue

    acertouLetra = letra in palavra_secreta and letra not in letras_acertadas
    if acertouLetra:
        letras_acertadas += letra

    palavra_formada = ''
    for l in palavra_secreta:
        if l in letras_acertadas:
            palavra_formada += l
        else:
            palavra_formada += '*'

    tentativas += 1
    if palavra_formada == palavra_secreta:
        acertou = True

os.system('cls')
print(f'A palavra secreta era: {palavra_secreta}')
print(f'Parabéns! Você acertou. Total de tentativas: {tentativas}')
