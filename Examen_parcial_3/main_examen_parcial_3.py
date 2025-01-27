from colorama import Fore

import Calculadora_argumentos_variables
import Promedio_materias
import Juego_del_gato
import cuatro_en_raya
import juego_ahorcado

print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 27 de diciembre del 2025                                  * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * main; código principal del examen                                * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

print(Fore.GREEN+ " |-------        ------------- ------                ")
print(Fore.RED+   " |         )     |                 /")
print(Fore.CYAN+  " |   D     )      ---------       /     ")
print(Fore.YELLOW+" |       )                 /     /      ")
print(Fore.BLUE+  " |     )                  /     /         ")
print(Fore.GREEN+ " |  |                    /     / _")
print(Fore.RED+   " |  |                   |           )    ")
print(Fore.CYAN+  " |  |                    )            )           ")
print(Fore.YELLOW+" ---                       )           )      ")
print(Fore.BLUE+  "                           )           )   ")
print(Fore.GREEN+ "                   | ------           )    ")
print(Fore.RED+   "                   |                )      ")
print(Fore.CYAN+  "                   -----------------       ")





def menu_principal() -> int:
    """
    Función que muestra el menú principal para seleccionar cualquier programa
    :return: Entero válido para validar el dato
    """

    print(Fore.LIGHTYELLOW_EX+"** MENÚ PRINCIPAL ** ")
    print(Fore.GREEN+"1.- Calculadora Argumentos variables.")
    print(Fore.YELLOW+"2.- Calcular promedios parciales. ")
    print(Fore.MAGENTA+"3.- Juego_del_gato. ")
    print(Fore.BLUE+"4.- Juego de Cuatro en raya. ")
    print(Fore.CYAN+"5.- Juego del ahorcado.")
    print(Fore.RED+"6.- Salir. ")
    print(Fore.LIGHTBLUE_EX+" ")
    opcion = input("Selecciona una opción: ")
    while not opcion.isnumeric() or int(opcion) not in range(1, 7):
        print("Opción no válida. Intenta de nuevo")
        opcion = input("Selecciona una opción: ")
    return int(opcion)





if __name__ == '__main__':
    opcion = 0
    while True:
        opcion = menu_principal()

        if opcion == 1:
            Calculadora_argumentos_variables.ejecutar_calculadora()
        elif opcion == 2:
            Promedio_materias.ejecutar_promedio_materias()
        elif opcion == 3:
            Juego_del_gato.ejecutar_juego_del_gato()
        elif opcion == 4:
            cuatro_en_raya.ejecutar_cuatro_en_raya()
        elif opcion == 5:
            juego_ahorcado.ejecutar_juego_ahorcado()
        elif opcion == 6:
            print("Saliendo, Gracias por jugar. :) ...")
            break
        else:
            print("Opción no válida. Ingresa un número del 1 al 6")
