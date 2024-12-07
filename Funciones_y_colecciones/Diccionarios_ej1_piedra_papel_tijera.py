import random #Para poder usar el random.choice

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



# Constantes:
PIEDRA = "Piedra"
PAPEL = "Papel"
TIJERAS = "Tijeras"
JUGADOR = "Gana el jugador"
EMPATE = "Empate"
CPU = "Gana el CPU"

# Contadores del juego
puntos_jugador = 0
puntos_cpu = 0
puntos_empate = 0

# Imprime y lee la opción del usuario
def menu():
    print("\n** PIEDRA, PAPEL O TIJERAS **")
    print("[1].- Piedra")
    print("[2].- Papel")
    print("[3].- Tijeras")
    print("[0].- Salir")

#La función Jugar recibe la opción que eligió el usuario, lo que hace esta función es determinar ambas elecciones
def jugar(option):
    if option == 1:
        eleccion_usuario = PIEDRA
    elif option == 2:
        eleccion_usuario = PAPEL
    elif option == 3:
        eleccion_usuario = TIJERAS
    # Elección aleatoria del CPU; En esta parte el cpu elige la opción con el random.choice (Que se utiliza para que elija un elemento aleatorio de una lista)
    eleccion_cpu = random.choice([PIEDRA, PAPEL, TIJERAS])

    print(f"Usuario: {eleccion_usuario}") #Imprime lo que haya elegido el usuario
    print(f"CPU: {eleccion_cpu}") #Imprime lo que haya elegido el cpu para que el usuario pueda visualizarlo mejor
    return eleccion_usuario, eleccion_cpu #Retorna la elección del usuario y la del cpu

# Función lógica para determinar el ganador y actualizar los contadores
def logica_contadora_del_juego(eleccion_usuario, eleccion_cpu): #Esta función recibe la elección del usuario y la del jugador
    global puntos_jugador, puntos_cpu, puntos_empate #La palabra reservada "global" sirve para acceder a estas variables fuera de la función, ya que si las declaro aquí, se reiniciarían y perdería la cuenta
    # Diccionario de reglas
    piedra_papel_tijeras = { (PIEDRA, TIJERAS): JUGADOR,(PIEDRA, PAPEL): CPU,(TIJERAS, PAPEL): JUGADOR,(TIJERAS, PIEDRA): CPU,(PAPEL, PIEDRA): JUGADOR,(PAPEL, TIJERAS): CPU}

    resultado = piedra_papel_tijeras.get((eleccion_usuario, eleccion_cpu), EMPATE)

    if resultado == JUGADOR:
        puntos_jugador += 1 #Aumenta el contador de puntos_juagador
        print(JUGADOR)
    elif resultado == CPU:
        puntos_cpu += 1 #Aumenta el contador de puntos_cpu
        print(CPU)
    else:
        puntos_empate += 1 #Aumenta el contador de puntos_empatw
        print(EMPATE)

# Código nivel de módulo
flag = 0  # Bandera para controlar el while
while flag == 0:
    menu()
    option = int(input("Elige una opción: "))
    if option == 0:
        print("Saliendo...")
        flag = 1 #Para romper el ciclo
    eleccion_usuario, eleccion_cpu = jugar(option)

    logica_contadora_del_juego(eleccion_usuario, eleccion_cpu)
    print(f"Marcador: Jugador {puntos_jugador}, CPU {puntos_cpu}, Empates {puntos_empate}")




