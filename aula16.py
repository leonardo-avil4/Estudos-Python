# if / elif / else
# se / se não se / se não

# Operações/Comandos que mudam o fluxo de execução do código com base em uma decisão ou valor escolhido, o que faz com que um bloco de código específico seja executado.

# Bloco de código
# → Um conjunto de zero ou mais instruções que pertencem a uma estrutura de controle.

entrada = input('Você quer "entrar" ou "sair"? ')

# Se a expressão for verdadeira, o bloco de código do if é executado.
if entrada == 'entrar':
    print('Você entrou no sistema.')
elif entrada == 'sair':
    print('Você saiu do sistema.')
else: # É executado se nenhuma das outras condições acima forem atendidas.
    print('Você não digitou nem entrar nem sair')

# Dessa forma, somente um dos blocos será executado dependendo do resultado da condição.


# if / elif e else dependem um do outro.
