
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 07 de noviembre del 2024                                   * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" *  Función pirámide                                                 * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")


'''
Este programa imprime una pirámide de caracteres '*' de cuatro formas y es la versión del ejercicio Ciclos_ej5_piramide.py, pero ahora utilizando funciones.
Cada pirámide debe estar en una función, la cual se llama en el código a nivel de módulo de acuerdo a las filas requeridas por el usuario.
'''



def funcion_1(numero_filas):
    print("Forma 1 ")
    # Caso 1
    for i in range(1, numero_filas + 1):
        asteriscos = "*" * i  # Este método consite en un sólo for y solo multiplica el número de fila por los asteriscos, en python un caracter se puede multiplicar
        print(asteriscos)
    print(" ")
    print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")

def funcion_2(numero_filas):
    count = numero_filas
    print("Forma 2 ")
    for i in range(1, numero_filas + 1):
        print(" ")
        count -= 1  # Al contador le restará uno pues se igualó con el numero de filas del caso anterior, si imprimió seis filas entonces comenzará imprimiendo seis astericos, decrementando cada iteración para hacer una pirámide inversa
        for j in range(1, count + 2):
            print("*", end=" ")
    print(" ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")


def funcion_3(numero_filas):
    print("Forma 3 ")
    # Cuarto caso
    contador_asterisco = numero_filas
    print()
    for i in range(1,
                   contador_asterisco + 1):  # En el rango de 1 hasta el número de filas, que anteriormente se igualó a contador asteriscos
        espacio = " " * numero_filas
        asteriscos = "*" * i
        print(f"{espacio} {asteriscos}", end=" ")
        i -= 1  # Para imprimir la cantidad de astericos en decremento
        asteriscos = "*" * i
        print(f"{asteriscos}")
        i += 1  # Para imprimir la cantidad de astericos en incremento
        numero_filas -= 1  # Se resta uno en cada interación para multiplicar por los espacios y cada vbez haya menos espacio en la alineación izquierda
        print()
    print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")


def funcion_4(numero_filas):
    print("Forma 4 ")
    count = 0
    contador_asterisco = numero_filas  # Aquí se inicializa el contador_asteriscos igual al número de filas que ingresó el ususario

    for i in range(1, numero_filas + 1):
        espacio = " " * count  # multiplica el espacio por el número de renglones, es decir, si va en el renglón dos, imprimirá dos espacios, esto con el fin de alinear los asteriscos a la derecha
        asteriscos = "*" * contador_asterisco  # Multiplica los asteriscos por el contador
        print(espacio, asteriscos)  # Imprime los espacios y despúés los asteriscos
        contador_asterisco -= 1  # La canidad de astericos decrementa cada vez
        count += 1

    print(" ")
    print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")



numero_filas = int(input("Ingrese número de filas de la pirámide: "))
funcion_1(numero_filas)
funcion_2(numero_filas)
funcion_3(numero_filas)
funcion_4(numero_filas)
