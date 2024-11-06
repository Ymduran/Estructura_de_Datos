print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 06 de noviembre del 2024                                   * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" *  ciclo for                                                        * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")


'''
SINTAXIS

for variable in secuencia: #En donde la variable será un elemento dentro de una secuencia, la variable secuencia es la secuencia
    Una cadena puede a su vez ser una secuencia en donde cada caracter es un elemento individual de ésta.
'''

'''
character_counter = 0
cadena = input("Cadena: ") #Se lee una cadena (no es necesario convertir a str porque ya se lee desde el teclado una cadena).


for caracter in cadena: 
    #character_counter += 1 #En este caso no se crea un contador puesto que el for ya incluye la suma elemento a elemento 
    print(f" {caracter}", end =" - ") # "end": palabra reservada para sustituir el salto de línea con un espacio/variable/etc y se impriman en la misma línea.
'''

'''
alumnos = ["Rosalinda", "Juan", "Lourdes", "Tania", "Bryan", "Rebeca", "Jennifer", "Héctor", "Jesús", "Addi"] #Arreglo: un arreglo es una estructura de datos que permite almacenar y acceder a un conjunto de elementos del mismo tipo en una ubicación de memoria contigua
#En python se puede añadir un nuevo elemento sin causar errores, a comparación de c en dónde se definían la cantidad de elementos de un arreglo como límite.

for alumno in alumnos: #En donde alumno es cada una de las cadenas (cada elemento del arreglo) y alumnos es
    print(f"Hola, {alumno}") #Esto imprime a cada elemento, en este caso, cada nombre
'''

for i in range(1, 11): #Range en una palabra reservada para añadir una secuencia de números range(número_inicial,número final).General números del número_final-1
    print(i, end= ", " )
