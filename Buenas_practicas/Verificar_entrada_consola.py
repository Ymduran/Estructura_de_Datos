
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 07 de diciembre del 2025                                  * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Verificar entrada consola                                        * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

'''
prueba_numero = int(input("Ingresa un número: "))
print()
cadena = input("Ingresa una cadena: ").strip()
print(f"{cadena.isnumeric()}") #Si es un número
print(f"{cadena.isalpha()}") #Si es alpha
print(f"{cadena.isalnum()}") #Si es alphanumeric
'''


'''
prueba_numero = (input("Ingresa un número: "))
while not prueba_numero.isnumeric():
    print("Opción no válida")
    prueba_numero = input("Intenta de nuevo: ")
print()
prueba_numero = int(prueba_numero)
print(f"El número {prueba_numero} es de tipo {type(prueba_numero)}")
'''

def cadena_a_entero(cadena):
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-")
    if revisar_cadena.isnumeric() and no_guiones in (0,1):
        return int(cadena)
    else:
        return None

def cadena_a_flotante(cadena):
    no_puntos = cadena.count(".")
    revisar_cadena = cadena.lstrip("-").replace(".","")
    if revisar_cadena.isnumeric() and no_puntos in (0,1):
        return int(cadena)
    else:
        return None

num_cadena = input("Ingresa Z: ")#Z es numero entero
numero = cadena_a_entero(num_cadena)
while numero is None:
    print("Opción no válida")
    num_cadena = input("Intenta de nuevo: ")
    numero = cadena_a_entero(num_cadena)
print(f"El numero {numero} es tipo {type(numero)}")

num_cadena = input("Ingresa Z: ")#Z es numero entero
numero = cadena_a_entero(num_cadena)
while numero is None:
    print("Opción no válida")
    num_cadena = input("Intenta de nuevo: ")
    numero = cadena_a_entero(num_cadena)
print(f"El numero {numero} es tipo {type(numero)}")

