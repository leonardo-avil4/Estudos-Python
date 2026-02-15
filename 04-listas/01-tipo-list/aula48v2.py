
"""
    Prática com listas
"""

# lista = []
# lista[0] = 1
# IndexError: list assignment index out of range
# → A lista precisa de um valor no índice especificado para poder alterar o valor

lista = [True, 123, 1.0]
print(lista)

lista[0] = 'list'
print(lista)

lista2 = [False, 456, 1.5, True, [True, 1010, 'Python'], 'Python']
print(lista2) # [False, 456, 1.5, True, [True, 1010, 'Python'], 'Python']
print()

print(lista2[4]) # [True, 1010, 'Python']
print(lista2[4][-1]) # Python → -1 acessa o último item da lista

lista2[4][-1] += ' 3.13.7'
print(lista2[4])
print(lista2[4][-1])
