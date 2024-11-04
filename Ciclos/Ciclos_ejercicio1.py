
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 28  octubre del 2024                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * ciclo while (mientras) ejercicio  1                               * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")


'''
while condición:
--> #Código a hacer mientras
#tabulacción 

'''

#Programa que calcula la suma acumulativa:

numero = int(input("ingresa el número final: "))

contador = 0
suma=0

while contador<=numero:
    suma+=contador #va sumando al contador
    contador+=1 #incrementar contador en uno

print(f"La suma de 0 hasta el número {numero} es {suma}")


