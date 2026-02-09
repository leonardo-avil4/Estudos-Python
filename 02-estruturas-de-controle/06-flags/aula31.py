

"""
id - a Identidade do valor que está na memória

Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = É ou Não é (tipo, valor, identidade)

id = identidade

"""

# A função id() retorna o número de idendidade de um valor que está na memória.
v1 = 'a'
v2 = 'a'

print(id(v1)) # 140727034605536
print(id(v2)) # 140727034605536
# Em alguns casos, os mesmos valores atribuídos à variáveis diferentes vão se referir ao mesmo ID
print()

x = 'py'
y = '123'

# Por outro lado, valores diferentes terão IDs diferentes.
print(id(x)) # 2849759871168
print(id(y)) # 2849762490624
