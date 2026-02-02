# Introdução aos operadores aritméticos

# Operação entre ints → resultado: inteiro
# Operação entre int e float → resultado: float
# Operação entre floats → resultado: float

adicao = 10 + 10
print('Adição: ', adicao) # 20
   
subtracao = 10 - 5
print('Subtração: ', subtracao) # 5

multiplicacao = 10 * 10
print('Multiplicação: ', multiplicacao) # 100

divisao = 10 / 2.2 # sempre retorna float
print('Divisão: ', divisao) # 4.54545454545

divisao_inteira = 10 // 2.2
# entre int e float → retorna float sem as casas decimais.
# entre ints → retorna int

print('Divisão inteira: ', divisao_inteira) # 4.0

potenciacao = 2 ** 10
print('Potenciação: ', potenciacao) # 1024


modulo = 25 % 2 # resto da divisão
print('Resto da divisão (módulo): ', modulo) # 1
# O resto é muito utilizado para descobrir se um número é múltiplo de outro.
