
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha:  13 de diciembre del 2025                                 * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * funcion main                                                     * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

def menu() -> None:
    """
    Función que muestra el menú
    :return: No retorna nada
    """
    print("Menú ")
    print("1.- Sumar ")
    print("2.- Restar ")
    print("3.- Salir ")

def calcular(option:int) -> float | None:
    """
    Función que hace la suma o resta de dos números, según lo desee el usuario
    :param option: Recibe un entero
    :return: Retorna el resultado en tipo flotante o de no tratarse de un número enonces retorna none
    """

    first_number = float(input("Ingresa primer número: "))
    second_number = float(input("Ingresa segundo número: "))

    if option == 1:
        resultado = first_number + second_number
        return resultado
    elif option == 2:
        resultado = first_number - second_number
        return resultado
    else:
        return None





def main() -> None:
    print(__name__)
    if __name__ == '__main__':
        flag = 0
        while flag == 0:
            menu()
            option = int(input("Igrese una opción: "))
            if option == 1 or option == 2:
                resultado = calcular(option)
                print(f"El resultado de la operación es: {resultado}")
            elif option == 3:
                print("Saliendo...")
                flag = 1
            else:
                print("Opción no válida. Intente de nuevo")

main()