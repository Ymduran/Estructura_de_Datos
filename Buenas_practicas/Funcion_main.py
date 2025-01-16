print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha:  13 de enero del 2025                                 * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Funcion main con validación de datos                            * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

# Funciones de validación del Código 1
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

# Menú y cálculo
def menu() -> None:
    """
    Función que muestra el menú
    :return: No retorna nada
    """
    print("Menú ")
    print("1.- Sumar ")
    print("2.- Restar ")
    print("3.- Salir ")

def calcular(option: int) -> float | None:
    """
    Función que hace la suma o resta de dos números, según lo desee el usuario
    :param option: Recibe un entero
    :return: Retorna el resultado en tipo flotante o None si los números no son válidos
    """
    first_number = None
    second_number = None

    # Validación del primer número
    while first_number is None:
        num_cadena = input("Ingresa el primer número: ")
        first_number = cadena_a_flotante(num_cadena)
        if first_number is None:
            print("Entrada no válida. Intenta de nuevo.")

    # Validación del segundo número
    while second_number is None:
        num_cadena = input("Ingresa el segundo número: ")
        second_number = cadena_a_flotante(num_cadena)
        if second_number is None:
            print("Entrada no válida. Intenta de nuevo.")

    # Realiza la operación
    if option == 1:
        return first_number + second_number
    elif option == 2:
        return first_number - second_number
    else:
        return None

if __name__ == '__main__':
    def main() -> None:
        flag = False
        while not flag:
            menu()
            opcion = None

            # Validación de opción del menú
            while opcion is None:
                opcion_cadena = input("Ingrese una opción: ")
                opcion = cadena_a_entero(opcion_cadena)
                if opcion not in (1, 2, 3):
                    print("Opción no válida. Intente de nuevo.")
                    opcion = None

            if opcion in (1, 2):
                resultado = calcular(opcion)
                print(f"El resultado de la operación es: {resultado}")
            elif opcion == 3:
                print("Saliendo...")
                flag = True

    main()