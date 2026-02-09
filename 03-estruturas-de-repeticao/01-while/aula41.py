"""
    while/else
"""


string = 'Valorqualquer'
i = 0
# variável com nome 'i' é comum de ser utilizada para contar índices ou números.

while False:
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')


# Uso dessa estrutura while/else:
# → Percorrer um objeto iterável para procurar algum tipo de dado. Dado encontrado → Utilizar o break para sair do laço
# → O else é executado quando o que você procura não foi encontrado.
