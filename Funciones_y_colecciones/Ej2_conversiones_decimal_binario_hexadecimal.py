print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 09 de diciembre de 24                                     * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Ej2_conversiones_decimal_binario_hexadecimal                     * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

'''
Instrucciones:
Escribe un programa de nombre Ej2_conversiones_decimal_binario_hexadecimal.py que realice lo que se indica en la descripción del programa.
Comparte el enlace de GitHub en la caja de texto al final de la pregunta.
Descripción del programa:
Este programa convierte números entre las bases decimal, binaria y hexadecimal.
Se debe mostrar el siguiente menú:
  ***  Ejercicio 2. Conversión entre las bases decimal, binaria y hexadecimal.  ***
1) Convertir de decimal a binario y hexadecimal.
2) Convertir de binario a decimal y hexadecimal.
3) Convertir de hexadecimal a decimal y binario.
0) Salir.
Cualquier otro caso -> Opción no válida.
Para ello:
a) Utilice la lógica adecuada para mostrar las conversiones. No utilice funciones como bin() o hex().
b) Asuma que el usuario siempre va a ingresar números en el formato adecuado. Por ejemplo: 1001 como número binario o 1F como hexadecimal, no 120 como número binario o 1Z como hexadecimal.
c) Para considerar el ejercicio como completo, utilice funciones para mostrar el menú y para las conversiones entre bases, considerando que cada función devuelve una tupla. Por ejemplo, la función que recibe el número decimal debe devolver el valor en binario y en hexadecimal como una tupla.
'''

print(" ***  Ejercicio 2. Conversión entre las bases decimal, binaria y hexadecimal.  *** ")

def menu():
    print("\n------------------------------------------ ")
    print("** MENÚ **")
    print("[1].- Convertir de decimal a binario y hexadecimal.")
    print("[2].- Convertir de binario a decimal y hexadecimal.")
    print("[3].- Convertir de hexadecimal a decimal y binario.")
    print("[0].- Salir.")


def decimal_a_binario_hexadecimal():
    numero_decimal = int(input("Ingrese un número decimal entero: "))
    numero_decimal_auxiliar = numero_decimal
    #Para convertir de decimal a binario
    lista_binario = []  # Lista vacía
    flag_decimal_binario = 0
    while flag_decimal_binario == 0:
        digito_binario = numero_decimal_auxiliar % 2 #Dígito binario será igual a 1 o 0
        lista_binario.append(digito_binario) #Agrega el 1 o 0, según corresponda a la lista_binario
        numero_decimal_auxiliar = numero_decimal_auxiliar // 2 #Ahora numero_decimal_auxiliar será la divisón entera del número decimal entre dos
        if numero_decimal_auxiliar == 0 or numero_decimal_auxiliar == 1: #Sí el resultado de la división entera del numero decimal entre dos es 1 o 0, significa que debe terminar el ciclo
            lista_binario.append(numero_decimal_auxiliar)
            flag_decimal_binario = 1
    print(f"{numero_decimal} en binario es: ")
    #Invertir lista
    for i in range(1,len(lista_binario)+1):
        print(f"{lista_binario[i*-1]}", end="") #imprime la lista desde -1 hasta -n, donde -n es el número total de elementos de la lista, recordando que el índice -1 refiere al último elemento de la lista

    #Para convertir de decimal a hexadecimal
    print("\n")
    numero_decimal_auxiliar = numero_decimal #Reinicio el número decimal auxiliar
    flag_decimal_hexadecimal = 0
    lista_hexadecimal = []
    lista_letras_hexadecimal = ["A","B","C","D","E","F"]
    while flag_decimal_hexadecimal == 0:
        digito_hexadecimal = numero_decimal_auxiliar % 16
        if digito_hexadecimal >= 10 and digito_hexadecimal <= 15:
            digito_hexadecimal = lista_letras_hexadecimal[digito_hexadecimal-10]
        lista_hexadecimal.append(digito_hexadecimal)
        numero_decimal_auxiliar = numero_decimal_auxiliar // 16
        if numero_decimal_auxiliar == 0 or numero_decimal_auxiliar == 1:
            lista_hexadecimal.append(numero_decimal_auxiliar)
            flag_decimal_hexadecimal = 1
        
    print(f"{numero_decimal} en hexadecimal es: ")
    for i in range(1, len(lista_hexadecimal) + 1):
        print(f"{lista_hexadecimal[i * -1]}", end="")



