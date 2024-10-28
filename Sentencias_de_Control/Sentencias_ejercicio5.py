print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 24  octubre del 2024                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Sentencia ejercicio 5                                           * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print("  ")

'''
Este programa determinará el promedio de una materia e indicará si el alumno aprobó o no la materia.
Para ello:
a) Solicite al usuario sus tres calificaciones parciales y la calificación del ordinario.
b) Calcule el promedio y determine si aprobó (calificación mínima de 6.0).
d) Muestre el promedio (utilizando un decimal) y el mensaje: "¡Felicidades! Aprobaste.", o el mensaje: "Lo siento, no aprobaste.", según sea el caso.

'''


parcial1,parcial2,parcial3, ordinario = float(input("Ingrese calificación del primer parcial: ")), float(input("ingrese la calificación del segundo parcial: ")), float(input("ingrese la calificación del tercer parcial: ")), float(input("ingrese la calificación del ordinario: "))

promedio = (((parcial1 + parcial2 + parcial3)/3)/2) + (ordinario/2)

if promedio >= 6:
    print(f"tu promedio es de: {promedio:.1f}, ¡Felicidades! Aprobaste. ")
else:
    print(f"tu promedio es de: {promedio:.1f}, Lo siento, no aprobaste.")


print("Convirtiendo primero el promedio a valor booleano")

promedioboole = (promedio >= 6)

if promedioboole == True:
    print(f"tu promedio es de: {promedio:.1f}, ¡Felicidades! Aprobaste. ")
else:
    print(f"tu promedio es de: {promedio:.1f}, Lo siento, no aprobaste.")
