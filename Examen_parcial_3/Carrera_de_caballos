import random # Importa el módulo random para generar números aleatorios y barajar la baraja

def crear_baraja() -> list[tuple[int, str, str]]:
    """
    Crea una baraja española sin ochos ni nueves.
    :return: Lista de tuplas que representan la baraja.
    """
    palos = {'oros': '🟡', 'copas': '🍷', 'espadas': '⚔️', 'bastos': '🌿'} #Diccionario con los palos y sus símbolos
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12] #Lista con los valores de las cartas
    return [(valor, palo, f"{valor}{simbolo}") for palo, simbolo in palos.items() for valor in valores] #para crear la baraja

def barajar(baraja: list[tuple[int, str, str]]) -> None:
    """
    Baraja las cartas.
    :param baraja: Lista de cartas a barajar.
    """
    random.shuffle(baraja) #Baraja la lista de cartas

def inicializar_carrera() -> dict[str, int]:
    """
    Inicializa los caballos en la posición de salida.
    :return: Diccionario con los caballos y su posición inicial en 0.
    """
    return {'oros': 0, 'copas': 0, 'espadas': 0, 'bastos': 0} #Diccionario con los caballos y su posición inicial

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

def retroceso(caballos: dict[str, int], cartas_fuera: list[str]) -> None:
    """
    Voltea la primera carta y hace retroceder al caballo correspondiente si todos han avanzado al menos una casilla.
    :param caballos: Diccionario con los caballos y su posición actual.
    :param cartas_fuera: Lista de cartas jugadas en la carrera.
    : return: no retorna nada
    """
    if all(pos > 0 for pos in caballos.values()) and cartas_fuera: #Sí todos los caballos han avanzado y hay cartas jugadas
        primera_carta = cartas_fuera.pop(0) #obtiene la primera carta jugada y la elimina de la lista
        palo_carta = next((p for p, s in {'oros': '🟡', 'copas': '🍷', 'espadas': '⚔️', 'bastos': '🌿'}.items() if s in primera_carta), None) #Obtiene el palo de la carta
        if palo_carta and caballos[palo_carta] > 0: #Sí existe el palo  y el caballo ha avanzado
            caballos[palo_carta] -= 1#Retrocede al caballo
            print(f"\nLa carta volteada es {primera_carta} -> {palo_carta} retrocede una casilla!\n") #Es para mostrar al ususario qué caballo retrocede

def jugar_carrera() -> None:
    """
    Ejecuta la carrera de caballos con apuestas.
    """
    
    
    print(r"    ____      _      ____    ____    _____   ____       _        ____    _____     _   _      _      ___   ____    _____   ____   ")
    print(r"   / ___|    / \    |  _ \  |  _ \  | ____| |  _ \     / \      |  _ \  | ____|   | \ | |    / \    |_ _| |  _ \  | ____| / ___|  ")
    print(r"  | |       / _ \   | |_) | | |_) | |  _|   | |_) |   / _ \     | | | | |  _|     |  \| |   / _ \    | |  | |_) | |  _|   \___ \  ")
    print(r"  | |___   / ___ \  |  _ <  |  _ <  | |___  |  _ <   / ___ \    | |_| | | |___    | |\  |  / ___ \   | |  |  __/  | |___   ___) | ")
    print(r"   \____| /_/   \_\ |_| \_\ |_| \_\ |_____| |_| \_\ /_/   \_\   |____/  |_____|   |_| \_| /_/   \_\ |___| |_|     |_____| |____/  ")
        
        
        
    
    baraja = crear_baraja()
    barajar(baraja)
    caballos = inicializar_carrera()
    cartas_fuera = [] #Para inicializar la lista de cartas jugadas

    eleccion = input("Apuesta por un caballo (oros, copas, espadas, bastos): ").strip().lower() #Pide al usuario que elija un caballo
    while eleccion not in caballos: #Mientras la elección no sea válida
        eleccion = input("Opción inválida. Ingresa un palo válido (oros, copas, espadas, bastos): ").strip().lower() #Pedirá al usuario que vuelva a elegir

    input("Presiona [ENTER] para iniciar la carrera...") 
    meta = 6 #Define la meta de la carrera
    ganador = None #Inicializa al ganador

    while not ganador: #mientras no haya ganador
        carta = baraja.pop() #Elimina la primera carta de la baraja 
        cartas_fuera.append(carta[2]) #Después añade la carta a la lista de cartas jugadas
        if carta[1] in caballos: #Sí el palo de la carta está en los caballos
            caballos[carta[1]] += 1 #Avanza el caball
            print(f"Salió la carta {carta[2]} -> {carta[1]} avanza!") #Impirme cuál avanza
        
        mostrar_pista(caballos)
        retroceso(caballos, cartas_fuera) #Verifica sí hay retroceso
        
        if caballos[carta[1]] >= meta: #Sí el caballo ha llegado a la meta
            ganador = carta[1] #El caballo es el ganador
        
        input("Presiona [ENTER] para continuar")

    print(f"\nEl caballo {ganador} ha ganado la carrera! 🏆")
    print("Cartas jugadas en la carrera:"| ' '.join(cartas_fuera)) #Muestra todas las cartas que jugaron

    if ganador == eleccion:
        print("¡Felicidades! Tu caballo ganó la apuesta! :)")
    else:
        print("Lo siento, tu caballo no ganó esta vez. :(")

if __name__ == "__main__":
    jugar_carrera()
