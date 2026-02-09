
"""
Tipos built-in
→ São tipos de dados que já vem embutidos na linguagem python. Você não precisa instalar nada.
Imutáveis já visto → str, int, float, bool → você não pode mudar esses tipos ao decorrer do programa.

Todos esses tipos são objetos, o que significa que são compostos por propriedades e métodos.


https://docs.python.org/3.13/library/stdtypes.html
"""

string = 'python'
# string[0] = 'J' → TypeError: 'str' object does not support item assignment
# É possível mudar o valor que está armazenado na variável, mas nunca o valor em si em tempo de execução.

print(string.capitalize()) # Python → Capitaliza a string transformando seu primeiro caractere em maiúscula e o resto em minúsculas.
print(string.zfill(10)) # 0000python → Preenche a string com 0 à esquerda até que a string tenha o tamanho informado.'
