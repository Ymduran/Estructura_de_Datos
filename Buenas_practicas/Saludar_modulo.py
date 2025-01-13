print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha:  13 de diciembre del 2025                                 * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Saludar módulo                                                  * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")


def saludar(nombre: str) -> None:
    """
    Función que saluda al usuario
    :param nombre: tipo cadena
    :return: No retorna nada
    """
    print(f"Hola, {nombre}")


#Código nivel de núdulo

if __name__ == '__main__':
    nombre = input("Ingresa nombre: ")
    saludar(nombre)

