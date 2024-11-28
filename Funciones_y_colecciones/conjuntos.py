print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 25 noviembre del 24                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Conjuntos                                                        * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

'''
Los conjuntos son: 
- Desordenados. No tiene índice
- Inmutables. No son cambiables
- Su declaración es con llaves (también para diccionarios)
- Para declarar un conjunto vacío nombre_conjunto set()
'''

print(" ** Ejemplos de uso de los conjuntos **")
conjunto_nombres = set() #Conjunto vacío
print(f"conjunto_vacío : {conjunto_nombres}")
# Se añaden valores al conjunto con .add
conjunto_nombres.update(["Rebeca", "Juan", "Bryan", "Yamilet", "Galilea", "Rosalinda", "Jennifer", "Tania", "Héctor", "Patricia", "Addi", "Alberto"]) #.update para añadir varios elementos, se hace con corchetes y paréntesis
print(f"Conjunto 303: {conjunto_nombres}")
print(" ")
print(" ** Ejemplos de uso de los conjuntos **")
conjunto_nombres.add("Yamilet") #.add para añadir un elemento
#El conjunto no acepta duplicados
#Ejemplo para eliminar
print(f"Conjunto 303 añadiento a Yamilet: {conjunto_nombres}")
print(" ")
conjunto_nombres.remove("Juan") #para eliminar se hace sólo por referencia porque no tiene un orden

#Para mostrar todos los elementos en el conjunto for
for nombre in conjunto_nombres:
    print(nombre, end = ",")

 #Para verificar si un elemento pertenece a un conjunto
print(f"\nEl elemento 'Rebeca' pertenece al conjunto? {'Rebeca' in conjunto_nombres}")
