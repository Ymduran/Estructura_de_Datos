
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 08 de diciembre del 2025                                  * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Marcadores de posición                                           * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")
'''
Conversor a números enteros y fotantes con validación
#pass instrucción para "no hacer nada" como algo pendiente
También se pueden usar los tres puntos "..." 
  print("[1].- Convertir a entero")
    print("[2].- Convertir a flotante")
    print("[0].- Salir")
    
#TO DO significa "por hacer"
# FIXME significa "repárame"
    
'''
#TODO implementar el menú
def menu():
    pass

def cadena_a_entero(cadena):
    pass

def cadena_a_flotante(cadena):
    raise NotImplementedError("Implementar función: ") #raise significa "subir"


#Código nivel de módulo
opcion = menu()
while opcion != 0:
    if opcion == 1:
        num_cadena = input("Ingresa número a convertir: ")
        num = cadena_a_entero(num_cadena)
    elif opcion == 2:
        num_cadena = input("Ingresa número a convertir: ")
        num = cadena_a_flotante(num_cadena)
    elif opcion == 0:
        print("Saliendo...")
    else:
        print("Opción no válida")






