"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
    x → hex minúsculo.
    X → hex maiúsculo.

Sintaxe derivada do C
→ Forma de exibir valores de variáveis dentro de strings.
"""

lang = 'Python'
ver = 3.14

output = '%s - ver%.2f' % (lang, ver)
print(output)

hexa = 'O hexadecimal de 15 é %02X' % 15
print(hexa)

# 02 → Preenche até duas casas e coloca zero.
