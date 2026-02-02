
# Conversão de tipos, coerção

# Type convertion / typecasting / coercion
# É o ato de converter um tipo em outro tipos imutáveis e primitivos

# Concatenar → Juntar duas coisas.
print('a' + 'b') # ab

# Tipagem fraca → Não possui restrições em relação à operações entre tipos diferentes.

# Python é uma linguagem de tipagem forte e dinâmica.


# Existem alguns valores de um tipo de dado no qual é possível converter para outro tipo.


print(float('1') + 2) # 3.0
print(type(float('1') + 2))

# print(float('a') + 1) 
# → ValueError: could not convert string to float: 'a'

print(str(11) + 'b') # 11b

# bool
# → retorna True ou False dependendo do valor do tipo de dado passado

print(bool('')) # False
print(bool(' ')) # True
print(bool('py')) # True
print(bool(0)) # False
print(bool(1)) # True
print(bool(-1)) # True
