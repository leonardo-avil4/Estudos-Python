# Precedência entre os operadores aritméticos

"""
1. (n + n) → os parênteses são resolvidos de dentro para fora, do mais interno para o mais externo.
2. **
3. * / // %
4. + - 
→ Operadores que fazem parte da mesma precedência são executados da esquerda para a direita.

"""

conta_1 = 1 + 1 ** 5 + 5
print(conta_1) # 7

conta_2 = (1 + 1) ** 5 + 5
print(conta_2) # 37

conta_3 = (1 + 1) ** (5 + 5)
print(conta_3) # 1024

conta_4 = (1 + int(0.5 + 0.5) ** (5 + 5))
print(conta_4) # 2

conta_5 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_5) # 1024

# Sobre o valor de uma variável → se no seu código, várias atribuições foram feitas na mesma variável, o valor considerado será o da última atribuição feita.

