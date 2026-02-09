"""
    Exercício - Iterando com strings
"""
nome = input("Digite o seu nome: ")
tam_nome = len(nome)
nova_string = ''
indice = 0

while indice < tam_nome:
    nova_string += f'*{nome[indice]}'
    indice += 1
    
print(nova_string)
