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
print(" ** Ejercicio 1. La escalera. ** ")
print("Ingresa el número de escalones (positivo - ascendente y negativo - descendente) o ingresa un cero para salir: ")




espacio = "  "
escalon_negativo = " |_"
escalon_positivo = "_| "
numero_de_escalones = 8

print("  _")
for i in range(0,numero_de_escalones):
    print(f"{espacio*i}{escalon_negativo}")

numero_de_escalones = -5
for j in range(numero_de_escalones, 0):
    print(f"{espacio*(j*-1)}{escalon_positivo}")
flag = 0
While flag == 0:

