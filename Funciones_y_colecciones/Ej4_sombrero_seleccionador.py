print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 09 de diciembre de 24                                     * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Ej2_conversiones_decimal_binario_hexadecimal                     * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

print("\n** Test del Sombrero Seleccionador**\n")
import random

def menu():
    print("** Menú **")
    print("[1].- Iniciar test.")
    print("[2].- Salir.")
    opcion = int(input("Ingresa número: "))
    return opcion




    # Lista de diccionario de preguntas y respuestas
    preguntas = [
        {"pregunta": "¿Cuál de las siguientes opciones odiarías más que la gente te llamara?",
         "respuestas": {"Gryffindor": "Ordinario", "Slytherin": "Ignorante", "Hufflepuff": "Cobarde", "Ravenclaw": "Egoísta"}},
        {"pregunta": "Después de tu muerte, ¿qué es lo que más le gustaría que hiciera la gente cuando escuche tu nombre?",
         "respuestas": {"Gryffindor": "Te extraña, pero sonríe", "Slytherin": "Pide más historias sobre tus aventuras","Hufflepuff": "Piensa con admiración tus logros","Ravenclaw": "No me importa lo que piensen de mí después de mi muerte, lo que piensen de mí ahora es lo que cuenta"}},
        {"pregunta": "Dada la opción, ¿preferirías inventar una poción que garantizara?",
         "respuestas": {"Gryffindor": "Gloria", "Slytherin": "Sabiduría", "Hufflepuff": "Amor", "Ravenclaw": "Poder"}},
        {"pregunta": "¿Cómo te definirías en una sola palabra?",
         "respuestas": {"Gryffindor": "Valiente", "Slytherin": "Ambicioso", "Hufflepuff": "Leal", "Ravenclaw": "Curioso"}},
        {"pregunta": "¿Qué cualidad te describe mejor?",
         "respuestas": {"Gryffindor": "La fuerza", "Slytherin": "La astucia", "Hufflepuff": "La paciencia", "Ravenclaw": "La inteligencia"}},
        {"pregunta": "¿Cuál es tu clase favorita?",
         "respuestas": {"Gryffindor": "Vuelo", "Slytherin": "Defensa contra las artes oscuras","Hufflepuff": "Animales fantásticos", "Ravenclaw": "Pociones"}},
        {"pregunta": "¿Cuál es tu lenguaje de programación favorito?",
         "respuestas": {"Gryffindor": "C", "Slytherin": "Python", "Hufflepuff": "C++", "Ravenclaw": "JavaScript"}}
    ]

    # Diccionario contador de puntos de cada casa
    puntuaciones = {"Gryffindor": 0, "Slytherin": 0, "Hufflepuff": 0, "Ravenclaw": 0}

    # Selección de preguntas sin repetir
    preguntas_seleccionadas = [] #Se crea una lista
    while len(preguntas_seleccionadas) < 5:
        indice = random.randint(0, len(preguntas) - 1)
        if indice not in preguntas_seleccionadas:
            preguntas_seleccionadas.append(indice)

    for indice in preguntas_seleccionadas:
        pregunta = preguntas[indice]
        print(f"\n{pregunta['pregunta']}")
        respuestas = list(pregunta["respuestas"].items())
        random.shuffle(respuestas)  # Ordenar aleatoriamente las opciones

        # Mostrar opciones
        opciones = {str(i + 1): respuesta[1] for i, respuesta in enumerate(respuestas)}
        for clave, valor in opciones.items():
            print(f"{clave}) {valor}")

        # Obtener respuesta válida del usuario
        while True:
            respuesta = input("Selecciona una opción (1-4): ").strip()
            if respuesta in opciones:
                # Buscar la casa correspondiente a la respuesta
                for casa, texto in pregunta["respuestas"].items():
                    if opciones[respuesta] == texto:
                        puntuaciones[casa] += 1
                break
            else:
                print("Opción no válida. Intenta nuevamente.")

    # Determinar la casa con mayor puntuación
    casa_seleccionada = max(puntuaciones, key=puntuaciones.get)
    print(f"\n¡Felicidades! El sombrero seleccionador te ha asignado a la casa {casa_seleccionada}.\n")

def seleccion(opcion):
    if opcion == 1:
        iniciar_test()
    elif opcion == 2:
        print("Saliendo...")
    else:
        print("Opción no válida. Intenta nuevamente.")

# Menú principal
print("***  Test del sombrero seleccionador de Harry Potter.  ***")

opcion = 0
while opcion != 2:
    opcion = menu()
    seleccion(opcion)
