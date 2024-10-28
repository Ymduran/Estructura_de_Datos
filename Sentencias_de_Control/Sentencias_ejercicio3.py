print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 24  octubre del 2024                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Sentencia ejercicio 3                                           * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print("  ")

'''
Escribe un programa de nombre Sentencias_ejercicio3.py que realice lo siguiente:
Este programa determinará un descuento en compras en "La cona", de acuerdo a lo siguiente:
    Si tiene membresía, obtiene un 5 % de descuento en todas sus compras.
    Si tiene la membresía y su compra fue mayor o igual a $ 1000.00, entonces el descuento es del 8 %.
    Si no tiene la membresía, no obtiene ningún descuento y se invita a ser miembro.
Para ello:
a) Solicite al usuario la cantidad comprada en la tienda.
b) Pregunte al usuario si cuenta con la membresía (Si/No).
c) Utilice la lógica adecuada para determinar el total a pagar.
'''

cantidad_comprada=int(input("ingrese cantidad comprada: ")) #Se lee por teclado la cantidad comprada
membresia=input("¿Cuenta con membresía?: si/no: ") #Se lee un si/no
membresia=membresia.lower()=="si" #la respuesta anterior se compara con la cadena "si" para determinar un true o un false

if membresia==False: #Sí la respuesta fue no
    print(f"Se le invita a formar parte de la empresa para obtener un descuento hasta del 8%. El total a pagar es de {cantidad_comprada}")
elif membresia==True and cantidad_comprada<=500: #si la respuesta fue si y la compra es menor o igual a 500
    print("Su descuento es del 5% ")
    print(f"Total a pagar= {cantidad_comprada-(cantidad_comprada*0.05)}") #se hace el descuento con la cantidad de la compra menos el 5%
elif membresia==True and cantidad_comprada>500: #si las respuesta fue si y la compra fue mayor a 500
    print("Su descuento es del 8% ")
    print(f"Total a pagar= {cantidad_comprada - (cantidad_comprada * 0.08)}") #Se hace el descuento de la compra menos el 8%
