print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 21 de diciembre del 2025                                  * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Calculadora con argumentos variables                             * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

def menu() -> int:
    """
    Muestra el menú de opciones y solicita una selección al usuario.

    :return: La opción seleccionada por el usuario como un entero.
    """
    print("** MENÚ DE LA CALCULADORA ** ")
    print("1.- Sumar")
    print("2.- Multiplicar")
    print("3.- Salir")

    opcion = input("Selecciona una opción: ")
    while not opcion.isnumeric() or int(opcion) not in range(1, 4):
        print("Opción no válida. Intenta de nuevo")
        opcion = input("Selecciona una opción: ")
    return int(opcion)



def cadena_a_entero(cadena):
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-")
    if revisar_cadena.isnumeric() and no_guiones in (0, 1):
        return int(cadena)
    else:
        return None

def validar_entrada(cadena: str) -> list[int]:
    """
    Valida y convierte una cadena de números seprados por comas en una lista de enteros.

    :param cadena: La cadena a validar y convertir
    :return: Una lista de números enteros si la entrada es válida
    """
    
    
    numeros = cadena.split(",")
    lista_numeros = []
    for num in numeros:
        convertido = cadena_a_entero(num.strip())
        if convertido is None:
            return None
        lista_numeros.append(convertido)
    return lista_numeros



def sumar(*vargs: int) -> int:
    """
    Suma todos los números dados como argumentos

    :param vargs: Números a sumar.
    :return: La suma de los números.
    """
    return sum(vargs)
    
    

def multiplicar(*vargs: int) -> int:
    """
    Resta todos los números dados como argumentos en orden

    :param vargs: Números a multiplicar
    :return: El resultado de la multiplicación de los números.
    """
    
    if len(vargs) == 0:
        return 0
    resultado = vargs[0]
    for num in vargs[1:]:
        resultado *= num
    return resultado
    
    
    
    
    

if __name__ == '__main__':
    Flag = 0
    while Flag == 0:
        opcion = menu()

        if opcion == 1:
            numeros = input("Introduce los números a sumar, separados por comas: ")
            numeros = validar_entrada(numeros)
            if numeros is None:
                print("Opción inválida. Todos los elementos deben ser números enteros separados por comas.")
                
            else:
                resultado = sumar(*numeros)
                print(f"El resultado de la suma es: {resultado}")

        elif opcion == 2:
            numeros = input("Introduce los números a multiplicar, separados por comas: ")
            numeros = validar_entrada(numeros)
            
            if numeros is None:
                print("Opción inválida.  Todos los elementos deben ser números enteros separados por comas ")
            else:
                resultado = multiplicar(*numeros)
                print(f"El resultado de la multiplicar es: {resultado}")


        elif opcion == 3:
            print("Saliendo...")
            Flag = 1

        print("")
