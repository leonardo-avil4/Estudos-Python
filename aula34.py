"""
Estrutura de repetição
while (enquanto)
→ Executa a mesma ação (ou bloco de código) enquanto uma expressão for verdadeira.

"""

condicao = True

while condicao:
    nome = input('Seu nome: ')
    if nome.lower() == 'sair':
        break
    else:
        print(f'Seu nome é {nome}')


# A palavra-chave break é utilizada para forçar a interrupção do laço. Ela procura o laço de repetição mais próximo.

