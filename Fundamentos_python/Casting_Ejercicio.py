#Casting_ejercicio.py
#Realiza un programa de nombre Casting_ejercicio.py que realice lo siguiente:
#a) Convierta los siguientes números en cadenas: 3.14159265, 12, 0.
#b) De los números anteriores, indica su valor booleano.
#c) Convierta las siguientes cadenas a números: "10002", "100.02", "0".
#d) De las cadenas anteriores, indica su valor booleano. Nota: especificar por qué el resultado de la cadena "0".

#declaración de variables
variable_cadena = "hola"
variable_flotante = 3.14159264
variable_entero = 12
variable_cero = 0

#impresión de variables sin modificar

print("")
print("** impresión de variables sin modificar ** ")
print("variable cadena: ", variable_cadena)
print("variable flotante: ", variable_flotante)
print("variable entero: ", variable_entero)
print("variable cero: ", variable_cero)


#a) Convierta los siguientes números en cadenas: 3.14159265, 12, 0.
print("")
print("** conversion a cadenas **")
variable_cadena = str(variable_flotante)
print(f"conversión del flotante a cadena: {variable_cadena}")
variable_cadena = str(variable_entero)
print(f"conversión del entero a cadena: {variable_cadena}")
variable_cadena = str(variable_cero)
print(f"conversión del cero a cadena: {variable_cadena}")

#b) De los números anteriores, indica su valor booleano.
print("")
print("** conversion a booleano **")
variable_booleano = bool(variable_cadena)
print(f"valor de cadena en booleano: {variable_booleano}") #valor true porque contiene los caracteres de hola
variable_booleano = bool(variable_flotante)
print(f"valor de flotante en booleano: {variable_booleano}") #valortrue porque contiene la cantidad de 3.1415...
variable_booleano = bool(variable_entero)
print(f"valor de entero en booleano: {variable_booleano}") #valor true porque contiene la cantidad de 12
variable_booleano = bool(variable_cero)
print(f"valor de cero en booleano: {variable_booleano}") #valor false porque contiene cantidad de cero

#c) Convierta las siguientes cadenas a números: "10002", "100.02", "0".

print("")
print("** conversion de cadenas a números **")
variable_flotante = "100.02" #cambiandoles el valor
variable_entero = "10002"
variable_cero = "0"
print("nueva variable cadena de flotante: ", variable_flotante)
print("nueva variable cadena de entero: ", variable_entero)
print("nueva variable cadena de cero: ", variable_cero)
print("")
print("Convirtiendo a números... ")
print("")
variable_numero = float(variable_flotante)
print(f"valor cadena de flotante a número flotante: {variable_numero}")
variable_numero = float(variable_entero)
print(f"valor cadena de enetero a número entero: {variable_numero}")
variable_numero = float(variable_cero)
print(f"valor cadena de cero a número cero: {variable_numero}")

#d) De las cadenas anteriores, indica su valor booleano. Nota: especificar por qué el resultado de la cadena "0".
print("")
print("** conversion de las cadenas enteriores a booleano **")
variable_numero=bool(variable_flotante)
print(f"valor cadena variable flotante en booleano es de: {variable_numero}")
variable_numero=bool(variable_entero)
print(f"valor cadena variable entero en booleano es de: {variable_numero}")
variable_numero=bool(variable_cero)
print(f"valor cadena variable cero en booleano es de: {variable_numero}") #imprime true porque se trata de una cadena y el cero es un caracter, por lo que es suficiente condición para que sea true

