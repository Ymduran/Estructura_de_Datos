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

# Lista de palabras
lista_palabras_adivinar = ["variable", "algoritmo", "prototipo"]

# Seleccionar una palabra al azar
palabra_adivinar = random.choice(lista_palabras_adivinar)

# Mostrar la pista inicial con la primera letra visible
print("  ☺")
print(" /|\🍟")
print(" / \ ")
print("\n")

print("Adivina la palabra:")
progreso = [letra if indice == 0 else "_" for indice, letra in enumerate(palabra_adivinar)]
print(" ".join(progreso))

# Intentos restantes
intento = 0
max_intentos = 6

# Bucle principal del juego
while intento < max_intentos:
    letra_usuario = input("\nIngresa una letra: ").lower()

    if letra_usuario in palabra_adivinar:
        # Actualizar el progreso si la letra está en la palabra
        for indice, letra in enumerate(palabra_adivinar):
            if letra == letra_usuario:
                progreso[indice] = letra
        print("¡Correcto!")
    else:
        # Incrementar los intentos fallidos y mostrar el ahorcado
        intento += 1
        print("Letra incorrecta.")
        if intento == 1:
            print("  ☺")
            print(" /|\ ")
            print(" / \ ")
        elif intento == 2:
            print("  ☺")
            print(" /|")
            print(" / \ ")
        elif intento == 3:
            print("  ☺")
            print("  |")
            print(" / \ ")
        elif intento == 4:
            print("  ☺")
            print("  |")
            print("   \ ")
        elif intento == 5:
            print("  ☺")
            print("  |")
            print("    ")
        elif intento == 6:
            print("  ☹")
            print("JUEGO TERMINADO. PERDISTE :( ")
            print(f"La palabra era: {palabra_adivinar}")
            break

    # Mostrar el progreso actualizado
    print(" ".join(progreso))

    # Comprobar si se ha adivinado toda la palabra
    if "_" not in progreso:
        print("\n¡Felicidades. Has adivinado la palabra")
        break
