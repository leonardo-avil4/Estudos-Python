# Operador lógico "not"
# → Usado para inverter o valor lógico de uma expressão.

# not True = False
# not False = True

usuario = input('Digite seu usuario:  ')

# not usuario (falsy) → true
# not usuario (truthy) → false

if not usuario:
    print('Você não digitou nada')
else:
    senha = input('Digite sua senha: ')

    if senha == 'kzm@':
        print('Acesso autorizado.')
    else:
        print('Acesso negado.')
