
frase_original = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido Van Rossum.'
frase = frase_original.lower().replace(' ', '').replace('.', '')

i = 0
letra_atual = ''
vezes = 0

# Iteração por cada caractere da string
while i < len(frase):
    total_letra_atual = frase.count(frase[i])
   
    if total_letra_atual > vezes:
        vezes = total_letra_atual
        letra_atual = frase[i]

    i += 1

print()
print(f'Na frase "{frase_original}" A letra que mais apareceu foi "{letra_atual}", totalizando {vezes} vezes.')
