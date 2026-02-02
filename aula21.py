
# Operadores Lógicos
# → Os operadores lógicos testam/verificam duas ou mais expressões e retornam um valor booleano.

# and (e)
# verifica duas ou mais expressões e retorna verdadeiro se todas as expressões forem verdadeiras.

# Valores falsy, são valores dos tipos de dados que são considerados como False em uma estrutura condicional.
# 0 0.0 '' False None
# → None é usado para representar um não valor.

# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor.

# Short Circuit Avaliation
# → Retorna o primeiro valor falsy encontrado.
print(True and 0 and '') # 0


# Por outro lado, se todos os valores forem truthy, o último valor truthy é retornado.
print(True and 1 and 'xpto') # 'xpto'


if(None):
    print('oi')
else:
    print('none.')
