import random

# Constantes:
PIEDRA = "Piedra"
PAPEL = "Papel"
TIJERAS = "Tijeras"
JUGADOR = "Gana el jugador"
EMPATE = "Empate"
CPU = "Gana el CPU"

# Contadores globales
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

# La función Jugar recibe la opción que eligió el usuario
def jugar(option):
    if option == 1:
        eleccion_usuario = PIEDRA
    elif option == 2:
        eleccion_usuario = PAPEL
    elif option == 3:
        eleccion_usuario = TIJERAS
    else:
        return None, None  # Caso de salida o error
    # Elección aleatoria del CPU
    eleccion_cpu = random.choice([PIEDRA, PAPEL, TIJERAS])
    print(f"Usuario: {eleccion_usuario}")
    print(f"CPU: {eleccion_cpu}")
    return eleccion_usuario, eleccion_cpu

# Lógica para determinar el ganador y actualizar contadores
def logica_contadora_del_juego(eleccion_usuario, eleccion_cpu):
    global puntos_jugador, puntos_cpu, puntos_empate
    # Diccionario de reglas
    piedra_papel_tijeras = {
        (PIEDRA, TIJERAS): JUGADOR,
        (PIEDRA, PAPEL): CPU,
        (TIJERAS, PAPEL): JUGADOR,
        (TIJERAS, PIEDRA): CPU,
        (PAPEL, PIEDRA): JUGADOR,
        (PAPEL, TIJERAS): CPU
    }
    resultado = piedra_papel_tijeras.get((eleccion_usuario, eleccion_cpu), EMPATE)
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
    try:
        option = int(input("Elige una opción: "))
        if option == 0:
            print("Saliendo...")
            break
        elif option not in [1, 2, 3]:
            print("Opción no válida, intenta de nuevo.")
            continue
        eleccion_usuario, eleccion_cpu = jugar(option)
        if eleccion_usuario and eleccion_cpu:
            logica_contadora_del_juego(eleccion_usuario, eleccion_cpu)
        print(f"Marcador: Jugador {puntos_jugador}, CPU {puntos_cpu}, Empates {puntos_empate}")
    except ValueError:
        print("Por favor, introduce un número válido.")
