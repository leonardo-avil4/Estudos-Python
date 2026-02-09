
# Uma introdução às f-strings (formatação de strings)

nome = 'Pycode'
peso = 90
altura = 1.80
imc = peso / (altura * altura)


# As f-strings possibilitam usar valores de variáveis dentro de uma string.

linha_1 = f'{nome} tem {altura:.2f} de altura.'
linha_2 = f'{nome} pesa {peso}Kg. IMC: {imc:.2f} '
print(linha_1)
print(linha_2)
