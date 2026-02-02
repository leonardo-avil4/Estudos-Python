# Operadores in e not in
# in → 'está entre'
# not in → 'não está entre'

# String são iteráveis
#  0 1 2 3 4 5
#  P y t h o n
# -6-5-4-3-2-1

# Um iterável é um objeto onde você pode navegar entre seus itens ou índices.

string = 'Python'

print(string[0]) # P
print(string[-1]) # n
print('y' in string) # True
print('p' in string) # False → python é case sensitive.

# O python checa caractere por caractere e retorna um valor booleano indicando se o valor informado está contido na string.


print('on' in string) # True
print()

# not in é o inverso, ele verifica se o valor informado NÃO ESTÁ contido.

print('abc' not in string) # True
print('Py' not in string) # False
