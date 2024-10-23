
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 10 octubre del 2024                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     *")
print(" * Entrada por consola ejercicio                                     * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")
'''
Escribe un programa de nombre Entrada_consola_ejercicio.py que realice lo siguiente:

a) Pida 2 números decimales por consola al usuario utilizando la función input.

b) Muestre los resultados de las operaciones básicas con esos números: suma, resta, multiplicación y división.

Nota: Asuma que el usuario siempre va a ingresar números y que el segundo número es diferente de cero.
'''
#Se leen los números por consola
numero_decimal1, numero_decimal2 = input("ingrese primer número decimal: "), input("ingrese el segundo número decimal: ")
#Se debe realizar la conversión de datos correspondiente (en este caso a flotante) para poder realizar las operaciones aritméticas posteriores
numero_decimal1, numero_decimal2 = float(numero_decimal1), float(numero_decimal2) #variable = tipo_dato_a_convertir(variable)

#suma
print(f"¿ {numero_decimal1} + {numero_decimal2} = {numero_decimal1 + numero_decimal2}") #se suman ambos números desde el print
#resta
print(f"¿ {numero_decimal1} - {numero_decimal2} = {numero_decimal1 - numero_decimal2}")#se restan ambos números desde el print
#multiplicación
print(f"¿ {numero_decimal1} * {numero_decimal2} = {numero_decimal1 * numero_decimal2}")#se multiplican ambos números desde el print
#dicisión
print(f"¿ {numero_decimal1} / {numero_decimal2} = {numero_decimal1 / numero_decimal2}")#se deviden ambos números desde el print
#la f antes de las comillas antes de print es para poder imrpimir las variables dentro de él, siempre y cuando estas variables estén dentro de las llaves "{}", en caso contrario será considerado texto