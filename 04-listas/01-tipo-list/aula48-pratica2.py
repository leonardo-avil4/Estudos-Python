
"""
    Prática rápida com métodos de listas
    
"""

lista = [10, 50, 60, 70, 90]
lista.append('Python')

print(lista) # [10, 50, 60, 70, 90, 'Python']

lista.insert(2, 99)
print(lista) # [10, 50, 99, 60, 70, 90, 'Python']

lista.pop()
print(lista) # [10, 50, 99, 60, 70, 90]

lista.insert(100, 'C')
# índice maior que o tamanho da lista → adiciona o valor ao final.

print(lista) # [10, 50, 99, 60, 70, 90, 'C']
print(len(lista)) # 7
