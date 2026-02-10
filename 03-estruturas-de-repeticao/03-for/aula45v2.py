"""

    Recriando o funcionamento do for utilizando while

"""

string = 'Python'
iterator = string.__iter__()
# retorna o objeto iterador da string

while True:
    try:
        print(iterator.__next__())
        # O método "__next__" de um iterável retorna o valor atual e aponta para o próximo item do iterável.
    except StopIteration:
        break


# Pode-se concluir que for precisa de um objeto com o método __iter__ para funcionar.
