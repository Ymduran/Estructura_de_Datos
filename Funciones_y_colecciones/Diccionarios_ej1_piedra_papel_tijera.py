from random import random

print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 02 de diciembre del 2024                                  * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Diccionarios_ej1_piedra_papel_tijera                             * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

'''
Escribe un programa de nombre Diccionarios_ej1_piedra_papel_tijera.py que realice lo siguiente:
Este programa es una nueva versión del juego realizado de 
piedra, papel y tijeras, pero utilizando un diccionario para las reglas del juego.
El juego mostrará las victorias del jugador, 
los partidos empatados y las victorias del CPU. Se debe mostrar el siguiente menú:
  ***  Juego de piedra, papel o tijeras  ***
1) Piedra.
2) Papel.
3) Tijeras.
0) Salir.
Cualquier otro caso -> Opción no válida.
Para ello:
a) Muestre el menú en una función que pida al usuario una de las opciones: piedra, papel o tijeras.
b) Utilice un diccionario para las distintas combinaciones.
c) Realice la lógica adecuada para determinar al ganador. Se requiere que utilice al menos una función.
d) Muestre la elección del jugador y la del cpu.
e) Muestre la cantidad de victorias, empates y derrotas.
f) Repita nuevamente el menú hasta salir.
'''

PIEDRA = "Piedra"
PAPEL = "Papel"
TIJERAS = "Tijeras"
JUGADOR = "Gana el jugador"
EMPATE = "Empate"
CPU = "Gana el CPU"

def menu():
    print("** PIEDRA, PAPEL O TIJERAS **")
    print("[1].- Piedra")
    print("[2].- Papel")
    print("[3].- Tijeras")
    option = int(input("Elige una opción: "))
    return option

def jugar(option):
    if option == 1:
        eleccion_usuario = PIEDRA
    elif option == 2:
        eleccion_usuario = PAPEL
    elif option == 3:
        eleccion_usuario = TIJERAS

    eleccion_cpu = random.choice([PIEDRA, PAPEL,TIJERAS])
    return eleccion_usuario,eleccion_cpu




