print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 09 de diciembre del 2025                                  * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Docstring                                                       * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")


def menu():
    """
    Muestra el menú
    :return: {Regresa un entero, que es una de las opciones del menú}
    """
    print("[1].- Convertir a entero")
    print("[2].- Convertir a flotante")
    print("[0].- Salir")
    opcion = int(input("Ingrese una opción: "))
    return opcion



def cadena_a_entero(cadena: str) -> int | None:
    """
        Función que convierte la cadena a un entero
        :param cadena: Es la cadena a convertir a número entero
        :return: Retorna la cadena convertida a entero o en caso de que no reciba un número devuelve None
    """
    numero_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-")
    if revisar_cadena.isnumeric() and numero_guiones in (0, 1):
        return int(cadena)
    else:
        return None


def cadena_a_flotante(cadena: str) -> float | None:
    """
        Función que convierte la cadena a un flotante
        :param cadena: Es la cadena a convertir a número flotante
        :return: Retorna la cadena convertida a flotante o en caso de que no reciba un número devuelve None
    """
    numero_puntos = cadena.count(".")
    revisar_cadena = cadena.replace(".", "").lstrip("-")
    if revisar_cadena.isnumeric() and numero_puntos in (0, 1):
        return float(cadena)
    else:
        return None


    return 0

# Código a nivel de módulo
print()

opcion = menu()
while opcion != 0:
    if opcion == 1:
        num_cadena = input("Ingresa número a convertir: ")
        numero = cadena_a_entero(num_cadena)
    elif opcion == 2:
        num_cadena = input("Ingresa el número a convertir: ")
        numero = cadena_a_flotante(num_cadena)
    else:
        opcion = int(input("Opción no válida. Intente de nuevo: "))
        continue

    while numero is None:
        num_cadena = input("Opción no válida. Intente nuevamente: ")
        numero = cadena_a_entero(num_cadena) if int(opcion) == 1 else cadena_a_flotante(num_cadena)

    print(f"El número {numero} es de tipo {type(numero)}")
    opcion = menu()

