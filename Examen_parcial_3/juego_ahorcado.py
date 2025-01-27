import random

print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha:  24 de Enero del 2025                                     * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Juego del ahorcado                                               * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")

def inicializar_juego(lista_palabras_adivinar):
    """
    Inicializa el juego seleccionando una palabra al azar de la lista y creando el progreso inicial.

    :param lista_palabras_adivinar: Lista de palabras disponibles para adivinar.
    :return: Palabra a adivinar y progreso inicial con la primera letra visible.
    """
    palabra_adivinar = random.choice(lista_palabras_adivinar) #Elige una palabra de la lista de palabras al azar
    progreso = [letra  if indice == 0  else "_"  for indice,  letra in enumerate(palabra_adivinar)]
    return palabra_adivinar, progreso

def mostrar_ahorcado(intentos):
    """
    Muestra el estado del ahorcado basado en el número de intentos fallidos.

    :param intentos: Número de intentos fallidos.
    """
    if intentos == 1:
        print("  ☺")
        print(" /|\ ")
        print(" / \ ")
    elif intentos == 2:
        print("  ☺")
        print(" /|")
        print(" / \ ")
    elif intentos == 3:
        print("  ☺")
        print("  |")
        print(" / \ ")
    elif intentos == 4:
        print("  ☺")
        print("  |")
        print("   \ ")
    elif intentos == 5:
        print("  ☺")
        print("  |")
        print("    ")
    elif intentos == 6:
        print("  ☹")
        print("JUEGO TERMINADO. PERDISTE :( ")





def actualizar_progreso(palabra_adivinar, progreso, letra_usuario):
    """
    Actualiza el progreso del juego al verificar si la letra ingresada está en la palabra a adivinar.
♥
    :param palabra_adivinar: La palabra que se está adivinando.
    :param progreso: Lista con el progreso actual del jugador.
    :param letra_usuario: Letra ingresada por el usuario.
    :return: Progreso actualizado.
    """

    for indice, letra in enumerate(palabra_adivinar):
        if letra == letra_usuario:
            progreso[indice] = letra
    return progreso



def ejecutar_juego_ahorcado() -> None:
    # Lista de palabras
    lista_palabras_adivinar = ["variable", "algoritmo", "prototipo", "compu"]

    # Inicialización del juego
    palabra_adivinar, progreso = inicializar_juego(lista_palabras_adivinar)

    # Como pista muestra la primera letra
    print("  ☺")
    print(" /|\🍟")
    print(" / \ ")
    print("")
    print("Adivina la palabra:")
    print(" ".join(progreso))

    # Intentos
    intento = 0 #Número de
    max_intentos = 6


    flag = 0
    while intento <max_intentos:
        letra_usuario = input("Ingresa una letra: ").lower()


        if letra_usuario in palabra_adivinar:
            # Actualizar el progreso si la letra está en la palabra añadiendo (o uniendo) la letra del usuario
            progreso = actualizar_progreso(palabra_adivinar, progreso, letra_usuario)
            print("Letra correcta :)")
        else:
            # Incrementa núemro de intentos y muestra el ahorcado
            intento += 1
            print("Letra incorrecta.")
            mostrar_ahorcado(intento)
            if intento == max_intentos:
                print(f"La palabra era: {palabra_adivinar}")
                flag = 1
                break



        # Mostrar el progreso actualizado
        print(" ".join(progreso))

        # Comprobar si ha adivinado toda la palabra
        if "_" not in progreso: #Cuando ya no hay guiones
            print(f"Adivinaste la palabra {palabra_adivinar}")
            break

if __name__ == '__main__':

    ejecutar_juego_ahorcado()
