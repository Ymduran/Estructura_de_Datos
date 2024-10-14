print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 14 octubre del 2024                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     *")
print(" * Conversión de tipos de datos (casting) en Python.                * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

# Notas
'''
La conversión de tipos de datos implica manipular datos que no están en el tipo de dato requerido. Ejemplos:
de cadena a entero, de cadena a número flotante, y viceversa.
'''

# *****   Conversión de cadena a entero     *****
var_cadena = "951"
var_int = int(var_cadena) #convierte la var_cadena que se trataba de una cadena a un entero, así var_int tiene el valor entero de 951

# Utiliza la letra "f" antes de las comillas para indicar que la cadena será formateada. Esto en el print
# Esto significa que puedes incluir variables y expresiones dentro de las llaves {}
# y su valor será insertado en el texto final. Después de la formateada

print("Conversión de cadena a entero.")
print(f"Número como cadena: {var_cadena}.") #las llaves permiten imprimer dentro del letrero, es decir, entre las comillas
print(f"Número como int más uno: {var_int + 1}.") #Ya en entero se pueden hacer operaciones aritméticas


# *****   Conversión de cadena a flotante     *****
var_cadena = "8.88"
var_float = float(var_cadena) #variable_flotante = tipo_de_dato(Dato a convertir)
print()
print("Conversión de cadena a flotante.")
print(f"Número como cadena: {var_cadena}.") #f que indica que el numero fue formateado y entre llaves
print(f"Número como float más cero punto uno: {var_float + 0.1}.") #ya en flotante se pueden hacer operaciones con resultado en flotante

# *****   Conversión de número a cadena     *****
var_int = 123 #número entero
var_float = 123.321 #número flotante
print() #salto de línea
print("Conversión de número a cadena.")
print(f"Los números {var_int} y {var_float} se convierten a cadena utilizando str(var_int): {str(var_cadena)}, y " f"str(var_float): {str(var_float)}.")
                                                                                            #cadena(var_cadena)


# *****   Conversión a booleano     *****
# Si el valor es 0, cadena vacía o None, la función bool regresa un valor de False. En caso contrario, regresa True.
print()
print("Conversión a booleanos.")

var_int = 0 #variable entera
es_verdadero = bool(var_int) # variable_es_verdadero = convertir_tipo_booleano(número_entero_que_se_convertirá_a_booleano)
print(f"¿El valor de {var_int} es verdadero? {es_verdadero}.") #imprime falso porque contiene 0
var_int = -30 #variable entera
es_verdadero = bool(var_int) #variable booleana
print(f"¿El valor de {var_int} es verdadero? {es_verdadero}.") #imprime verdadero porque contiene el número -30

var_float = 0.0
es_verdadero = bool(var_float)
print(f"¿El valor de {var_float} es verdadero? {es_verdadero}.") #imprime falso porque contiene 0.0
var_float = 0.01
es_verdadero = bool(var_float)
print(f"¿El valor de {var_float} es verdadero? {es_verdadero}.") #imprime verdadero porque ahora contiene el número 0.01

var_cadena = ""
es_verdadero = bool(var_cadena)
print(f"¿El valor de {var_cadena} es verdadero? {es_verdadero}.") #imprime falso porque la cadena está vacía, contiene 0 caracteres
var_cadena = None
es_verdadero = bool(var_cadena)
print(f"¿El valor de {var_cadena} es verdadero? {es_verdadero}.") #imprime falso porque la variable no contiene nada
var_cadena = " "
es_verdadero = bool(var_cadena)
print(f"¿El valor de {var_cadena} es verdadero? {es_verdadero}.") #imprime verdadero porque la cadena tiene un espacio


#Casting_ejercicio.py

#Realiza un programa de nombre Casting_ejercicio.py que realice lo siguiente:

#a) Convierta los siguientes números en cadenas: 3.14159265, 12, 0.

#b) De los números anteriores, indica su valor booleano.

#c) Convierta las siguientes cadenas a números: "10002", "100.02", "0".

#d) De las cadenas anteriores, indica su valor booleano. Nota: especificar por qué el resultado de la cadena "0".
