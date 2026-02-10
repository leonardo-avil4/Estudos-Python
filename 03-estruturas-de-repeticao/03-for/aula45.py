"""

    Como o for funciona por baixo dos panos?

    Iterável → str, range, etc (objeto que possui um método chamado __iter__)
    Iterador → Quem sabe entregar um valor por vez
    next → me entregue o próximo valor
    iter → me entregue seu iterador

"""

# numeros = range(0, 100, 8)

# for numero in numeros:
#     print(numero)

texto = 'Python'
# print(texto.__iter__())
# dois underlines "__" são chamados de "dunder"

texto2 = iter('#Python') # A função nativa entrega o objeto iterador de um iterável
print(texto2.__next__())
print(texto2.__next__())
print(texto2.__next__())
print(texto2.__next__())
print(texto2.__next__())
print(texto2.__next__())
print(texto2.__next__()) # stop iteration
# ou next(texto2)

# next chama o próximo valor disponível no iterador
