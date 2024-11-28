print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha:   26 noviembre del 24                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Conjuntos operaciones                                            * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

'''
Los conjuntos son: 
- Desordenados. No tiene índice
- Inmutables. No son cambiables
- Su declaración es con llaves (también para diccionarios)
- Para declarar un conjunto vacío nombre_conjunto ser{}
'''
conjuntoA = {11,7,10,9,5,1,15,7}
conjuntoB = {55,70,11,77,66,9,5}
print(f"Conjunto A: {conjuntoA}")
print(f"Conjunto B: {conjuntoB}")

print(f"Unión = {conjuntoA|conjuntoB}")
print(f"Intersección = {conjuntoA&conjuntoB}")
print(f"Diferencia = {conjuntoA-conjuntoB}")

lista_animales = ["pato", "perro", "pez", "pato", "zapato", "bambi"]
conjunto_animales = set(lista_animales) #De lista a conjunto
print(f"Conjunto animales: {conjunto_animales}")
lista_modificada = list(conjunto_animales) #Palabra reservada para convertir a lista "list"
print(f"Lista animales modificada: {lista_modificada}")

#Ganador = random.choice(lista) Para seleccionar de una lista