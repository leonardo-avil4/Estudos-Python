"""
    Fatiamento de Strings

    012345678
    Olá Mundo
   -987654321

   O índice 0 já está sendo utilizado para se referir ao primeiro caractere, por isso que os negativos começam com -1
"""

# Função len
# → Retorna a quantidade de caracteres da str

var = 'Olá Mundo'
print(var[-len(var)]) # O

# Fatiamento de Strings → Possibilita você pegar uma fatia da string.
# [i:f:p] → inicio:fim:passo
# : → indica o fatiamento
# o item indicado no índice final não será incluído

print(var[4:]) # Mundo
# Começa do índice 4 e vai até o final.

print(var[:4 + 1]) # Olá M
# índice 4 → M, porém índice final não é incluído, portanto para incluir o 4 soma mais 1 (:4 + 1)

print(var[-8:]) # lá Mundo

print(len(var)) # 9
# Contagem x Índices
# → Contagem → Total de caracteres.
# → Índice → Posição de um caractere na string (começa com 0)

print()

# Inverter a string

print(var[::-1]) # odnuM álO
print(var[-1:-10:-1]) # odnuM álO
