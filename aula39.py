"""
    Iterando strings com while
"""


nome = input("Digite o seu nome: ")
tam_nome = len(nome)
nova_string = ''

indice = 0
while indice < tam_nome:

    if indice == 0:
        nova_string += '*'
    
    if indice < tam_nome - 1:
        nova_string += nome[indice]+'*'
    else:
        nova_string += nome[indice]
    
    indice += 1

print(nova_string)
