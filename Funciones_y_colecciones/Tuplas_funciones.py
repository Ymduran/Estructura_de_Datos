print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 19 noviembre del 24                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Tuplas_ejercicio                                                * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

'''
'''
print("** Calificaciones del parcial **")

def calificacion (calificaciones):
    promedio_parcial = sum(calificaciones[0:2])/3
    promedio_final = (promedio_parcial + calificaciones[3])/2
    promedios = (promedio_parcial, promedio_final)
    return promedios


primer_parcial, segundo_parcial, tercer_parcial = float(input("Calificación 1er Parcial: ")),float(input("Calificación 2do Parcial: ")),float(input("Calificación 3er Parcial: "))
ordinario = float(input("Ingrese calificación de Ordinario: "))
calificaciones = (primer_parcial, segundo_parcial, tercer_parcial, ordinario)
tupla_receptora = calificacion(calificaciones)
print(f"Promedio Parcial: {tupla_receptora[0]}, Final: {tupla_receptora[1]}")



