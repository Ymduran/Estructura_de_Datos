print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 28  octubre del 2024                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Sentencia ejercicio 6                                           * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print("  ")

'''
Escribe un programa de nombre Sentencias_ejercicio6.py que realice lo siguiente:
Este programa mostrará los detalles del tour turístico Ecoturixtlán de acuerdo a las siguientes tarifas:
    Precio de un adulto: $ 200.00
    Precio de un niño: $ 100.00
Además, si la visita son los lunes, martes y jueves, se tiene un descuento del 10 %.
Para ello:
a) Solicite al usuario el nombre de la persona a cargo.
b) Defina con valores constantes el precio del boleto del adulto y del niño.
c) Solicite el número de adultos y de niños.
d) Pregunte el día de la semana.
e) Calcule el costo total.
f) Muestre los detalles del cliente y el día, así como el costo total.
'''

print("** tour turístico Ecoturixtlán **")

nombre_persona_a_cargo = input("ingrese nombre de la persona a cargo: ")#Se leen por teclado el nombre de la persona a cargo
#Se asignan los valores fijos y se leen otros datos por teclado, los cuales se convierten al tipo de dato correspondiente
precio_boleto_adulto, precio_boleto_niño, numero_adultos, numero_niños, dia_semana = 200, 100, int(input("ingrese cantidad de adultos: ")), int(input("ingrese cantidad de niños: ")), input("ingrese día de la semana: ")


dia_semana = dia_semana.lower()#Se convierte a minúsculas para posteriormente comparar con otras cadenas

print(f"día de la semana {dia_semana}")
print(f"persona encargada: {nombre_persona_a_cargo}")
print(f"Ingresaron {numero_adultos} adultos y {numero_niños} niños")
if dia_semana=="lunes" or dia_semana== "martes" or dia_semana== "jueves" : #Sí el día de la semana es igual a estas otras cadenas entonces se ejecuta la siguinte línea de código
    print(f"El costo total del tour es de: ${ ((numero_adultos * precio_boleto_adulto) + (numero_niños * precio_boleto_niño))  -  ((numero_adultos*precio_boleto_adulto)+(numero_niños*precio_boleto_niño))*0.1}, con descuento")
                                                #costo de todos los adultos            +  costo de todos los niños             - el 10%
else: #sí la condición anterior no se cumple, entonces no aplica el descuento
    print(f"El costo total del tour es de: ${(numero_adultos * precio_boleto_adulto) + (numero_niños * precio_boleto_niño)}, sin descuento")
                                                # costo de todos los adultos            +  costo de todos los niños
