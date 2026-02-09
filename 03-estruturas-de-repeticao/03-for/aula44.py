"""
    For + Range
    range → range (start, stop, step)
"""

numeros = range(0, 10)
# A função range cria um objeto de números inteiros iteráveis.

# range(5) → 0, 1, 2, 3, 4
# range(2, 6) → 2, 3, 4, 5
# range(1, 10, 2) → 1, 3, 5, 7, 9
# → O valor de parada (stop) nunca é incluído.


print(numeros)

# O for percorre por cada valor de um objeto iterável. Não é necessário se preocupar com índices como era no caso do while.

for numero in numeros:
    print(numero)
