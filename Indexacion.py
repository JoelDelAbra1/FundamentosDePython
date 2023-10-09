# Indexando cadenas, se corportaran como listas
print("-------------------- Cadena como lista -------------------")
the_string = "Silly walks"

for ix in range(len(the_string)):
    print(the_string[ix], end = ' ')

print()

# rebanadas de cadenas
print("-------------------- Rebanadas de cadenas -------------------")
alpha = "abdefg"

print(alpha[1:3]) # db
print(alpha[3:]) # efg
print(alpha[:3]) # abd
print(alpha[3:-2]) # e
print(alpha[-3:4]) # e
print(alpha[::2]) # :: Intervalo de 2 en 2
print(alpha[1::2])


# Operador in Devuelve True si el caracter esta en la cadena
print("-------------------- Operador in -------------------")

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("F" in alphabet)

#operador not in
print("-------------------- Operador not in -------------------")
print("F" not in alphabet)
print("ñ" not in alphabet)

#Las cadenas son inmutables , por lo que no admite metodos como apend() o inser()
print("-------------------- Las cadenas son inmutables -------------------")
alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
aplphabet = alphabet + "z"

print(aplphabet)

print("-------------------- Metodos de cadenas MIN -------------------")
# min, devuleve el caracter minimos en la cadena en ascii
print(min("aAbByYzZ"))

t = 'The Knights Who Say "Ni!"'	# el espacio cuenta
print("[" + min(t) + "]")

t = [0, 1, 2]
print(min(t))


# max, devuelve el caracter maximo en la cadena en ascii
print("-------------------- Metodos de cadenas MAX -------------------")

print(max("aAbByYzZ"))

t = 'The Knights Who Say "Ni!"'
print("[" + max(t) + "]")

t = [0, 1, 2]
print(max(t))

# index, devuelve el indice del caracter en la cadena, debe de estar en la cadena si no devuelve error

print("-------------------- Metodos de cadenas INDEX -------------------")
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))  
print("aAbByYzZaA".index("A"))

#funcion list crea una lista de caracteres

print("-------------------- Funcion LIST -------------------")

print(list("abcabc"))

# count, devuelve el numero de veces que aparece el caracter en la cadena

print("-------------------- Metodos de cadenas COUNT -------------------")
print("abcabc".count("b"))
print('abcabc'.count("d"))