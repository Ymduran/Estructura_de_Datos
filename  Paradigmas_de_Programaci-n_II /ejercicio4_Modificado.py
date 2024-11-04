from random import randint

print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 04 noviembre del 2024                                     * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" *  Ejercicio4_juego_adivinador.py                                  * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")


'''
Este programa es un juego en donde el usuario intente adivinar un número secreto.
Para ello:
a) El número a adivinar es un número aleatorio entre 1 y 100.
b) El jugador tendrá 5 intentos para encontrar el número.
c) Como pista, el juego indicará si el número a adivinar es menor o mayor al número ingresado, si el número no es el correcto.
d) Si el jugador adivina el número, el juego muestra un mensaje de felicitación y el número de intentos.
e) Si el jugador no adivina el número, el juego muestra un mensaje con el número.
'''
print(" ** JUEGO DEL ADIVINADOR ** ")

print("[f]. Fácil")
print("[m]. Medio")
print("[d]. Difícil")
dificultad=input("Seleccione la dificultad: ")
dificultad=dificultad.lower()
print(" ")


if dificultad == "f":
    random_number = randint(1, 50)
    numero_intentos= 10
elif dificultad == "m":
    random_number = randint(1, 100)
    numero_intentos = 5
elif dificultad == "d":
    random_number = randint(1, 110)
    numero_intentos = 4


counter = 1
flag = 0


while counter <= numero_intentos and flag == 0:
    number = int(input(f"Número de intento {counter}. Ingrese un número: "))
    if number < random_number:
        print("El número a divinar es mayor ")
    elif number > random_number:
        print("El número a divinar es menor ")
    elif number == random_number:
        print("Felicitaciones, acertaste el número")
        flag = 1
    counter += 1

if counter == (numero_intentos+1) and flag==0:
    print("Máximo número de intentos :(")
    print(f"El número es {random_number}")