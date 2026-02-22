
"""

    Listas em Python ou Array
    Tipo list - mutável

    Suporta vários valores de qualquer tipo
    Conhecimentos reutilizáveis - índices e fatiamento
    Métodos úteis: append, insert, pop, del, clear, extend, +

    Create  Read  Update      Delete (CRUD) → Operações básicas de um banco de dados.
    Criar   Ler   Atualizar   Apagar


"""
#        0   1   2   3
lista = [10, 20, 30, 40]
lista[2] = 300
numero = lista[2]
print(numero)

del lista[2] # del → deleta um índice e reorganiza os índices da lista
# del requer bastante processamento (depende do tamanho da lista), pois precisa reorganizar os índices que estão após aquele que foi deletado (move os índices uma posição para trás).

# Listas são úteis em situações onde você precisa adicionar/remover itens do final.

print(lista)
print(lista[2])

# Deck (outra estrutura) → Pode ser usado para adicionar/remover itens do começo, meio e fim da estrutura.
