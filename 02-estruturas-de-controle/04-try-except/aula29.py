
# Try/except
# try → tenta executar o código
# except → ocorreu um erro ao executar. Um bloco para tratamento de erros será executado.
  

# O que significa quando um programa levanta uma exceção?
# → Significa que a execução do algoritmo foi interrompida na linha onde ocorreu algum tipo de erro.


# Toda vez que o usuário informar algo ao sistema (input) este valor deve ser tratado.


# Diferença entre if/else e try/except
# → if/else checa uma expressão e muda o fluxo de execução de código. Não evita exceções (erros).

numero_str = input('Digite um número: ')

try:
    numero_float = float(numero_str) # A exceção 'ValueError' ocorre aqui.
    print(f'FLOAT: ${numero_float}')
    print(f'O dobro de {numero_float} é {numero_float * 2}')
except:
    # Ao identificar uma exceção, a execução do código imediatamente pula para o bloco except
    print(f'Isso não é um número.')
