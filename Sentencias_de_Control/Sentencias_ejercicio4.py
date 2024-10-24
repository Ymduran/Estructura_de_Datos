print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 24  octubre del 2024                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Sentencia ejercicio 4                                           * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print("  ")

'''
Este programa determinará si te permiten el acceso al bar "La Negra", por lo que se debe cumplir lo siguiente:
    Tener al menos 18 años.
    Tener al menos $ 250.00 para gastar.
Si ambas condiciones se cumplen, se imprime el mensaje en consola: "¡Bienvenido a tu mejor bar!". En caso contrario, se imprime: "Lo sentimos, ya estamos por cerrar!"
Para ello:
a) Solicite al usuario su edad.
b) Solicite al usuario el dinero con el que cuenta.
c) Utilice la lógica adecuada para determinar el mensaje.
d) Muestre el mensaje adecuado en consola.
'''

print("**Bar la Negra**")
edad=int(input("ingrese su edad: "))
cantidad_a_gastar=float(input("ingrese catidad disponible para gastar: "))
if edad>=18 and cantidad_a_gastar>=250:
    print("¡Bienvenido a tu mejor bar!")
else:
    print("Lo sentimos, ya estamos por cerrar! :(")