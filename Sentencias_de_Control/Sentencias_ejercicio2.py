print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 24  octubre del 2024                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Sentencia ejercicio 2                                           * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print("  ")

'''
Este programa determinará la estación del año de acuerdo al número de mes ingresado por el usuario. Para ello:
a) Solicite al usuario un número que representa al mes.
b) Utilice la lógica adecuada para determinar la estación del año de acuerdo con:
    3, 4 y 5: Primavera.
    6, 7 y 8: Verano.
    9,10 y 11: Otoño.
    12, 1 y 2: Invierno.
    Otro caso: Mensaje de mes incorrecto.
c) Muestre la estación correspondiente en consola.
'''

numero_de_mes=int(input("ingrese el número que respresente al mes: ")) #Se lee por tecladd el número de mes
if numero_de_mes>=3 and numero_de_mes>=5: #1 condición: sí los meses se encuentran entre el tercer y quinto mes: true/false
    print("La estación es: Primavera")
elif numero_de_mes>=6 and numero_de_mes<=8: #2 condición: sí los meses se encuentran entre el sexto y octavo mes: true/false
    print("La estación es: Verano")
elif numero_de_mes>=9 and numero_de_mes<=11: #3 condición: sí los meses se encuentran entre el noveno y décimo primer mes: true/false
    print("La estación es: Otoño")
elif numero_de_mes==12 or numero_de_mes==1 or numero_de_mes==2: #4 condición: si es diciembre, o enero o febrero
    print("La estación es: Invierno")
else: #sí no se cumple ninguna de las condiciones anteriores
    print("Mes incorrecto")