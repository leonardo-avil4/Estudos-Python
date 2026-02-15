"""

    Listas em Python ou Array
    Tipo list - mutável

    Suporta vários valores de qualquer tipo
    Conhecimentos reutilizáveis - índices e fatiamento
    Métodos úteis: append, insert, pop, del, clear, extend, +

"""
#         01234
#        -54321
string = 'ABCDE' # 5 caracteres (len)


# Formas de criar uma lista
# lista = list () → Em type conversion

# Porém a forma mais comum é:

#         0     1     2        3    4
#         -5    -4    -3       -2   -1
lista = [123, True, 'Python', 1.2, []]
print(lista, type(lista))
# list é um tipo mutável

# print(bool(lista)) # lista vazia → False

print(lista[2].upper(), type(lista[2])) # PYTHON <class 'str'>
print()

print(lista[-5]) # 123
lista[-5] = False
print(lista)

# Acessando a lista dentro da lista (-1)
#   lista[-1][0] = 'teste'
#   IndexError: → Erro ao acessar um índice que não existe (não possui valor neste índice)

print(lista)
