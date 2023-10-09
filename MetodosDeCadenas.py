# metodo capitalize(), La vuelve mayuscula la primera letra de la cadena indice 0

print("-------------------- Metodos de cadenas Capitaliza -------------------")

print('aBCd'.capitalize())
print("Alpha".capitalize())
print('ALPHA'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())

# metodo center(), centra la cadena en el numero de caracteres que se le indique
print('[' + 'HOLA'.center(12) + ']')

# Si no es un lo suficientemente grande para contener la cadena, se regresa laa cadena original

print('[' + 'HOLA'.center(2) + ']')

# Variante de dos argumentos, el segundo argumento es el caracter de relleno
print('[' + 'HOLA'.center(12, '*') + ']')

#metodo endswith(), devuelve True si la cadena termina con el sufijo indicado
print("-------------------- Metodos de cadenas endswith -------------------")
if "gatos".endswith("os"):
    print("Si termina con os")
else:
    print("No termina con os")

t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))

#metodo find(), devuelve el indice de la primera aparicion de la subcadena, si no se encuentra devuelve -1 (Solo cadenas)

print("-------------------- Metodos de cadenas find -------------------")

print("Casandra".find("a"))
print("Casandra".find("o"))

t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))

#Variante de dos argumentos, el segundo argumento es el indice donde se inicia la busqueda
print("-------------------- Metodos de cadenas find con dos argumentos -------------------")
print("Gatas".find("a", 2))

#Variante de tres argumentos, el tercer argumento es el indice donde se termina la busqueda
print("-------------------- Metodos de cadenas find con tres argumentos -------------------")
print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))

#metodo isalnum(), devuelve True si la cadena contiene solo letras y numeros
print("-------------------- Metodos de cadenas isalnum -------------------")
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())
t = 'ΑβΓδ'
print(t.isalnum())
t = '20E1'
print(t.isalnum())

#Metodo isalpha(), devuelve True si la cadena contiene solo letras y no numeros
print("-------------------- Metodos de cadenas isalpha -------------------")
print("Moooo".isalpha())
print('Mu40'.isalpha())

#Metodo isdigit(), devuelve True si la cadena contiene solo numeros y no letras
print("-------------------- Metodos de cadenas isdigit -------------------")
print('2018'.isdigit())
print("Year2019".isdigit())

#Metodo islower(), devuelve True si la cadena contiene solo letras minusculas
print("-------------------- Metodos de cadenas islower -------------------")
print("Moooo".islower())
print('moooo'.islower())

#Metodo isspace(), devuelve True si la cadena contiene solo espacios en blanco
print("-------------------- Metodos de cadenas isspace -------------------")
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

#Metodo isupper(), devuelve True si la cadena contiene solo letras mayusculas
print("-------------------- Metodos de cadenas isupper -------------------")
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())