# Usando a função input para coletar dados do usuário

nome = input('Qual o seu nome? ')
# → A função input sempre retorna o dado digitado no tipo str.

print(f'O seu nome é {nome}')

numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))
soma = numero_1 + numero_2
print(f'A soma é {soma}')
