
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
print(numero) # 300

del lista[2] # del → deleta um índice e reorganiza os índices da lista
# del requer bastante processamento (em listas grandes), pois precisa reorganizar os índices que estão após aquele que foi deletado (move os índices uma posição para trás).

# Listas são úteis em situações onde você precisa adicionar/remover itens do final.
# Deck (outra estrutura) → Pode ser usado para adicionar/remover itens do começo, meio e fim da estrutura.

print(lista) # [10, 20, 40]
print(lista[2]) # 40

# Método append → Adiciona um item ao final da lista.
lista.append(50)
lista.append(60)
lista.append('70')
 
# Método pop → Remove um item específico e retorna seu valor. Remove o último item se nenhum argumento for informado.
removido = lista.pop()
print(lista) # [10, 20, 40, 50, 60]
print(f'Valor removido: {removido} - {type(removido)}') # Valor removido: 70

lista.pop(0)
print(lista) # [20, 40, 50, 60]
