import os
import time

"""
    Calculadora com while
"""

while True:
    os.system('cls')
    print('--- CALCULADORA v0.1 ---')
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))

    print('Escolha uma opção: ')
    print('[1] - ADIÇÃO')
    print('[2] - SUBTRAÇÃO')
    print('[3] - MULTIPLICAÇÃO')
    print('[4] - DIVISÃO')
    print('-' * 20)
    print('[0] - SAIR')
    op = int(input('> '))

    if op == 1:
        print(f'A soma de {n1} com {n2} é {n1 + n2}')
    elif op == 2:
        print(f'A subtração de {n1} com {n2} é {n1 - n2}')
    elif op == 3:
        print(f'A multiplicação de {n1} com {n2} é {n1 * n2}')
    elif op == 4:
        print(f'A divisão de {n1} com {n2} é {n1 / n2:.2f}')
    elif op == 0:
        break
    else:
        print('Opção Inválida! Tente novamente.')
        time.sleep(2)
        continue

    cont = input('Você deseja continuar? [S/N] >').upper()
    if cont == 'S':
        continue
    elif cont == 'N':
        break

print('Programa finalizado.')
