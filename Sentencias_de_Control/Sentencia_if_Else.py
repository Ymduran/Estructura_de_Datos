print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 17 octubre del 2024                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Sentecncia if  y sentencia else                                 * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

'''
if condición1:
    #Código a ejecutar sí
else: 
    #Código si la condición1 no es verdadera
    
'''
#Están agrupados por el tabulador, cuando se ocupa la siguiente línea sin tabular, entonces termina el código de la sentencia anterior
'''
Para decidir si se cumple una condición o no, sí no, ejecutar algo en particular
'''

#PROGRAMA PARA DETERMINAR SÍ UN NÚMERO ES PAR O IMPAR
numero = int(input("ingrese número: ")) #Se lee el número por teclado
if (numero % 2) == 0: # "%" = módulo, es decir el sobrante, la condición establece que si el sobrante de la división entre 2 es 0 entonces es par
    #Un número par es todo aquel número múltiplo de 2
    print(f" el número {numero} es par")
else: #De no cumplirse la sentencia anterior, entonces se jecuta el siguiente código
    print(f" el número {numero} es impar")
#En este ejercicio tiene que mostrar un si cuando ambas respuestas sea verdadera.

