"""
20. Fazer um programa para: 
    a. receber 10 números inteiros do usuário em um array 

    b. copiar os pares para o array pares e os ímpares para o array ímpares, na 
    ordem em que aparecem 

    c. mostrar os arrays resultantes no final 

    Ex: se o usuário forneceu: 7, 4, 2, 9, 3, 5, 0, 2, 3, 6 
    o array pares deve conter: 4, 2, 0, 2, 6 
    o array ímpares deve conter: 7, 9, 3, 5, 3

"""

array = []
pares = []
impares = []

for i in range(10):
    n = int(input('Digite um número: '))
    array.append(n)

    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(array)
print(pares)
print(impares)