def binario_a_decimal_hexadecimal():
    numero_binario = input("Ingrese un número binario: ")
    lista_digitos_binario = [int(un_digito) for un_digito in numero_binario]
    lista_digitos_binario_auxiliar = lista_digitos_binario
    numero_decimal = 0
    exponente = 0
    digito_invertido = -1
    #Para convertir de binario a decimal
    for i in lista_digitos_binario_auxiliar:
        numero_decimal += (2 ** exponente) * lista_digitos_binario_auxiliar[digito_invertido]
        exponente += 1
        digito_invertido -= 1
    print(f"{numero_binario} en decimal es:")
    print(numero_decimal)

    #Para convertir a Hexadecimal
    numero_decimal_auxiliar = numero_decimal  # Reinicio el número decimal auxiliar
    flag_decimal_hexadecimal = 0
    lista_hexadecimal = []
    lista_letras_hexadecimal = ["A", "B", "C", "D", "E", "F"]
    while flag_decimal_hexadecimal == 0:
        digito_hexadecimal = numero_decimal_auxiliar % 16
        if digito_hexadecimal >= 10 and digito_hexadecimal <= 15:
            digito_hexadecimal = lista_letras_hexadecimal[digito_hexadecimal - 10]
        lista_hexadecimal.append(digito_hexadecimal)
        numero_decimal_auxiliar = numero_decimal_auxiliar // 16
        if numero_decimal_auxiliar == 0 or numero_decimal_auxiliar == 1:
            lista_hexadecimal.append(numero_decimal_auxiliar)
            flag_decimal_hexadecimal = 1
        print(f"{numero_binario} en hexadecimal es:")
        for i in range(1, len(lista_hexadecimal) + 1):
            print(f"{lista_hexadecimal[i * -1]}", end="")

def hexadecimal_a_decimal_binario():
    numero_hexadecimal = input("Ingrese número hexadecimal: ")
    lista_digitos_hexadecimal = [un_digito for un_digito in numero_hexadecimal]
    lista_digitos_hexadecimal_auxiliar = lista_digitos_hexadecimal


    for i in range(len(lista_digitos_hexadecimal)):
        if lista_digitos_hexadecimal[i] == "A":
            lista_digitos_hexadecimal_auxiliar[i] = 10
        elif  lista_digitos_hexadecimal[i] == "B":
            lista_digitos_hexadecimal_auxiliar[i] = 11
        elif lista_digitos_hexadecimal[i] == "C":
            lista_digitos_hexadecimal_auxiliar[i] = 12
        elif lista_digitos_hexadecimal[i] == "D":
            lista_digitos_hexadecimal_auxiliar[i] = 13
        elif lista_digitos_hexadecimal[i] == "E":
            lista_digitos_hexadecimal_auxiliar[i] = 14
        elif lista_digitos_hexadecimal[i] == "F":
            lista_digitos_hexadecimal_auxiliar[i] = 15
        else:
            lista_digitos_hexadecimal_auxiliar[i] = int(lista_digitos_hexadecimal_auxiliar[i])

    numero_decimal = 0
    exponente = 0
    digito_invertido = -1
    for i in lista_digitos_hexadecimal_auxiliar:
        numero_decimal += (16 ** exponente) * lista_digitos_hexadecimal_auxiliar[digito_invertido]
        exponente += 1
        digito_invertido -= 1
    print(f"{numero_hexadecimal} en decimal es: ", end="")
    print(numero_decimal)

    #Para convertir a binario
    numero_decimal_auxiliar = numero_decimal
    lista_binario = []  # Lista vacía
    flag_decimal_binario = 0
    while flag_decimal_binario == 0:
        digito_binario = numero_decimal_auxiliar % 2  # Dígito binario será igual a 1 o 0
        lista_binario.append(digito_binario)  # Agrega el 1 o 0, según corresponda a la lista_binario
        numero_decimal_auxiliar = numero_decimal_auxiliar // 2  # Ahora numero_decimal_auxiliar será la divisón entera del número decimal entre dos
        if numero_decimal_auxiliar == 0 or numero_decimal_auxiliar == 1:  # Sí el resultado de la división entera del numero decimal entre dos es 1 o 0, significa que debe terminar el ciclo
            lista_binario.append(numero_decimal_auxiliar)
            flag_decimal_binario = 1
    print(f"{numero_hexadecimal} en binario es: ")
    # Invertir lista
    for i in range(1, len(lista_binario) + 1):
        print(f"{lista_binario[i * -1]}",
              end="")  # imprime la lista desde -1 hasta -n, donde -n es el número total de elementos de la lista, recordando que el índice -1 refiere al último elemento de la lista


def conversion(option):
    if option == 1:
        decimal_a_binario_hexadecimal()
    elif option == 2:
        binario_a_decimal_hexadecimal()
    elif option == 3:
        hexadecimal_a_decimal_binario()


#Código nivel de módulo
flag = 0
while flag == 0:
    menu()
    option = int(input("Ingrese una opción: "))
    if option == 0:
        print("Saliendo...")
        flag = 1
    elif option >= 1 and option <= 3:
        conversion(option)
    else:
        print("Opción no válida :(")





