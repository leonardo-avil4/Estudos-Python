"""
Estrutura de Repetição while (enquanto)

executa uma ação enquanto uma expressão for verdadeira
loop infinito → quando o bloco de código de alguma estrutura repete infinitamente devido a sua expressão ser sempre verdadeira.

"""

contador = 0

while contador <= 50:
    contador += 1
    
    if contador == 6:
        continue

    if contador > 10 and contador <= 30:
        continue

    print(contador)

    if contador == 40:
        break

print('Acabou')

# break → força a interrupção de todo a estrutura. Casos de usos: Buscas, saídas de erro, limites de tempo.

# continue → para de executar as próximas linhas do laço atual e pula para o próximo laço. Casos de uso: filtragem de dados, tratamento de exceções leves.
# Essas palavras-chaves são utilizadas para o laço de repetição while mais próximo delas.
