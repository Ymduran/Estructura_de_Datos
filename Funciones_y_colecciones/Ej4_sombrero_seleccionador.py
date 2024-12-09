print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 07 de diciembre de 24                                     * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Ejercicio 4. Test del sombrero seleccionador de Harry Potter.    * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

'''
import random

# Diccionario de respuestas y casas
diccionario_respuestas = {
    'Ordinario': 'Gryffindor',
    'Ignorante': 'Slytherin',
    'Cobarde': 'Hufflepuff',
    'Egoísta': 'Ravenclaw',
    
    'Te extraña, pero sonríe': 'Gryffindor',
    'Pide más historias sobre tus aventuras': 'Slytherin',
    'Piensa con admiración tus logros': 'Hufflepuff',
    'No me importa lo que piensen de mí después de mi muerte, lo que piensen de mí ahora es lo que cuenta': 'Ravenclaw',
    
    'Gloria': 'Gryffindor',
    'Sabiduría': 'Slytherin',
    'Amor': 'Hufflepuff',
    'Poder': 'Ravenclaw',
    
    'Valiente': 'Gryffindor',
    'Ambicioso': 'Slytherin',
    'Leal': 'Hufflepuff',
    'Curioso': 'Ravenclaw',
    
    'La fuerza': 'Gryffindor',
    'La astucia': 'Slytherin',
    'La paciencia': 'Hufflepuff',
    'La inteligencia': 'Ravenclaw',
    
    'Vuelo': 'Gryffindor',
    'Defensa contra las artes oscuras': 'Slytherin',
    'Animales fantásticos': 'Hufflepuff',
    'Pociones': 'Ravenclaw',
    
    'C': 'Gryffindor',
    'Python': 'Slytherin',
    'C++': 'Hufflepuff',
    'JavaScript': 'Ravenclaw'
}

# Preguntas y sus respuestas posibles
preguntas = {
    "¿Cuál de las siguientes opciones odiarías más que la gente te llamara?": {"Ordinario", "Ignorante", "Cobarde", "Egoísta"},
    "Después de tu muerte, ¿qué es lo que más te gustaría que hiciera la gente cuando escuche tu nombre?": {
        "Te extraña, pero sonríe", "Pide más historias sobre tus aventuras", 
        "Piensa con admiración tus logros", "No me importa lo que piensen de mí después de mi muerte, lo que piensen de mí ahora es lo que cuenta"
    },
    "Dada la opción, preferirías inventar una poción que garantizara:": {"Gloria", "Sabiduría", "Amor", "Poder"},
    "¿Cómo te definirías en una sola palabra?": {"Valiente", "Ambicioso", "Leal", "Curioso"},
    "¿Qué cualidad te describe mejor?": {"La fuerza", "La astucia", "La paciencia", "La inteligencia"},
    "¿Cuál es tu clase favorita?": {"Vuelo", "Defensa contra las artes oscuras", "Animales fantásticos", "Pociones"},
    "¿Cuál es tu lenguaje de programación favorito?": {"C", "Python", "C++", "JavaScript"}
}

# Función para iniciar el test
def iniciar_test():
    print("\n*** Test del sombrero seleccionador de Harry Potter ***\n")
    print("Este programa determina la casa (Gryffindor, Slytherin, Hufflepuff y Ravenclaw) a la que perteneces, de acuerdo a tus respuestas.\n")
    respuestas = []
    
    # Iterar sobre las preguntas en orden
    for pregunta, opciones in preguntas.items():
        print(pregunta)
        opciones = list(opciones)
        random.shuffle(opciones)  # Barajar las opciones
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}) {opcion}")
        while True:
            try:
                eleccion = int(input("Respuesta: ")) - 1
                if eleccion < 0 or eleccion >= len(opciones):
                    raise ValueError("Opción no válida.")
                respuestas.append(diccionario_respuestas[opciones[eleccion]])
                break
            except (ValueError, IndexError):
                print("Por favor, elige una opción válida.")
    
    # Calcular la casa
    casa = max(set(respuestas), key=respuestas.count)
    print(f"\n¡El sombrero seleccionador te asigna a la casa **{casa}**!\n")

# Programa principal
def main():
    while True:
        print("\n*** Ejercicio 4. Test del sombrero seleccionador de Harry Potter. ***")
        print("1) Iniciar test.")
        print("0) Salir.")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            iniciar_test()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()

'''

