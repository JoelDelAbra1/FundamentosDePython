str1  = 'a'
str2  = 'b'
  # El operador + concatena cadenas, es importante el orden en el que se concatenan
print(str1 + str2)
print(str2 + str1)

# El operador * repite una cadena un numero determinado de veces, se necesita un entero y una cadena, 
# no importa el orden en el que se escriban

print(5 * 'a')
print('b' * 4)

# ord() devuelve el valor ASCII de un caracter, es necesario que sea un solo caracter

char_1 = 'a'
char_2 = ' ' # espacio en blanco

print(ord(char_1))

print(ord(char_2))

char_3 = 'ñ'
char_4 = 'α'

print(ord(char_3))
print(ord(char_4))

# chr() devuelve el caracter de un valor ASCII, es necesario que sea un entero

print(chr(97))
print(chr(945))