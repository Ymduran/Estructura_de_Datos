from itertools import count

print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 07 de noviembre del 2024                                   * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" *  Pirámide                                                         * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")


'''

'''
count = 0
numero_filas = 5
for i in range (1, numero_filas+1):
    print(" ")
    count += 1
    for j in range (1,count+1):
        print ("*", end=" ")

#Caso 1; Otro método
print(" ")
print(" ")
for i in range (1, numero_filas+1):
    asteriscos = "*" * i
    print(asteriscos)

print(" ")
#Segundo caso
for i in range (1, numero_filas+1):
    print(" ")
    count -= 1
    for j in range (1,count+2):
        print ("*", end=" ")

print(" ")
print(" ")

#Tercer caso
count = 0

contador_asterisco= numero_filas

for i in range(1, numero_filas+1):
    espacio = " " * count
    asteriscos= "*" * contador_asterisco
    print(espacio,asteriscos)
    contador_asterisco -= 1
    count+=1



