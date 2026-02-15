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


# Um else associado à um while é executado quando a expressão desse while se torna Falsa.

# Exemplo de uso da estrutura while/else:
# → Percorrer um objeto iterável para procurar algum dado:
#   Dado encontrado → Utilizar o break para sair do laço.
#   Dado não encontrado → O else é executado quando não foi possível encontrar o dado desejado.
