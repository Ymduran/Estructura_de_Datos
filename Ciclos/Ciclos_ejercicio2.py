
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 17 octubre del 2024                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * ciclos ejercicio 2                                               * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

'''
PROGRAMA QUE CALCULA LA SUMA ACUMULATIVA ENTRE DOS NÚMEROS
'''

numero_inicial, numero_final = int(input("ingrese número inicial: ")), int(input("ingrese número final: "))

suma=0 #se inicializa la suma en cero
#como contador se puede utilizar el número incial puesto que es ahí donde inicia la suma y solo basta con incrementar
while numero_inicial <= numero_final: #meintras en número inicial sea menor o llegue hasta el número final sumando de uno en uno
    suma+=numero_inicial #Se acumula en suma los valores del contador, que en este caso es "numero_inicial"
    numero_inicial+=1  #se incremente en 1

print(f"La suma acumulativa desde el número inicial hasta {numero_final} es {suma}")