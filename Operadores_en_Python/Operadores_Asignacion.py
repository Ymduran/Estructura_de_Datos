print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 14 octubre del 2024                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Operadores de asignación                                         * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")
# ------------------------------------------------------
#ASIGNACIÓN MÚLTIPLE
variable1 , variable2 = 5 , 10  #se pueden asignar dos o más valores al mismo tiempo
variable3 , variable4 = 9.14 , "chuy" #se pueden asignar dos o más valores de diferente tipo de dato

print(f" variable 1: {variable1}")
print(f" variable 2: {variable2}")
print(f" variable 3: {variable3}")
print(f" variable 4: {variable4}")

variable5 , variable6 = variable1 + variable2 , variable1 + variable2 #se pueden realizar la asignación del resultado de las sumas de dos o más respectivamente

print(f" variable 5: {variable5}")
print(f" variable 6: {variable6}")
 #------------------------------------------------------
#ASIGNACIÓN EN CADENA

variable7 = variable8 = variable9 = 10  #Se puede igualar a otra variable en cadena

print(f" variable 7: {variable7}") #imprime 10
print(f" variable 8: {variable8}") #imprime 10
print(f" variable 9: {variable9}") #imprime 10

variable10 , variable11 = "Alberto" , "Beto"

print(f" variable 10: {variable10}")
print(f" variable 11: {variable11}")
print("intercambiando...")
variable11 , variable10 = variable10 , variable11 #Para hacer intercambio de variables sin tener que guardarlo en una existencia
print(f" variable 10: {variable10}")
print(f" variable 11: {variable11}")

nombre , apellido = input("ingresa nombre: ") , input("ingresa tu apellido: ") #Para leer datos por teclado al mismo tiempo
print(nombre ,  apellido)
