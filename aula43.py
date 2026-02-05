"""
    Introdução ao for in - estrutura de repetição para coisas infinitas.
"""

texto = 'Python'

# O while não é muito comum de ser usado em situações onde você sabe o número de repetições necessárias.
# → O while é recomendado em situações onde não se sabe precisamente o número de repetições que vão ocorrer. 

# Ex: situações dinâmicas onde uma interação específica dita se a repetição será executada
# → Se o usuário digitar uma senha diferente daquela que está salva no banco de dados, permanecer na página de login

# for letra in texto:
#     print(letra)


# for é um laço que percorre itens de uma sequência (strings, listas ou um intervalo de um número)
novo_texto = ''
for letra in texto:
# Iteráveis entregam um valor por vez
    novo_texto += f'*{letra}'
    print(letra)

print(novo_texto)
