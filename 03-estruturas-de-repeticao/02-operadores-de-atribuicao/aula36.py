"""

Operadores de Atribuição 
= 
+= → soma com o valor atual ou concatena com o valor atual
-=
*=
/=
//=
**=
%= → Calcula o resto da divisão com o valor atual

"""

contador_str = '0'
contador_str += '1'
print(contador_str) # concatena as strings → 01

contador_int = 5
contador_int %= 2
print(contador_int) # resto da divisão → 1

contador_int2 = 10
contador_int2 //= 3
print(contador_int2) # divisão inteira → 3
