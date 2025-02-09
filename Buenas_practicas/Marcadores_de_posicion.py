import random

def crear_baraja():
    """Crea una baraja española sin ochos ni nueves"""
    palos = {'oros': '🟡', 'copas': '🍷', 'espadas': '⚔️', 'bastos': '🌿'}
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    return [(valor, palo, f"{valor}{simbolo}") for palo, simbolo in palos.items() for valor in valores]

def barajar(baraja):
    """Baraja las cartas."""
    random.shuffle(baraja)

def inicializar_carrera():
    """Inicializa los caballos en la posición de salida."""
    return {'oros': 0, 'copas': 0, 'espadas': 0, 'bastos': 0}

def mostrar_pista(caballos):
    """Muestra la pista de la carrera."""
    print("\nPista de carrera:")
    print("--------------------------------|")
    for palo in caballos:
        posicion = caballos[palo]
        pista = ""
        contador = 0

        while contador < posicion:
            pista = pista + "  —"
            contador = contador + 1
        
        if posicion == 0:
            pista = "🐴 >"
        else:
            pista = pista + "🐴 >"
        if palo == "oros":
            figura = "🟡   "
        elif palo == "copas":
            figura = "🍷  "
        elif palo == "espadas":
            figura = "⚔️"
        elif palo == "bastos":
            figura = "🌿 "
        
        print(palo + figura + " " + pista)
        print("****************************🏁   " + "|")
    print("--------------------------------|")

def retroceso(caballos, cartas_fuera):
    """Voltea la primera carta y hace retroceder al caballo de ese palo."""
    todos_avanzaron = True
    for caballo in caballos:
        if caballos[caballo] == 0:
            todos_avanzaron = False

    if todos_avanzaron:
        if len(cartas_fuera) > 0:
            primera_carta = cartas_fuera.pop(0)  # Se voltea la primera carta
            palo_carta = ""

            if "🟡" in primera_carta:
                palo_carta = "oros"
            elif "🍷" in primera_carta:
                palo_carta = "copas"
            elif "⚔️" in primera_carta:
                palo_carta = "espadas"
            elif "🌿" in primera_carta:
                palo_carta = "bastos"

            if palo_carta in caballos:
                if caballos[palo_carta] > 0:
                    caballos[palo_carta] = caballos[palo_carta] - 1
                    print(f"\nLa carta volteada es {primera_carta} -> {palo_carta} retrocede una casilla!\n")

def jugar_carrera():
    """Ejecuta la carrera de caballos con apuestas."""
    baraja = crear_baraja()
    barajar(baraja)
    caballos = inicializar_carrera()
    cartas_fuera = []

    print("Bienvenido a la carrera de caballos con naipes!\n")
    eleccion = input("Apuesta por un caballo (oros, copas, espadas, bastos): ").strip().lower()
    while eleccion not in caballos:
        eleccion = input("Opción inválida. Ingresa un palo válido (oros, copas, espadas, bastos): ").strip().lower()

    input("Presiona [ENTER] para iniciar la carrera...")

    meta = 6  # Definir la meta para los caballos, en este caso son seis cartas
    ganador = None

    while not ganador:
        carta = baraja.pop()
        cartas_fuera.append(carta[2])
        if carta[1] in caballos:
            caballos[carta[1]] += 1
            print(f"Salió la carta {carta[2]} -> {carta[1]} avanza!")
        mostrar_pista(caballos)

        retroceso(caballos, cartas_fuera)  # Verifica si debe voltear una carta del camino

        if caballos[carta[1]] >= meta:
            ganador = carta[1]

        input("Presiona [ENTER] para continuar")

    print(f"\nEl caballo {ganador} ha ganado la carrera! 🏆")
    print("Cartas jugadas en la carrera:", ' '.join(cartas_fuera))

    if ganador == eleccion:
        print("¡Felicidades! Tu caballo ganó la apuesta! :)")
    else:
        print("Lo siento, tu caballo no ganó esta vez. :(")


if __name__ == "__main__":
    jugar_carrera()
