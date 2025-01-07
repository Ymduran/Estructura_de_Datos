import random

print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 06 de diciembre del 2025                                  * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Piedra papel o tijeras a dos manos                               * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")


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
'''
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

'''

flag = 0 #Bandera que controla el while
while flag == 0: #Mientras que flag valga 0

    menu()
    option_derecha = int(input("Elige una opción para mano derecha: ")) #Pide opción para la mano derecha
    option_izquierda = int(input("Elige una opción para mano izquierda : "))#Pide opción para la mano izquierda

    if option_derecha == 0 or option_izquierda == 0: #Si alguna/cualquiera de las dos opciones es 0 entonces se rompe el ciclo
        print("Saliendo...")
        flag = 1  # Se rompe el cliclo

    else:
        print("Derecha:")
        eleccion_usuario_derecha, eleccion_cpu_derecha = jugar(option_derecha) #Muestra lo que ha elegido tanto el usuario como la cpu respecto a la mano derecha
        print("Izquierda:")
        eleccion_usuario_izquierda, eleccion_cpu_izquierda = jugar(option_izquierda) #Muestra lo que ha elegido tanto el usuario como la cpu respecto a la mano izquierda
        print("")

        eleccion_usuario = int(input("Qué mano desea dejar; 1)Derecha   2)Izquierda: ")) #Pregunta al usuario que mano desea dejar
        if eleccion_usuario == 1:
            eleccion_usuario = eleccion_usuario_derecha
            print(f"Usuario elige derecha: {eleccion_usuario}")
        elif eleccion_usuario == 2:
            eleccion_usuario = eleccion_usuario_izquierda
            print(f"Usuario elige izquierda: {eleccion_usuario}")

        print("")
        eleccion_cpu = random.choice([eleccion_cpu_derecha,eleccion_cpu_izquierda]) #La cpu también elige que mano desea dejar
        print(f"CPU elige: {eleccion_cpu}")

        logica_contadora_del_juego(eleccion_usuario, eleccion_cpu) #manda a llamar a la función que lleva la cuenta de victorias y empates
        print(f"Marcador: Jugador {puntos_jugador}, CPU {puntos_cpu}, Empates {puntos_empate}")




        #Condición: 0< opción <4 = opción > 0 and opción < 4







