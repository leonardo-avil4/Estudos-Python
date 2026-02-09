"""

Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = É ou Não é (tipo, valor, identidade)

id = identidade

"""

# Flags são utilizadas para verificar se o interpretador do Python passou em algum local do código (Demarcar um local no código.).
# → Rastrear o estado de uma parte no código
# → Indicar se o programa passou por um determinado ponto no código
# → Indicar que um evento ocorreu.

passou_no_if = None # flag deve ser inicializada com o valor None (não valor)
condicao = True

if condicao:
    passou_no_if = True
    print("Passou no if.")
else:
    print("Não passou no if.")

print(passou_no_if, passou_no_if is None) # True False
print(passou_no_if, passou_no_if is not None) # True True

# is None → É None?
# is not None → Não é None?
# → Ambos operadores retornam um valor lógico.
