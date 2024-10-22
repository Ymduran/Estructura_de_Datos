
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 10 octubre del 2024                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     *")
print(" * Entrada por consola.                                             * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

# Comentar sobre la función input.
numero1_cadena = input("Introduce un número decimal: ") #input sirve para escribir un número por consola, el número que escribe el usuario
numero2_cadena = input("Introduce otro número decimal: ")#Dentro del parentesis se imprime el letrero descriptivo para facilitar el entendimiento
resultado_cadena = numero1_cadena + numero2_cadena # Verificar qué es lo que realiza esta instrucción (ver el print).
print()
print(" ****  Recibir número sin un casting de varibles  ****")
print(f"El resultado de {numero1_cadena} y {numero2_cadena} es: {resultado_cadena}") #esta instruccuón concatena el "numero1_cadena" con "número2_cadena". Ejemplo si en la primer variable se ingres un "1" y en la segunda un 8, este print imprimirá el letrero "18"
#Lo anterior se debe a que al leer un dato por consola, este se interpreta como cadena puesto que sin importar si se trata de número o letras estos siguen siendo caracteres

numero1_float = float(numero1_cadena) #la función variable = tipo_dato_a_convertir(variable) sirve para convertir la cadena que se leyó en consola a un tipo de dato en el cuál se puedan realizar operaciones aritméticas
numero2_float = float(numero2_cadena)
resultado_float = numero1_float + numero2_float # Después de hacer la conversión, entonces se podrán realizar operaciones ariméticas con estas variables
print()
print(" ****  Casting de varibles  ****")
print(f"El resultado de {numero1_float} y {numero2_float} es: {resultado_float}")

'''

-Funciones anidadas: variable_float = float(variable)

Entrada_consola_ejercicio.py

variable = variable.lower   //.lower convierte a minúscular() 
variable = variable.lower == "si" //comparar si es igual a si

Escribe un programa de nombre Entrada_consola_ejercicio.py que realice lo siguiente:

a) Pida 2 números decimales por consola al usuario utilizando la función input.

b) Muestre los resultados de las operaciones básicas con esos números: suma, resta, multiplicación y división.

Nota: Asuma que el usuario siempre va a ingresar números y que el segundo número es diferente de cero.
'''