'''
import random

# Diccionario de respuestas y casas
diccionario_respuestas = {
    'Ordinario': 'Gryffindor',
    'Ignorante': 'Slytherin',
    'Cobarde': 'Hufflepuff',
    'Egoísta': 'Ravenclaw',
    
    'Te extraña, pero sonríe': 'Gryffindor',
    'Pide más historias sobre tus aventuras': 'Slytherin',
    'Piensa con admiración tus logros': 'Hufflepuff',
    'No me importa lo que piensen de mí después de mi muerte, lo que piensen de mí ahora es lo que cuenta': 'Ravenclaw',
    
    'Gloria': 'Gryffindor',
    'Sabiduría': 'Slytherin',
    'Amor': 'Hufflepuff',
    'Poder': 'Ravenclaw',
    
    'Valiente': 'Gryffindor',
    'Ambicioso': 'Slytherin',
    'Leal': 'Hufflepuff',
    'Curioso': 'Ravenclaw',
    
    'La fuerza': 'Gryffindor',
    'La astucia': 'Slytherin',
    'La paciencia': 'Hufflepuff',
    'La inteligencia': 'Ravenclaw',
    
    'Vuelo': 'Gryffindor',
    'Defensa contra las artes oscuras': 'Slytherin',
    'Animales fantásticos': 'Hufflepuff',
    'Pociones': 'Ravenclaw',
    
    'C': 'Gryffindor',
    'Python': 'Slytherin',
    'C++': 'Hufflepuff',
    'JavaScript': 'Ravenclaw'
}

# Preguntas y respuestas
preguntas = {
    "¿Cuál de las siguientes opciones odiarías más que la gente te llamara?": {"Ordinario", "Ignorante", "Cobarde", "Egoísta"},
    "Después de tu muerte, ¿qué es lo que más te gustaría que hiciera la gente cuando escuche tu nombre?": {
        "Te extraña, pero sonríe", "Pide más historias sobre tus aventuras", 
        "Piensa con admiración tus logros", "No me importa lo que piensen de mí después de mi muerte, lo que piensen de mí ahora es lo que cuenta"
    },
    "Dada la opción, preferirías inventar una poción que garantizara:": {"Gloria", "Sabiduría", "Amor", "Poder"},
    "¿Cómo te definirías en una sola palabra?": {"Valiente", "Ambicioso", "Leal", "Curioso"},
    "¿Qué cualidad te describe mejor?": {"La fuerza", "La astucia", "La paciencia", "La inteligencia"},
    "¿Cuál es tu clase favorita?": {"Vuelo", "Defensa contra las artes oscuras", "Animales fantásticos", "Pociones"},
    "¿Cuál es tu lenguaje de programación favorito?": {"C", "Python", "C++", "JavaScript"}
}

# Función para iniciar el test
def iniciar_test():
    print("\n*** Test del sombrero seleccionador de Harry Potter ***\n")
    print("Este programa determina la casa (Gryffindor, Slytherin, Hufflepuff y Ravenclaw) a la que perteneces, de acuerdo a tus respuestas.\n")
    respuestas = []
    
    # Seleccionar 5 preguntas aleatorias
    preguntas_seleccionadas = random.sample(list(preguntas.items()), 5)
    
    for pregunta, opciones in preguntas_seleccionadas:
        print(pregunta)
        opciones = list(opciones)
        random.shuffle(opciones)  # Barajar las opciones
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}) {opcion}")
        while True:
            try:
                eleccion = int(input("Respuesta: ")) - 1
                if eleccion < 0 or eleccion >= len(opciones):
                    raise ValueError("Opción no válida.")
                respuestas.append(diccionario_respuestas[opciones[eleccion]])
                break
            except (ValueError, IndexError):
                print("Por favor, elige una opción válida.")
    
    # Calcular la casa
    casa = max(set(respuestas), key=respuestas.count)
    print(f"\n¡El sombrero seleccionador te asigna a la casa **{casa}**!\n")

# Programa principal
def main():
    while True:
        print("\n*** Ejercicio 4. Test del sombrero seleccionador de Harry Potter. ***")
        print("1) Iniciar test.")
        print("0) Salir.")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            iniciar_test()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()

'''
#Diccionarios de las respuestas
diccionario_respuestas = {
    'Ordinario': 'Gryffindor',
    'Ignorante': 'Slytherin',
    'Cobarde': 'Hufflepuff',
    'Egoísta': 'Ravenclaw',
    
    'Te extraña, pero sonríe': 'Gryffindor',
    'Pide más historias sobre tus aventuras': 'Slytherin',
    'Piensa con admiración tus logros': 'Hufflepuff',
    'No me importa lo que piensen de mí después de mi muerte, lo que piensen de mí ahora es lo que cuenta': 'Ravenclaw',
    
    'Gloria': 'Gryffindor',
    'Sabiduría': 'Slytherin',
    'Amor': 'Hufflepuff',
    'Poder': 'Ravenclaw',
    
    'Valiente': 'Gryffindor',
    'Ambicioso': 'Slytherin',
    'Leal': 'Hufflepuff',
    'Curioso': 'Ravenclaw',
    
    'La fuerza': 'Gryffindor',
    'La astucia': 'Slytherin',
    'La paciencia': 'Hufflepuff',
    'La inteligencia': 'Ravenclaw',
    
    'Vuelo': 'Gryffindor',
    'Defensa contra las artes oscuras': 'Slytherin',
    'Animales fantásticos': 'Hufflepuff',
    'Pociones': 'Ravenclaw',
    
    'C': 'Gryffindor',
    'Python': 'Slytherin',
    'C++': 'Hufflepuff',
    'JavaScript': 'Ravenclaw'
}

# Conjunto respuestas de la primera pregunta
# Conjunto respuestas de la primera pregunta
A = {"Ordinario", "Ignorante", "Cobarde", "Egoísta"}
# Conjunto respuestas de la segunda pregunta
B = {"Te extraña, pero sonríe", "Pide más historias sobre tus aventuras", "Piensa con admiración tus logros", "No me importa lo que piensen de mí después de mi muerte, lo que piensen de mí ahora es lo que cuenta"}
# Conjunto respuestas de la tercera pregunta
C = {"Gloria", "Sabiduría", "Amor", "Poder"}
# Conjunto respuestas de la cuarta pregunta
D = {"Valiente", "Ambicioso", "Leal", "Curioso"}
# Conjunto respuestas de la quinta pregunta
E = {"La fuerza", "La astucia", "La paciencia", "La inteligencia"}
# Conjunto respuestas de la sexta pregunta
F = {"Vuelo", "Defensa contra las artes oscuras", "Animales fantásticos", "Pociones"}
# Conjunto respuestas de la séptima pregunta
G = {"C", "Python", "C++", "JavaScript"}



print("¿Cuál de las siguientes opciones odiarías más que la gente te llamara?")
lista_respuestas = list(A)
coun = 1
for i in lista_respuestas:
    print(f"{coun}) {i} ")
    coun += 1
respuesta_primer_pregunta = int(input("Respuesta: "))

