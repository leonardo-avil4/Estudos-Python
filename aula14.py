# Formatação de strings com o método .format

a = 'A'
b = 'B'
c = 1.1
formato = 'a={} b={} c={:.2f}'.format(a, b, c)
#  Os valores de cada chave vão ser referentes a posição de cada variável
# primeira chave → valor de a

# Também é possível especificar por índices

index_format = 'b={2} a={0} b={1} c={2:.2f} a={0} c={2:.2f}'.format(a, b, c)

print(formato)
print(index_format)


# Tudo em python é um objeto, e objetos possuem métodos. Os métodos são ações que objetos podem fazer.
# → Uma função dentro de um objeto é um método.

# Sobre erros "out of range"
# → Indicam que você está tentando buscar algo que já acabou ou que está fora do alcance.
# → Comum em: listas, loop for


print('{} {} {}'.format(a, b, c))
