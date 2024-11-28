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
        correo_delete = input("Ingrese el correo del participante a eliminar: ")
        conjunto_correos.remove(correo_delete)
    if opcion == 4: #Seleccionar ganador
        #Primero se debe convertir a lista para usar la función random.choice
        lista_correos = list(conjunto_correos)
        #Ahora ya se puede elegir a un ganador
        print(f"El ganador es {random.choice(lista_correos)}")


