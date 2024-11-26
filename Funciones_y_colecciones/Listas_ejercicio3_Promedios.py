
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 07 de noviembre del 2024                                   * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" *  Promedios      primer parcial                                    * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")
print(" ")

'''
Este programa es una lista de las calificaciones de los alumnos del Parcial 1. La lista está conformada por el nombre del alumno y sus calificaciones.
Cada alumno tiene 5 calificaciones: estructuras de datos, derecho, contabilidad, álgebra y electrónica.
Se debe mostrar el siguiente menú:
  ***  Calificaciones del Parcial 1  ***
1) Ver calificaciones de todos los alumnos.
2) Ver calificaciones detalladas de un alumno.
3) Ver promedios del Parcial 1 de todos los alumnos.
4) Ver promedio grupal del Parcial 1.
5) Agregar alumno y sus calificaciones.
6) Eliminar alumno y sus calificaciones.
0) Salir.
Cualquier otro caso -> Opción no válida.
'''

def menu():
    print(" ***  Calificaciones del Parcial 1  *** ")
    print("1) Ver calificaciones de todos los alumnos. ")
    print("2) Ver calificaciones detalladas de un alumno. ")
    print("3) Ver promedios del Parcial 1 de todos los alumnos. ")
    print("4) Ver promedio grupal del Parcial 1. ")
    print("5) Agregar alumno y sus calificaciones. ")
    print("6) Eliminar alumno y sus calificaciones. ")
    print("0) Salir. ")

#Código nivel de módulo
flag = 0 #Se usa una bandera para el while
while flag = 0:
    menu()#Se manda a llamar la función menú, cuya función solo es mostrar el mení, por lo que no se le manda nada
    option = int(input("Ingresa una opción: "))
    funcion_operaciones_segun_menu(option)
    print(" ")
    if option == 0:
        print("Saliendo...")#Imprime este letrero justo antes de salir
        flag = 1 #Cambia el valor de la bandera rompiendo el ciclo while


#Declaración de las listas
calificaciones = [ Contabilidad. Algebra, Derecho, Electronica ]
alumnos = []
un_alumno = [nombre,calificaciones]

#Operaciones
def funcion_operaciones_segun_menu(option):
    count = 0
    if option == 1:#------------------------------> Ver calificaciones de todos los alumnos.
        for alumno in alumnos:
            print(f"{count}.- {alumno}")
            count += 1
        elif not alumnos:
            print("Aún no hay alumnos para mostrar")
    if option == 2:  #------------------------------> Ver calificaciones detalladas de un alumno.
        indice = int(input("Ingrese número de índice del alumno a mostrar"))
        print(alumnos[indice])
        elif not alumnos:
            print("Aún no hay alumnos para mostrar")
    if option == 3: #------------------------------> Ver promedios del Parcial 1 de todos los alumnos
         count = 0
        for alumno in alumnos:
            print(f"{count}.- = {sum}") #todo: Calcular promedio
    if option == 4: #------------------------------> Ver promedio grupal del Parcial 1.
        print(f"Promedio grupal del 1er parcial es de {sum()}") #todo: Calcular promedios
            elif not alumnos:
                print("Aún no hay alumnos para mostrar")
    if option == 5: #------------------------------> Agregar alumno y sus calificaciones
        nombre = input("Ingrese nombre del alumno: ")
        Contabilidad =
        Algebra =
        Estructura_de_Datos =
        Derecho =
        Electronica =
