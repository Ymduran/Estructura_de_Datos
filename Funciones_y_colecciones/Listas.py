print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 12 noviembre del 24                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * listas                                                           * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

'''
Colecciones: 
Ordenadas y mutables
mutables: pueden cambiar/modificar/crecer/reducir
Una cola "FIFO" (en inglés, First Into, First Output); ésta se realiza en orden
Una pila se realiza en orden de el último en entrar es el primero en salir, Queue o "LIFO" (en inglés, Last Input First Output

Para crear una lista:

nombre_de_la_lista = []


'''

'''
#Para llenar la lista
alumnos = []
alumnos.append("Héctor", "Addi", "Jesús", "Alberto", "Juan")

#Para insertar
alumnos.insert(1,"Tania")

#Para imprimirlos en un for
for alumno in alumnos:
    print(f"{alumno}", end = " ")

#Eliminación. A continuación tres formas de eliminar un elemento
alumnos.remove("Héctor") #Eliminación por referencia
alumnos.pop(2) #eliminación por índice
del alumnos[2] #eliminación por índice


for alumno in alumnos:
    print(f"{alumno}", end = " ")


'''

alumnos = ["Rosalinda", "Juan", "Lourdes", "Tania", "Bryan", "Rebeca", "Jennifer", "Héctor", "Jesús", "Addi"]

print(" ")
len(alumnos) #ver lista por añadidos
print("función len ")
print(alumnos)

print(" ")
alumnos.sort() #ver lista por A-Z
print("función sort")
print(alumnos)

print(" ")
alumnos.sort(reverse=True) #Ver lista por Z-A
print("función sort reverse ")
print(alumnos)

print(alumnos[-1]) #Mustra el último de la lista, es decir el primero de atras hacia delante




