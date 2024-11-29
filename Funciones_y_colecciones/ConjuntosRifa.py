print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 25 noviembre del 24                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Conjuntos Rifa                                                    * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")


'''
Este programa es una rifa, 
en donde se registra el correo electrónico y solamente permite ingresar un correo por participante.
Se debe mostrar el siguiente menú:
  ***  Rifa de una computadora  ***
1) Ver correos de participantes.
2) Agregar correo de participante.
3) Eliminar correo de participante.
4) Seleccionar ganador.
0) Salir.
Cualquier otro caso -> Opción no válida.
Para ello:
a) Utilice un conjunto para almacenar los correos de los participantes.
b) Utilice un valor aleatorio utilizando la función random.choice(lista). 
Notar que hay que convertir primero a una lista.
'''
import random #La función random.choice pertenece al módulo random, es por eso que se debe de improtar

#Declaración del conjunto
conjunto_correos = set() #Conjunto vacío
#Declaración de la lista

def menu():
    print("   ***  Rifa de una computadora  *** ")
    print("[1].- Ver correos de participantes.")
    print("[2].- Agregar correo de participante.")
    print("[3].- Eliminar correo de participante.")
    print("[4].- Seleccionar ganador.")
    print("[0].- Salir")

def funcion_rifa(opcion):
    if opcion == 1: #Ver correos de participantes
        if not conjunto_correos:
            print("Aún no hay elementos para mostrar:( ")
        for correo in conjunto_correos:
            print(f"+ {correo}")
    if opcion == 2: #Agregar correo de participantes
        correo_add = input("Ingrese correo del participante: ")
        conjunto_correos.add(correo_add)
        print(f" Se añadió a {correo_add} :) ")
    if opcion == 3: #Eliminar correo de participante
        if not conjunto_correos: #Si el conjunto está vació
            print("Aún no hay elementos para mostrar:( ")
        for correo in conjunto_correos: #Imprime los elementos para que el usuario indique cuales eliminar
            print(f"+ {correo}")
        else:
            correo_delete = input("Ingrese el correo del participante a eliminar: ")
            conjunto_correos.remove(correo_delete)
            print(f"Se eliminó {correo_delete}")
    if opcion == 4: #Seleccionar ganador
        if not conjunto_correos:
            print("No hay elementos para mostrar :(")
        else:
            #Primero se debe convertir a lista para usar la función random.choice
            lista_correos = list(conjunto_correos)
            #Ahora ya se puede elegir a un ganador
            print(f"El ganador es { random.choice(lista_correos)}")

flag = 0 #Bandera para controlar el ciclo while
while flag == 0:
    menu() #Se manda a llamar a la función menú, como su única utilidad es imprimir pues no se le manda ningún argumento
    opcion = int(input("Ingrese una opción: ")) #Se lee una opción por teclado
    funcion_rifa(opcion) #Se manda a llamar la función rifa, y como su lógica trabaja según la opción, pues como argumento se le manda la opción
    if opcion == 0: #si la opción es salir
        print("Saliendo del programa...") #Imprime este letrero justo antes de salir
        flag = 1 #Se cambia el valor de bandera para romper el ciclo



