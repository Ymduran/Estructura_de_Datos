import random #Para poder usar el random.choice

print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 02 de diciembre del 2024                                  * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Diccionarios_ej2_piedra_papel_tijera_lagarto_spock.py            * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

'''
 ***  Juego de piedra, papel, tijeras, lagarto, spock  ***
1) Piedra.
2) Papel.
3) Tijeras.
4) Lagarto.
5) Spock.
6) Ver reglas.
0) Salir.
Cualquier otro caso -> Opción no válida.
Para ello:
a) Muestre el menú en una función que pida al usuario una de las opciones.
b) Utilice un diccionario para las distintas combinaciones.
c) Realice la lógica adecuada para determinar al ganador.
d) Muestre la elección del jugador y la del cpu.
e) Muestre la cantidad de victorias, empates y derrotas.
f) Repita nuevamente el menú hasta salir.
Observe la salida de la consola como guía:
'''

# Constantes:
PIEDRA = "Piedra"
PAPEL = "Papel"
TIJERAS = "Tijeras"
LAGARTO = "Lagarto"
SPOCK = "Spock"
JUGADOR = "Gana el jugador"
EMPATE = "Empate"
CPU = "Gana el CPU"

# Contadores que se  usarán para sumar al juego
puntos_jugador = 0
puntos_cpu = 0
puntos_empate = 0

# Imprime el menú
def menu():
    print("------------------------------------------ ")
    print(" ")
    print("** PIEDRA, PAPEL, TIJERAS, LAGARTO, SPOCK **")
    print("[1].- Piedra")
    print("[2].- Papel")
    print("[3].- Tijeras")
    print("[4].- Lagarto")
    print("[5].- Spock")
    print("[6].- Ver reglas")
    print("[0].- Salir")


#Función que imprime las reglas
def imprimir_reglas():
    print("** REGLAS DEL JUEGO **")
    print("- Tijeras cortan papel.")
    print("- Papel cubre piedra.")
    print("- Piedra aplasta lagarto.")
    print("- Lagarto envenena Spock.")
    print("- Spock destruye tijeras.")
    print("- Tijeras decapitan lagarto.")
    print("- Lagarto come papel.")
    print("- Papel desaprueba Spok.")
    print("- Spock vaporiza piedra.")
    print("- Piedra aplasta tijeras.")



# La función Jugar recibe la opción que eligió el usuario y solo determina la opción del jugador como la del cpu
def jugar(option):
    if option == 1:
        eleccion_usuario = PIEDRA
    elif option == 2:
        eleccion_usuario = PAPEL
    elif option == 3:
        eleccion_usuario = TIJERAS
    elif option == 4:
        eleccion_usuario = LAGARTO
    elif option == 5:
        eleccion_usuario = SPOCK
    #En esta parte la cpu elige de forma al azar
    eleccion_cpu = random.choice([PIEDRA, PAPEL, TIJERAS, LAGARTO, SPOCK]) #Elige entre la lista con el .choice
    print(" -------------------------------------------------------------")
    print(f"Usuario: {eleccion_usuario}") #Escribe la opción que eligió el usuario
    print(f"CPU: {eleccion_cpu}") #Escribe la opción que eligió la cpu
    return eleccion_usuario, eleccion_cpu #Retorna ambas elecciones

# Lógica para determinar el ganador y actualizar contadores
def logica_contadora_del_juego(eleccion_usuario, eleccion_cpu):
    global puntos_jugador, puntos_cpu, puntos_empate


    # Diccionario de reglas, son todas las combinaciones del juego
    reglas = {
        (PIEDRA, TIJERAS): JUGADOR,
        (PIEDRA, LAGARTO): JUGADOR,
        (PAPEL, SPOCK): JUGADOR,
        (PIEDRA, SPOCK): CPU,
        (TIJERAS, LAGARTO): JUGADOR,
        (LAGARTO, SPOCK): JUGADOR,
        (LAGARTO, PAPEL): JUGADOR,
        (SPOCK, TIJERAS): JUGADOR,
        (SPOCK, PIEDRA): JUGADOR,
        (PIEDRA, PAPEL): CPU,
        (TIJERAS, PAPEL): JUGADOR,
        (PAPEL, TIJERAS): CPU,
        (PAPEL, LAGARTO): CPU,
        (TIJERAS, PIEDRA): CPU,
        (TIJERAS, SPOCK): CPU,
        (LAGARTO, PIEDRA): CPU,
        (LAGARTO, TIJERAS): CPU,
        (SPOCK, PAPEL): CPU,
        (SPOCK, LAGARTO): CPU,
        (PAPEL, PIEDRA): JUGADOR
    }



    resultado = reglas.get((eleccion_usuario, eleccion_cpu), EMPATE)
    if resultado == JUGADOR:
        puntos_jugador += 1
        print(JUGADOR)
    elif resultado == CPU:
        puntos_cpu += 1
        print(CPU)
    else:
        puntos_empate += 1
        print(EMPATE)

# Código nivel de módulo
flag = 0  # Bandera para controlar el while
while flag == 0:
    menu()
    option = int(input("Elige una opción: "))
    if option == 0:
        print("Saliendo...")
        flag = 1 #Rompe el ciclo
    elif option == 6:  # Mostrar reglas
        imprimir_reglas()  # Manda a llamar a la función para imprimir las reglas
    else:
        eleccion_usuario, eleccion_cpu = jugar(option)
        logica_contadora_del_juego(eleccion_usuario, eleccion_cpu)
        print(f"Marcador: Jugador {puntos_jugador}, CPU {puntos_cpu}, Empates {puntos_empate}") #Imprime los puntos, guardó la suma gracias a las variables globales


