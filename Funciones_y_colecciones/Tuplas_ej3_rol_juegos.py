print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 21 noviembre del 24                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Tuplas_ejercicio2                                                * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

'''
Este programa crea un rol de juegos, según el usuario lo indique el número de veces que se harán las combinaciones
Utiliza un pivoque que usa para sobre ese combinar el resto de equipos
'''


print("** Rol de juegos **")




equipos = [] #Se crea la lista de equipos
numero_equipos = int(input("Ingrese número (PAR) de equipos que jugarán:  "))


for i in range(0,numero_equipos):
    equipo = input(f"Ingrese el nombre del equipo {i}: ") #Se lee por teclado el nombre del equipo
    equipos.append(equipo) #Se añade el equipo a la lista de equipos







numero_partidos = int(input("Ingrese cantidad de veces que se jugará: "))
rol = [] #Se crea la lista de rol
pivote = equipos[0] #Se crea el pivote que es el primero
ultimo_equipo = numero_equipos-1


count_while = 0
i=1



while i <= numero_partidos:
    rol.append((pivote, equipos[ultimo_equipo]))
    while count_while <= numero_equipos/2:
        ultimo_equipo -= 1
        rol.append((equipos[count_while+1], equipos[ultimo_equipo]))
        if ultimo_equipo == 1:
            ultimo_equipo = numero_partidos
        count_while += 1
    i += 1





    '''
    rol.append((pivote, equipos[i]))  # En la lista de rol se guarda la tupla del rol del pibote vs algún otro equipo
    rol.append((equipos[i], equipos[j])) #En la lista de rol se guarda la tupla del rol "equipox" vs "equipoy"
'''


'''
for i in range(1, len(equipos)): #En el rango desde 1 hasta el número de equipos, la palabra reservada "len"es para obterner la cantidad de elementos en la lista, en este caso cuántos equipos hay
    rol.append((pivote, equipos[i])) #En la lista de rol se guarda la tupla del rol del pibote vs algún otro equipo
    for j in range(i + 1, len(equipos)): # En el rango desde la fila anterior con el resto de los equipos, esta parte es para girar los equipos entre sí y que todos jueguen con todos
        for k in range(0,numero_partidos): # Repertirá hasta el número de partidad que el usuario haya indicado
            rol.append((equipos[i], equipos[j])) #En la lista de rol se guarda la tupla del rol "equipox" vs "equipoy"
'''
#Esta partew imprime los vs
count = 0
contador_ronda = 1
for versus in rol:
    '''
    if count == ((numero_partidos/2)) or count == 0:
        print(f"** Ronda número {contador_ronda} **")
        count = 0
        contador_ronda += 1
        '''
    print(f"{versus[0]} vs {versus[1]}") #Imprime cada elemento 0 y 1 de la tupla que está en la lista de rol
    count += 1






