
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 28  octubre del 2024                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * ciclo while (mientras) ejercicio  1 suma acumulativa              * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
'''
while condición:
--> #Código a hacer mientras
    #tabulacción 

'''

#Programa que calcula la suma acumulativa:

numero = int(input("ingresa el número final: "))

contador = 0 #El contador se incializa en cero
suma=0 #Suma se incia en cero

while contador<=numero: #hacer mientras el contador sea menor o igual al número
    suma+=contador #va sumando al contador, que el contador es cada número hasta el número final que el usuario haya ingresado
    contador+=1 #incrementar contador en uno

print(f"La suma de 0 hasta el número {numero} es {suma}")


