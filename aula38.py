"""
Estrutura de Repetição while (enquanto)

executa a mesma ação enquanto uma expressão for verdadeira
loop infinito → quando o bloco de código de alguma estrutura repete infinitamente devido a sua expressão ser sempre verdadeira.

"""


qtd_linhas = 5
qtd_colunas = 5

linha = 1

print('   1    2    3    4    5')
while linha <= qtd_linhas:
    print(linha, end='')

    linha += 1
    coluna = 1

    while coluna <= qtd_colunas:
        print(' [ ] ', end='')
        coluna += 1
    print()

print('-' * 40)

