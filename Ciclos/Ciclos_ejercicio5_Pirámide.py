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
count = 0  #El contador inicia en cero para que realice llas cuentas de las filas posteriomente
numero_filas = int(input("ingrese número de filas para la pirámide: "))

for i in range (1, numero_filas+1): #Imprime en el rango de 1 al total del número de filaS
    print(" ") #Imprime salto de línea
    count += 1 #Suma al contador
    for j in range (1,count+1): #Imprime el mismo número del contador que de asteriscos cada vez para hacer una pirámide, es decir, cuando el conatador vaya en el segundo renglón, entonces imprimirá dos asteriscos
        print ("*", end=" ") # Imprime el asterisco, y para reemplazar el salto de línea, end = " " para reemplazar el salto de línea por un espacio
print("Caso 1 ")
#Caso 1; Otro método
print(" ")
print(" ")
for i in range (1, numero_filas+1):
    asteriscos = "*" * i #Este método consite en un sólo for y solo multiplica el número de fila por los asteriscos, en python un caracter se puede multiplicar
    print(asteriscos)

print(" ")
#Segundo caso
print("Caso 2 ")
for i in range (1, numero_filas+1):
    print(" ")
    count -= 1 #Al contador le restará uno pues se quedó con la cuenta del caso anterior, si imprimió seis filas entonces comenzará imprimiendo seis astericos, decrementando cada iteración para hacer una pirámide inversa
    for j in range (1,count+2):
        print ("*", end=" ")

print(" ")
print(" ")

#Tercer caso
print("Caso 3 ")
count = 0

contador_asterisco= numero_filas #Aquí se inicializa el contador_asteriscos igual al número de filas que ingresó el ususario

for i in range(1, numero_filas+1):
    espacio = " " * count #multiplica el espacio por el número de renglones, es decir, si va en el renglón dos, imprimirá dos espacios, esto con el fin de alinear los asteriscos a la derecha
    asteriscos= "*" * contador_asterisco #Multiplica los asteriscos por el contador
    print(espacio,asteriscos) #Imprime los espacios y despúés los asteriscos
    contador_asterisco -= 1 #La canidad de astericos decrementa cada vez
    count+=1

print(" ")
print(" ")

print("Caso 4 ")
#Cuarto caso
contador_asterisco= numero_filas
print()
for i in range(1,contador_asterisco+1): #En el rango de 1 hasta el número de filas, que anteriormente se igualó a contador asteriscos
    espacio = " " * numero_filas
    asteriscos = "*" * i
    print(f"{espacio} {asteriscos}",end=" ")
    i -= 1 #Para imprimir la cantidad de astericos en decremento
    asteriscos = "*" * i
    print(f"{asteriscos}")
    i +=1 #Para imprimir la cantidad de astericos en incremento
    numero_filas -= 1 #Se resta uno en cada interación para multiplicar por los espacios y cada vbez haya menos espacio en la alineación izquierda
    print()

    



