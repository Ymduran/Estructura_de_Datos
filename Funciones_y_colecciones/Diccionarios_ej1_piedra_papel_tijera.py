import random

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
#Constantes:
PIEDRA = "Piedra"
PAPEL = "Papel"
TIJERAS = "Tijeras"
JUGADOR = "Gana el jugador"
EMPATE = "Empate"
CPU = "Gana el CPU"

#Contadores de las rondas
puntos_jugador = 0
puntos_cpu = 0
puntos_empate = 0

#Imprime el menú
def menu():
    print("** PIEDRA, PAPEL O TIJERAS **")
    print("[1].- Piedra")
    print("[2].- Papel")
    print("[3].- Tijeras")
    print("[0].- Salir")

# La función Jugar recibe la opción que eligió el usuario
def jugar(option):
    if option == 1:
        eleccion_usuario = PIEDRA
    elif option == 2:
        eleccion_usuario = PAPEL
    elif option == 3:
        eleccion_usuario = TIJERAS
    # Esta parte es en donde el cpu elige
    eleccion_cpu = random.choice([PIEDRA, PAPEL, TIJERAS])
    print(f"Usuario: {eleccion_usuario}") #Imprime lo que haya elegido el usuario
    print(f"CPU: {eleccion_cpu}") #Imprime lo que haya elegido el cpu para que el usuario lo vea
    return eleccion_usuario, eleccion_cpu #Retorna las dos opciones

# Función Lógica para saber quién gana y suma al marcador
def logica_contadora_del_juego(eleccion_usuario, eleccion_cpu):
    global puntos_jugador, puntos_cpu, puntos_empate #Se accede a variables desde afuera con la palabra reservada "global", ya que si las vuelvo a declarar en la función se reinician y pierde la cuenta
    #Diccionario "piedra_papel_tijeras" tiene las reglas del juego
    piedra_papel_tijeras = {(PIEDRA, TIJERAS): JUGADOR,(PIEDRA, PAPEL): CPU,(TIJERAS, PAPEL): JUGADOR,(TIJERAS, PIEDRA): CPU,(PAPEL, PIEDRA): JUGADOR,(PAPEL, TIJERAS): CPU}
    resultado = piedra_papel_tijeras.get((eleccion_usuario, eleccion_cpu), EMPATE)
    if resultado == JUGADOR:
        puntos_jugador += 1 #Se le suma al marcador al jugador
        print(JUGADOR)
    elif resultado == CPU:
        puntos_cpu += 1 #Se le suma al marcador al cpu
        print(CPU)
    else:
        puntos_empate += 1 #Se le suma al marcador al empate
        print(EMPATE)

#Código nivel de módulo
flag = 0  #Bandera para controlar el while
while flag == 0:
    menu()

    option = int(input("Elige una opción: "))
    if option == 0:
        print("Saliendo...")
        flag = 1 #Se rompe el cliclo
    else:
        eleccion_usuario, eleccion_cpu = jugar(option)
        logica_contadora_del_juego(eleccion_usuario, eleccion_cpu)
    print(f"Marcador: Jugador {puntos_jugador}, CPU {puntos_cpu}, Empates {puntos_empate}")









