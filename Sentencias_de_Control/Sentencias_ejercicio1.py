print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 124 octubre del 2024                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Sentencia ejercicio                                             * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print("  ")

'''
Instrucciones: Escribe un programa de nombre Sentencias_ejercicio1.py que realice lo siguiente:

Este programa determinará cuál de dos números ingresados por el usuario es menor o si son iguales. Para ello:

a) Solicite al usuario dos números decimales.

b) Utilice la lógica adecuada para determinar cuál de los dos números es menor o si es que son iguales.

c) Muestre el número menor (o que son iguales) en consola.

'''
numero1, numero2=float(input("ingrese primer número decimal: ")), float(input("ingrese segundo número decimal: "))

if numero1<numero2:
    print(f"el número {numero1:.3f} es menor")
elif numero1>numero2:
    print(f"el número {numero2:.3f} es menor")
else:
    print(f"el número {numero1:.3f} y el número {numero2:.3f} son iguales")
