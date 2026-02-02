
# A função print
# → Utilizada para exibir alguma coisa na tela. Recebe argumentos.
# Um argumento é um dado que você passa para uma função ao executa-la.

print(12, 34) # Argumentos não nomeados.


print(56, 78, sep='-', end='...') 
print(1, 2, 3, sep='-', end='\n___')

# A função print possui diversos argumentos nomeados:
# → sep é um argumento nomeado da função print que é utilizado para modificar o separador padrão (espaço) da função.
# → end define o que será exibido após todos os argumentos.
# → O sep evita fazer coisas assim: print("A" + "-" + "B" + "-" + "C")

# Pode receber mais de um argumento. Separa os argumentos com um espaço nativo da função.
# A função print por padrão já inclui uma quebra de linha ao final da mensagem.


# Dica: CTRL + C e CTRL + V na mesma linha vai duplicar essa linha na linha seguinte.

# Importante: Na programação, existem caracteres que não estão sendo exibidos mas estão fazendo algo no seu código.

# Quebra de linha do windows: \r\n → CRLF (Carriage Return Line Feed)
# Quebra de linha em sistemas baseado em Unix: \n → LF (Line Feed)

# Python é Case Sensitive, ou seja, ele diferencia letras minúsculas de letras maiúsculas, portanto "Print" não é a mesma coisa que "print", pois cada caractere possui um código binário diferente.
