
# Operadores lógicos

# O operador or (ou) avalia toda a expressão como verdadeira se pelo menos uma condição ou teste for verdadeira.

senha_permitida = '0kmz@'

entrada = input('[E] - Entrar / [S] - Sair \n> ')


if entrada == 'E' or entrada == 'e':
    senha_digitada = input('Senha: ')
    
    if senha_digitada == senha_permitida:
        print('Acesso autorizado.')
    else:
        print('Acesso negado.')
else:
    print('Você saiu do sistema.')

# Short Circuit Avaliation 

print('' or False or 0) # 0
# Se todos os valores forem falsy, retorna o último valor falsy identificado.

print(0 or False or 0 or 'abc' or None or True) # abc
# Por outro lado, se houver pelo menos um truthy retorna o primeiro valor truthy encontrado.
