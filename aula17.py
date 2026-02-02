# if / elif / else
# se / se não se / se não


condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = True

if condicao1:
    print('Condição 1 → True.')
elif condicao2:
    print('Condição 2 → True.')
elif condicao3:
    print('Condição 3 → True.') # Executa somente o primeiro bloco que conter a condição verdadeira. Ao encontrar a primeira condição verdadeira, o interpretador para de executar os blocos de if/elif/else e segue para a execução das próximas linhas.
elif condicao4:
    print('Condição 4 → True.')
else:
    print('Nenhuma condição foi satisfeita.')
