import random

print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha:  26 de Enero del 2025                                     * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Juego cuatro en raya                                             * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")





'''
Las reglas del juego 4 en raya son las siguientes: 
Dos jugadores compiten por alinear cuatro piezas de su color en una fila.
Cada jugador elige un color de fichas.
Los jugadores se turnan para colocar sus fichas en las columnas del tablero.
Las fichas no se pueden mover una vez colocadas.
El jugador que primero alinee cuatro fichas gana.
Si no hay un ganador, el juego termina en empate.
'''




def menu() -> None:
    """
    Muestra el menú  del juego de Cuatro en Raya.
    """
    print("** MENÚ CUATRO EN RAYA**")
    print("1. Jugar contra otro jugador")
    print("2. Jugar contra la CPU")
    print("3. Salir")






def mostrar_tablero(tablero: list) -> None:
    """
    Muestra el tablero del juego

    :param tablero: Lista como representación del tablero
    """
    print("\n")
    for fila in tablero:
        print(" | ".join(fila)) #El join es para unir una lista con sublistas
        print("-" * 29)
    print("\n")





def verificar_ganador(tablero: list, jugador: str) -> bool:
    """
    Verifica si un jugador ha ganado el juego

    :param tablero: Lista que representa el tablero
    :param jugador: Carácter de cada jugador, X u O
    :return: True si jugador gana, o false si pierde
    """
    # Verificar filas
    for fila in tablero:
        for col in range(4):
            if all(fila[col + i] == jugador for i in range(4)): #Retorna verdadero si todos los elementos de la fila elinean cuatro elementos
                return True

    # Verificar columnas
    for columna in range(7):
        for fila in range(3):
            if all(tablero[fila + i][columna] == jugador for i in range(4)): #Retorna verdadero si todos los elementos en la columna alinean 4 elementos
                return True

    # Verificar diagonales de izquierda a derecha
    for fila in range(3):
        for columna in range(4):
            if all(tablero[fila + i][columna + i] == jugador for i in range(4)):
                return True

    # Verificar diagonales (de derecha a izquierda)
    for fila in range(3):
        for columna in range(3, 7):
            if all(tablero[fila + i][col - i] == jugador for i in range(4)):
                return True

    return False





def columna_valida(tablero: list, columna: int) -> bool:
    """
    Verifca si una columna es válida para realizar un movimiento

    :param tablero: Lista para representar el tablero
    :param columna: Número de columna (0 a 6)
    :return: True si la columna es válida, False en caso contrario
    """
    return 0 <= columna < 7 and tablero[0][columna] == " " #Retorna un valor en booleano, en este caso para verificar si la columna es válida pues debe cumplir que esté dentro del rango.




def realizar_movimiento(tablero: list, columna: int, jugador: str) -> None: 
    """
    Realiza un movimiento en la columna especificada para el jugador dado

    :param tablero: Lista para representar el tablero
    :param columna: Número de columna (0 a 6)
    :param jugador: Carácter que representa al jugador ('X' u 'O').
    """
    for fila in reversed(range(6)):
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador
            break






def movimiento_cpu(tablero: list) -> int:
    """
    Realiza un movimiento aleatorio para la CPU en aleatorio

    :param tablero: Lista bidimensional que representa el tablero.
    :return: Columna donde la CPU realizó el movimiento
    """
    columnas_validas = [columna for columna in range(7) if columna_valida(tablero, columna)]
    return random.choice(columnas_validas)







def jugar_contra_jugador() -> None:
    """
    Inicia una partida de Cuatro en Raya entre dos jugadores.
    """
    tablero = [[" " for _ in range(7)] for _ in range(6)]
    mostrar_tablero(tablero)
    turno = "X"


    while True:
        print(f"Turno de {turno}")
        columna = int(input("Selecciona una columna: "))

        while not columna_valida(tablero, columna):
            print("Columna inválida. Intenta de nuevo.")
            columna = int(input("Selecciona una columna : "))

        realizar_movimiento(tablero, columna, turno)
        mostrar_tablero(tablero)

        if verificar_ganador(tablero, turno):
            print()
            print(f" {turno} ha ganado!")
            break

        if all(tablero[0][col] != " " for col in range(7)):
            print()
            print("¡Empate!")
            break

        turno = "O" if turno == "X" else "X" #Turno 





def jugar_contra_cpu() -> None:
    """
    Inicia una partida de Cuatro en Raya contra la CPU.
    """
    tablero = [[" " for _ in range(7)] for _ in range(6)]
    mostrar_tablero(tablero)
    turno = "X"



    flag = 0
    while True:
        if turno == "X":
            print("Tu turno:")
            columna = int(input("Selecciona una columna (0 a 6): "))

            while not columna_valida(tablero, columna):
                print("Columna inválida. Intenta de nuevo.")
                columna = int(input("Selecciona una columna (0 a 6): "))
        else:
            print("Turno de la CPU:")
            columna = movimiento_cpu(tablero)

        realizar_movimiento(tablero, columna, turno)
        mostrar_tablero(tablero)

        if verificar_ganador(tablero, turno):
            print(f"{turno} ha ganado!")
            flag = 1
            break


        if all(tablero[0][col] != " " for col in range(7)):
            print("¡Empate!")
            break

        turno = "O" if turno == "X" else "X"
        




def iniciar_menu() -> int:
    """
    Inicia el menú para solicitar una opción al usuario

    :return: Opción seleccionada por el usuario
    """
    opcion = input("Selecciona una opción: ")
    while opcion not in ["1", "2", "3"]:
        print("Opción inválida. Por favor, selecciona 1, 2 o 3.")
        opcion = input("Selecciona una opción: ")
    return int(opcion)




def ejecutar_cuatro_en_raya() -> None:
    while True:
        menu()
        opcion = iniciar_menu()
        if opcion == 1:
            jugar_contra_jugador()
        elif opcion == 2:
            jugar_contra_cpu()
        elif opcion == 3:
            print("Saliendo...")
            break
if __name__ == '__main__':
    ejecutar_cuatro_en_raya()