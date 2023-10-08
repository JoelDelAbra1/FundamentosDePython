# Indexando cadenas, se corportaran como listas

the_string = "Silly walks"

for ix in range(len(the_string)):
    print(the_string[ix], end = ' ')

print()

# rebanadas de cadenas

alpha = "abdefg"

print(alpha[1:3]) # db
print(alpha[3:]) # efg
print(alpha[:3]) # abd
print(alpha[3:-2]) # e
print(alpha[-3:4]) # e
print(alpha[::2]) # :: Intervalo de 2 en 2
print(alpha[1::2])


# Operador in Devuelve True si el caracter esta en la cadena

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("F" in alphabet)

#operador not in

print("F" not in alphabet)
print("ñ" not in alphabet)

#Las cadenas son inmutables , por lo que no admite metodos como apend() o inser()

alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
aplphabet = alphabet + "z"

print(aplphabet)