"""
Testando operadores lógicos

"""


print(1 or 2 or None or 'abc') # 1

# O fluxo de execução ocorre de cima para baixo / da esquerda para direita.
# Como nenhum parênteses foi definido, a verificação seque o fluxo da esquerda para a direita.

# O que acontece na verificação acima?
# 1 or 2 → retorna 1 (primeiro truthy)
# 1 or None → retorna 1 (primeiro truthy)
# 1 or 'abc' → retorna 1.

print()

print((1 and 0 or 'x') or not(None or True)) # x



# Portanto, a prioridade dos operadores lógicos é:
# NOT
# AND
# OR
