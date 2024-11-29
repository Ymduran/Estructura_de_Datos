

print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 25 noviembre del 24                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Conjuntos Juego sin repetir                                       * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")


'''
Este es un juego que se puede jugar de manera grupal,
 en donde el objetivo es decir palabras de un tema en específico y 
 los jugadores deben tratar de no repetir la misma palabra.
  Nota: no se debe mostrar las palabras en ningún caso.
 Además, se debe llevar un contador de la cantidad de palabras que llevan.
Se debe mostrar el siguiente menú:
  ***  Juego "sin repetir"  ***
    Mostrar las reglas del juego.
    Presiona 'enter' para comenzar.
Para ello:
a) Utilice un conjunto para almacenar las palabras ingresadas.
b) Utilice la lógica adecuada para realizar el juego.
c) Al final, se deben mostrar todas las palabras ingresadas.
'''
flag = 0 #Bandera para controlar
word_count = 1 #Contador de palabras
conjunto_palabras = set()
topic = input("Ingrese el tema del juego: ")
while flag == 0:
    word = input(f"Ingrese palabra {word_count} del tema de {topic}: ")
    for palabra in conjunto_palabras:
        if word == palabra:
            print(f"El juego ha terminado, han dicho {word_count} palabras diferentes")
            print(palabra)
            flag = 1
        else:
            conjunto_palabras.add(word)
            word_count += 1




