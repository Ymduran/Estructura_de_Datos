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
    print("------------------------------------------------------------------ ")
    print(" ")
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
    preguntas_seleccionadas = [] #Se crea una lista de las preguntas, las cuales se harán de forma aleatoria
    while len(preguntas_seleccionadas) < 5: #Lo hará cinco veces, pusto que solo se ocupan 5 preguntas
        indice = random.randint(0, len(preguntas) - 1) #Índice de la lista de preguntas, se seleccionará aleatoriamente
        if indice not in preguntas_seleccionadas: #Sí el índice no está entre la lista de las preguntas 
            preguntas_seleccionadas.append(indice) #Entonces lo añade en la lisrta de preguntas a mostrar

    for indice in preguntas_seleccionadas: #Ahora con la lista de preguntas hecha, en cada 
        pregunta = preguntas[indice] #Se asigna cada elemento de la lista a una variable individual
        print(f"\n{pregunta['pregunta']}") #Se imprime el elemento del diccionario desde la clave "Pregunta"
        respuestas = list(pregunta["respuestas"].items()) #Y lo combierte a una lista las respuestas del diccionario, la converión se hace con list y el ,item accede al valor del diccionario, es decir clave y diccionario
        respuestas = set(respuestas) #Se convierte a conjunto con el set con el fin de guardarlos de forma aleatoria
        respuestas = list(respuestas) #Y se vuelve a guardar como una lista con "list"
        


        # Mostrar respuestas a elegir por el usuario
        
        opciones = {str(i + 1): respuesta[1] for i, respuesta in enumerate(respuestas)} #Se asigna  a la variable "opciones" las respuestas de del diccionario de respuestas, y como no se moestrará las casa, por eso semuestra la siguiente posición
        
        for clave, valor in opciones.items(): #Para iterar en el diccionario con su clave y valor
            print(f"{clave}) {valor}") 

        # Obtener respuesta válida del usuario
        flag = 0
        while flag == 0:
            respuesta = input("Respuesta: ").strip()
            if respuesta in opciones:
                # Buscar la casa correspondiente a la respuesta
                for casa, texto in pregunta["respuestas"]:
                    if opciones[respuesta] == texto:
                        puntuaciones[casa] += 1 #Se suma a los puntos de la casa 
                flag = 1
            else:
                print("Opción no válida :(")

    # Para obtener la casa con mayor puntuación
    casa_seleccionada = max(puntuaciones, key=puntuaciones.get)
    
    
    
    
    print(f"\nEl sombrero seleccionador te ha asignado a la casa {casa_seleccionada}.\n")

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

