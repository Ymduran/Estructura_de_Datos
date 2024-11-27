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


def menu(): # Función menú: muestra las opciones disponibles al usuario. No recibe ni regresa valores.
    print(" ***  Calificaciones del Parcial 1  *** ")
    print("1) Ver calificaciones de todos los alumnos. ")
    print("2) Ver calificaciones detalladas de un alumno. ")
    print("3) Ver promedios del Parcial 1 de todos los alumnos. ")
    print("4) Ver promedio grupal del Parcial 1. ")
    print("5) Agregar alumno y sus calificaciones. ")
    print("6) Eliminar alumno y sus calificaciones. ")
    print("0) Salir. ")


# Operaciones
def funcion_operaciones_segun_menu(option): # Función principal para realizar las operaciones según la opción seleccionada en el menú
    count = 0  # Contador para mostrar índices de los alumnos
    if option == 1:  #1. ----------------------------------> Ver calificaciones de todos los alumnos
        if not alumnos:  # Si la lista de alumnos está vacía
            print("Aún no hay alumnos para mostrar")
            return #Termina la función
        for alumno in alumnos:  # Itera sobre la lista de alumnos
            print(f"{count}.- {alumno}")
            count += 1
        count = 0  # Reinicia el contador de nuevo en cero
    elif option == 2:  #  ----------------------------------> Ver calificaciones detalladas de un alumno
        if not alumnos:  # Si la lista de alumnos está vacía
            print("Aún no hay alumnos para mostrar")
            return
        indice = int(input("Ingrese número de índice del alumno a mostrar: "))
        print(alumnos[indice])  # Muestra la información del alumno con el índice
    elif option == 3:  #  ---------------------------------->Ver promedios del Parcial 1 de todos los alumnos
        if not alumnos:  # Verifica que existan alumnos para calcular promedios.
            print("Aún no hay alumnos para mostrar")
            return
        for alumno in alumnos:  # Itera sobre cada alumno en la lista de alumnos
            promedio = sum(alumno[1]) / len(alumno[1])  # Calcula el promedio de las calificaciones, "sum" hace la sumatoria mientras que len tiene la cantidad de calificaciones, tiene el corchete 1 porque allí es donjde se encuentran las calificaciones mientras que en el ;indice 0 tiene el nombre
            print(f"{count}.- {alumno[0]}: Promedio = {promedio:.2f}")  # Muestra el promedio
            count += 1
    elif option == 4:  #  ---------------------------------->Ver promedio grupal del Parcial 1
        if not alumnos:  # Verifica que existan alumnos para calcular el promedio grupal.
            print("Aún no hay alumnos para mostrar")
            return
        total_calificaciones = 0  # Acumular todas las calificaciones
        cantidad_calificaciones = 0  # Contador del total de calificaciones

        for alumno in alumnos:  # Itera sobre la lista de alumnos
            calificaciones = alumno[1]  # Se le asigna las calificaciones del alumno
            total_calificaciones += sum(calificaciones)  # Suma de las calificaciones
            cantidad_calificaciones += len(calificaciones)  # Contar las calificaciones

        promedio_grupal = total_calificaciones / cantidad_calificaciones  # Calcular el promedio grupal
        print(f"Promedio grupal del 1er parcial es de: {promedio_grupal:.2f}")  # Imprimiendo el resultado
    elif option == 5:  #  ----------------------------------> Agregar alumno y sus calificaciones
        nombre = input("Ingrese nombre del alumno: ")  # Solicita el nombre del alumno
        calificaciones = []  # Lista para guardar las calificaciones

        # Leer las 5 calificaciones
        calificaciones.append(float(input("Ingrese calificación de Contabilidad: ")))
        calificaciones.append(float(input("Ingrese calificación de Álgebra: ")))
        calificaciones.append(float(input("Ingrese calificación de Estructura de Datos: ")))
        calificaciones.append(float(input("Ingrese calificación de Derecho y Legislación: ")))
        calificaciones.append(float(input("Ingrese calificación de Electrónica II: ")))

        agrupar = [nombre, calificaciones]  # Agrupa el nombre y las calificaciones en una lista
        alumnos.append(agrupar)  # Añade la lista a la lista principal de alumnos
        print(f"Se agregó a {nombre} exitosamente")
    elif option == 6:  # ---------------------------------->  Eliminar alumno y sus calificaciones
        indice_eliminar = int(input("Ingrese número de índice del alumno que desea eliminar: "))  # Solicita índice para hacer la eliminación por índice
        alumnos.pop(indice_eliminar)  # Elimina al alumno indicado
        print("Se eliminó con éxito")
    elif option == 0: #  ---------------------------------->  Salir del programa
        print("Saliendo...")  # Imprime este letrero justo antes de salir
    else:  #   ---------------------------------->Opción no válida
        print("Opción no válida, intentélo de nuevo...")


# Código nivel de módulo
flag = 0  # Bandera para romper el ciclo while
alumnos = []  # Lista principal para almacenar los datos de los alumnos
agrupar = []  # Lista temporal para agrupar los datos antes de añadirlos a la lista principal

while flag == 0:
    menu()  # Llama a la función menú para mostrar las opciones por lo que no se manda nada
    option = int(input("Ingresa una opción: "))
    funcion_operaciones_segun_menu(option)  # Ejecuta la función correspondiente según la opción ingresada y se le manda la opcxión
    print(" ")
    if option == 0:  # Si la opción es 0, se termina el programa
        flag = 1  # Cambia el valor de la bandera para salir del while



