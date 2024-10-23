print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 10 octubre del 2024                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     *")
print(" * Entrada por consola ejercicio                                     * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")
'''
Instrucciones:

    Revisa el código fuente proporcionado en la lección y reprodúcelo en PyCharm.
    Avanza en la lección y verifica el comportamiento del código agregado en cada caso.
    Realiza los comentarios que crea pertinentes a su propio código, de acuerdo a lo observado.

Entrada_conversiones_ejercicio.py

Escribe un programa de nombre Entrada_conversiones_ejercicio.py que realice lo siguiente:

a) Pida los datos de los profesores utilizando nombres de variables adecuadas, la función input y el casting:

        Nombre (cadena).
        No. de cubículo (int).
        Horas de que imparte clase a la semana (float con 3 decimales).
        ¿Tiene más de 5 años en la unsij? (booleno).

b) Muestre los datos en consola de forma adecuada.

Nota: Asuma que el usuario siempre va a ingresar números cuando se requiera. 

'''
# Recordando la lección anterior: variable = tipo_de_dato(input("letrero a imprimir"))
nombre_profesor, no_cubo, horas_de_clase_semanal, años = input("ingrese su nombre: "), int(input("ingrese su número de cubículo: ")), float(input("ingrese el número de horas de clases que imparte a la semana: ")), input("Lleva más de cinco años en la unsij? si/no:  ")
                                                        #El nombre ya se lee como una cadena, no necesita convertirse                                                                                                  #El tipo de dato bool no se puede hacer directamente
años = años.lower() == "si" #Se convierte a minúsculas y se compara con la cadena si, cualquier respuesta diferente a esta imprimirá un false
print(f"su nombre es: {nombre_profesor}, su número de cubículo es: {no_cubo}, usted imparte  {horas_de_clase_semanal:.3f} horas a la semana. Tiene más de cinco años en la UNSIJ?: {años} ")
                                                                                            #variable:.3f imprime los tres decimales del número
