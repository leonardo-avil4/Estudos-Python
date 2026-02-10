"""

    Recriando o funcionamento do for utilizando while

"""

string = 'Python'
iterator = string.__iter__()
# retorna o objeto iterador da string

while True:
    try:
        print(iterator.__next__())
        # retorna o próximo item 
    except StopIteration:
        break


# Pode-se concluir que for precisa de um objeto com o método __iter__ para funcionar.
