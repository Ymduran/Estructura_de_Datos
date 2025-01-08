print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 08 de diciembre del 2025                                  * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Especificar datos en funciones                                   * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")


def menu():
    print("[1].- Convertir a entero")
    print("[2].- Convertir a flotante")
    print("[0].- Salir")
    opcion = input("Ingrese una opción: ")
    return opcion


def cadena_a_entero(cadena: str) -> int | None:
    numero_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-")
    if revisar_cadena.isnumeric() and numero_guiones in (0, 1):
        return int(cadena)
    else:
        return None


def cadena_a_flotante(cadena: str) -> float | None:
    numero_puntos = cadena.count(".")
    revisar_cadena = cadena.replace(".", "").lstrip("-")
    if revisar_cadena.isnumeric() and numero_puntos in (0, 1):
        return float(cadena)
    else:
        return None


# Código a nivel de módulo
opcion = menu()
while int(opcion) != 0:
    if int(opcion) == 1:
        num_cadena = input("Ingresa número a convertir: ")
        numero = cadena_a_entero(num_cadena)
    elif int(opcion) == 2:
        num_cadena = input("Ingresa el número a convertir: ")
        numero = cadena_a_flotante(num_cadena)
    else:
        print("Opción no válida.")
        opcion = menu()
        continue

    while numero is None:
        num_cadena = input("Opción no válida. Intente nuevamente: ")
        numero = cadena_a_entero(num_cadena) if int(opcion) == 1 else cadena_a_flotante(num_cadena)

    print(f"El número {numero} es de tipo {type(numero)}")
    opcion = menu()

