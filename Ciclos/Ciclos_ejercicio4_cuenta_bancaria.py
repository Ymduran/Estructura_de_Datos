
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

operacion=1 #Inicializa en cero solamente para que entre al ciclo, aunque también se puede hacer con una bandera
saldo=0.0 #El saldo inicializa en cero, se hace antes del while porque de lo contrario este se reiniciaría en cero cada vez

while operacion !=0: #Mientras que el ususario siga ingresando cualquier otra opción que no sea cero
    print(" ** Menú: ** ")
    print("[0].- Salir")
    print("[1].- Consultar saldo")
    print("[2].- Ingresar dinero")
    print("[3].- Retirar dinero")

    operacion = int(input("ingresa la operación que desea realizar: ")) #Para leer la opción elegida

    if operacion == 1: #consultar saldo
        print(f"su saldo hasta ahora es de: {saldo}")
        print("  ")
    elif operacion== 2:#ingresar dinero
        ingreso=float(input("ingrese cantidad a ingresar: "))
        saldo+=ingreso #Se suma la cantidad a al saldo total
        print(f"su saldo ahora es de: {saldo}")
        print("  ")
    elif operacion==3:#retirar dinero
        retiro=float(input("ingrese cantidad a retirar: "))
        if saldo<retiro: #Solo se va a poder retirar mientras el saldo sea mayor que el retiro
            print("saldo insuficiente")
            print("  ")
        else: #si el saldo es igual o mayor que cantidad a retirar entonces se podrá realizar la operación
            saldo-=retiro #Resta del saldo
            print(f"su saldo ahora es de: {saldo}")
            print("  ")
    elif operacion==0:
        print("saliendo del programa..") #Justo antes de salir imprime este letrero
    else:
        print("operación no válida")

