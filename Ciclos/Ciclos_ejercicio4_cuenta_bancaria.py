
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 29  octubre del 2024                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * ciclos ejercicio número 4.                                       * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print("  ")

'''
'''

print(" ** BIENVENIDO A BANCO AZTECA ** ")

operacion=1
saldo=0.0

while operacion !=0:
    print(" ** Menú: ** ")
    print("[0].- Salir")
    print("[1].- Consultar saldo")
    print("[2].- Ingresar dinero")
    print("[3].- Retirar dinero")

    operacion = int(input("ingresa la operación que desea realizar: "))

    if operacion == 1: #consultar saldo
        print(f"su saldo hasta ahora es de: {saldo}")
        print("  ")
    elif operacion== 2:#ingresar dinero
        ingreso=float(input("ingrese cantidad a ingresar: "))
        saldo+=ingreso
        print(f"su saldo ahora es de: {saldo}")
        print("  ")
    elif operacion==3:#retirar dinero
        retiro=float(input("ingrese cantidad a retirar: "))
        if saldo<retiro: #Solo se va a poder retirar mientras el saldo sea mayor que el retiro
            print("saldo insuficiente")
            print("  ")
        else: #si el saldo es igual o mayor que cantidad a retirar entonces se podrá realizar la operación
            saldo-=retiro
            print(f"su saldo ahora es de: {saldo}")
            print("  ")
    elif operacion==0:
        print("saliendo del programa..")
    else:
        print("operación no válida")

