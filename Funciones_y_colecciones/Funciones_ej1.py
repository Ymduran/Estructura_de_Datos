print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 11 noviembre del 24                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Funciones                                                        * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

'''
Definición "Código de nivel de módulo". Aquel que se ejecuta directamente en el programa. Dicho de otro modo, es el código que no está en función y que sirve como punto de partida 
para ejecutar el programa.
'''





#Función hola: def nombre_función(dato_que_recibe)
def hola(nombre):  # Para crear un función se usa la palabra reservada "def", el nombre y el dato a recibir
    print(f"hola, {nombre}") #Imprime hola y el dato que recibió la función

#Función calculadora: Esta función recibe una opción, y dos números del "código de nivel de módulo" y retorna/devuelve el resultado de las operaciones
def calculadora(opcion, numero1, numero2):
    resultado = 0
    if opcion == 1:
        resultado = numero1 + numero2  # suma
    elif opcion == 2:
        resultado = numero1 - numero2  # resta
    elif opcion == 3:
        resultado = numero1 * numero2  # Multiplicación
    elif opcion == 4:
        resultado = numero1 / numero2  # resultado de división en flotante (decimal)
    elif opcion == 5:
        resultado = numero1 // numero2  # resultado de división en entero
    elif opcion == 6:
        resultado = numero1 % numero2  # Módulo de la divisón
    elif opcion == 7:
        resultado = numero1 ** numero2  # eleva al primero a la potencia del segundo número
    return resultado

#Función menú: Esta función no recibe nada, su función, valga la redundancia, es solo imprimir el menú
def menu(): #No tiene nada entre los paréntesis puesto que no recibe nada
    print(" ** Menú: ** ")
    print("[1].- Suma")
    print("[2].- Resta")
    print("[3].- Multiplicación")
    print("[4].- División ")
    print("[5].- División entera")
    print("[6].- Módulo")
    print("[7].- Exponenciación")


#Código nivel de módulo:
nombre = input("ingrese su nombre: ")
hola(nombre)
print("Adiós")


menu() #Se manda a llamar, pero sin ningún argumento
opcion = int(input("ingrese una opción: ")) 
numero_uno = float(input("ingrese primer número: "))
numero_dos = float(input("ingrese segundo número: "))
resultado = calculadora(opcion,numero_uno,numero_dos) #Aquí se manda a llamar la función calculadora y se le mandan los datos entre parentesis (como una copia) para que trabaje con ellos
print(f"El resultado es: {resultado:.2f}")




