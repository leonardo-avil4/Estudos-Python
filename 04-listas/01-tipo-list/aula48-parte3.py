"""

    Listas (array) Python
    Tipo list - mutável

    Suporta vários valores de qualquer tipo
    Conhecimentos reutilizáveis - índices e fatiamento
    Métodos úteis: 
        append → Adiciona um item ao final
        insert → Adiciona um item no índice escolhido
        pop → Remove do final ou do índice escolhido
        del → Apaga um índice
        clear → limpa a lista
        extend → estende a lista
        + → concatena listas


    Create  Read  Update      Delete (CRUD) → Operações básicas de um banco de dados.
    Criar   Ler   Atualizar   Apagar

"""

lista = [10, 20, 30, 40]
lista.append('Python')

print(lista) # [10, 20, 30, 40, 'Python']
print(lista, lista.pop()) # [10, 20, 30, 40] Python
# → Executa primeiro o método e depois exibe.

# lista.clear()

# argumentos do insert → índice, valor
lista.insert(0, 5)
# → Adiciona o valor 5 no índice 0 da lista. Os próximos índices serão reorganizados (movidos para direita).
print(lista) # [5, 10, 20, 30, 40]
print()

lista.insert(999, 50)
# Se um índice que não existe na lista for especificado, o valor será adicionado ao final da lista.
print(lista, len(lista)) # [5, 10, 20, 30, 40, 50] 6

# print(lista[999]) IndexError: list index out of range