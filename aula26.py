"""
Formatação de strings com f-strings

s - string
d - int
f - float
    → .(nº casas decimais)f

x e X
    → Hexadecimal

> - Esquerda
< - Direita
^ - Centro

Sinal - + ou -

Conversion flags - !r (__repr__) !s (__str__) !a (__?__)
"""

# padding → adicionar caracteres até atingir a quantidade especificada.

var = 'ABC'
print(f'{var: >10}.')
# Preenche a string com espaços vazios até o seu tamanho ser de 10 caracteres.
# Como a minha string 'ABC' já tem 3 caracteres e faltam 7 para 10, então será preenchida com 7 espaços vazios.

# {var:char (s) len}
# char → caractere utilizado para preencher.
# s → onde o preenchimento será feito (esquerda, direita ou centro)
# len → tamanho desejado.

print(f'{var: <10}.')
print(f'{var:-^13}')

print(f'{var:0^11}')

print()
print('-' * 50)
print()

# sinais

print(f'{123.56887:-.1f}')
# - mostra o sinal de negativo somente se o número for negativo.

print(f'{1278.999:+.1f}')
print(f'{-7851.213:+.1f}')
# + mostra o sinal de positivo somente se o número for positivo.
print(f'{var!s}')
