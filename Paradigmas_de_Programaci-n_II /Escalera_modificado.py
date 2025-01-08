print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 05 de diciembre de 24                                     * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * La escalera                                                      * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

'''
Instrucciones:

Escribe un programa de nombre Ej1_escalera.py que realice lo que se indica en la descripción del programa.
Comparte el enlace de GitHub en la caja de texto al final de la pregunta.
Descripción del programa:
Este programa dibuja una escalera, en donde el usuario ingresa el número de escalores.
Si el número es positivo, la escalera será ascendente. Un ejemplo cuando se ingresa un valor de 4:
        _
      _|
    _|
  _|
_|

Si el número es negativo, la escalera será descendente. Un ejemplo cuando se ingresa un valor de -4:
_
 |_
   |_
     |_
       |_

Si el número es cero, se deberá salir del programa.
Se debe mostrar la siguiente pantalla:
  ***  Ejercicio 1. La escalera.  ***
Ingresa el número de escalones (positivo - ascendente y negativo - descendente) o ingresa un cero para salir:
Cualquier otro caso -> Opción no válida.
Para ello:
a) Solicite el número de escalones utilizando un ciclo.
b) Muestre la escalera utilizando la lógica adecuada. Se requiere utilizar funciones para dibujar las escaleras para considerar el ejercicio como completo.

'''


def menu():
    print(" ")
    print(" ")
    print(" ** Ejercicio 1. La escalera. ** ")
    print("Número de escalones (positivo - descendente y negativo - ascendente) o ingresa un cero para salir")


espacio = "  "
escalon_positivo = "_| "
escalon_negativo = " |_"



def imprimir_escalones_ascendentes(numero_de_escalones):  # Cuando es un número positivo
    print(f"{espacio * (numero_de_escalones*-1)}    _")
    for i in range(numero_de_escalones-1,0):
        print(f"{espacio * (i*-1)}{escalon_positivo}")


def imprimir_escalones_descendentes(numero_de_escalones):  # Cuando es un número negativo
    print("_")
    for j in range(0,numero_de_escalones+1):
        print(f"{espacio * (j)}{escalon_negativo}")


# código a nivel de módulo
flag = 0
while flag == 0:
    menu()
    numero_de_escalones = int(input("Ingresa número entero: "))
    if numero_de_escalones == 0:
        print("Saliendo...")
        flag = 1  # Rompe el ciclo
    elif numero_de_escalones < 0:  # Si se trata de un número negativo
        numero_de_escalones = numero_de_escalones
        imprimir_escalones_ascendentes(numero_de_escalones)
    elif numero_de_escalones > 0:  # Si se trata de un número positivo
        numero_de_escalones = numero_de_escalones
        imprimir_escalones_descendentes(numero_de_escalones)
