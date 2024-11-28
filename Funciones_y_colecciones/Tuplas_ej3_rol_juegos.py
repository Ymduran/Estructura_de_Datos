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
Utiliza un pivote que usa para sobre ese combinar el resto de equipos
'''


print("** Rol de juegos **")




equipos = [] #Se crea la lista de equipos
numero_equipos = int(input("Ingrese número (PAR) de equipos que jugarán:  "))#Debe ser par porque los emparejamientos deben ser par



for i in range(0,numero_equipos):
    equipo = input(f"Ingrese el nombre del equipo {i}: ") #Se lee por teclado el nombre del equipo
    equipos.append(equipo) #Se añade el equipo a la lista de equipos



numero_partidos = int(input("Ingrese cantidad de veces que se jugará: "))
rol = [] #Se crea la lista de rol
pivote = equipos[0] #Se crea el pivote que es el primero
ultimo_equipo = numero_equipos-1



#Este for solo se encarga de hacer las asignaciones, posteriormente se hará el reordenamiento de la lista
for partido in range(numero_partidos):
    print(f"** Ronda {partido} **")
    ultimo_equipo = numero_equipos-1
    for j in range(0, len(equipos)//2): #División entera, la palabra "len" accede al número de elementos que hay en la lista, se divide entre dos porque solo hará la mitad de los equipos para asignarlos con la otra mitad
        if j == 0: #Cuando se esté en el caso 1, se asigna ese par. el primero con el último y se guarda como tupla en la lista de rol
            rol.append((pivote, equipos[ultimo_equipo]))
        else: #Para todos los demás casos solo se van guardando tal cual los pares en las tuplas
            rol.append((equipos[j], equipos[ultimo_equipo - j])) 




    # Imprimir los vs en pantalla
    for versus in rol:
        print(f"{versus[0]} vs {versus[1]}") #Imprime la lista
#Lista[-1] refiere al último elemento de la lista
    equipos = [equipos[0]] +[equipos[-1]] + equipos[1:-1]   #el primero siempre se mantiene pues es el pivote, el siguiente es el último y el resto sigue igual
    rol = [] #Reincia la lista cada vez solo para imprimirlos




