print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 29  octubre del 2024                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * ciclos ejercicio número 3. calculadora                           * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")

print("  ")



'''
'''

print(" ** CALCULADORA BÁSICA ** ")

opcion = 1 #Se iguala a 1 para que pueda entrar al ciclo pero posteriormente se cambiará a la opción que se ingrese por teclado

while opcion !=0: #Mientras que la opción sea diferente de cero seguirá mostrando el menú
    print(" ** Menú: ** ")
    print("[0].- Salir")
    print("[1].- Suma")
    print("[2].- Resta")
    print("[3].- Multiplicación")
    print("[4].- División ")
    print("[5].- División entera")
    print("[6].- Exponenciación")

    opcion = int(input("ingresa una opción: ")) #es necesario convertirlo a emtero porque a pesar de ya haber definido el tipo de datos en la línea 17, las variables en python son dinámicas, lo que significa que en diferentes puntos del programa puede tomar distintos tipos de valor

    if opcion==1:#suma
        numero1, numero2 = float(input("Ingrese primer número: ")), float(input("Ingrese segundo número: "))
        print(f"{numero1} + {numero2} = {(numero1 + numero2):.2f}")
        print("  ")
    elif opcion==2:#resta
        numero1, numero2 = float(input("Ingrese primer número: ")), float(input("Ingrese segundo número: "))
        print(f"{numero1} - {numero2} = {(numero1 - numero2):.2f}")
        print("  ")
    elif opcion==3:#multiplicación
        numero1, numero2 = float(input("Ingrese primer número: ")), float(input("Ingrese segundo número: "))
        print(f"{numero1} * {numero2} = {(numero1 * numero2):.2f}")
        print("  ")
    elif opcion==4:#división
        numero1, numero2 = float(input("Ingrese primer número: ")), float(input("Ingrese segundo número: "))
        print(f"{numero1} / {numero2} = {(numero1 / numero2):.2f}")
        print("  ")
    elif opcion==5:
        numero1, numero2 = float(input("Ingrese primer número: ")), float(input("Ingrese segundo número: "))
        print(f"{numero1} // {numero2} = {(numero1 // numero2):.2f}")
        print("  ")
    elif opcion==6:
        numero1, numero2 = float(input("Ingrese primer número: ")), float(input("Ingrese segundo número: "))
        print(f"{numero1} ** {numero2} = {(numero1 ** numero2):.2f}")
        print("  ")
    elif opcion==0:
        print("saliendo...")
    else:
        print("opción no válida")









