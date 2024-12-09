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


def decimal_a_binario_hexadecimal(): #Función para convertir de decimal al binario
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
            lista_binario.append(numero_decimal_auxiliar) #Añade a la lista el nuevo dígito, también este caso significa que es el último caso
            flag_decimal_binario = 1 #Cambia la bandera y rompe el ciclo
    print(f"{numero_decimal} en binario es: ") 
    #Invertir lista
    for i in range(1,len(lista_binario)+1):
        print(f"{lista_binario[i*-1]}", end="") #imprime la lista desde -1 hasta -n, donde -n es el número total de elementos de la lista, recordando que el índice -1 refiere al último elemento de la lista

    #Para convertir de decimal a hexadecimal
    print("\n")
    numero_decimal_auxiliar = numero_decimal #Reinicio el número decimal auxiliar
    flag_decimal_hexadecimal = 0 #Bandera para controlar el ciclo while que convierte a hexadecimal
    lista_hexadecimal = []
    lista_letras_hexadecimal = ["A","B","C","D","E","F"] #Lista de los caracteres del 10 al 15 en hexadecimal
    while flag_decimal_hexadecimal == 0: 
        digito_hexadecimal = numero_decimal_auxiliar % 16 #el módulo de la división sobre 15 se asigna al dígito hexadecimal
        if digito_hexadecimal >= 10 and digito_hexadecimal <= 15: #Pero si el dígito hexadecimal se encuentra entre el rango de 10 a 15, entonces se reemplaza por una letra
            digito_hexadecimal = lista_letras_hexadecimal[digito_hexadecimal-10] #Según la letra que le corresponda de la lista_letas_hexadecimal
        lista_hexadecimal.append(digito_hexadecimal) #Se añade a la lista de hexadecimal
        numero_decimal_auxiliar = numero_decimal_auxiliar // 16 #Y ahora numero_decimal_auxiliar vale ese mismo número // 1(división entera)
        if numero_decimal_auxiliar == 0 or numero_decimal_auxiliar == 1: #Significa que ya terminó de dividir
            lista_hexadecimal.append(numero_decimal_auxiliar) #Y añade el último a la lista_hexadecimal
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

  #Dependiendo del valor literal que haya en la cadena se convierte a número
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
        else: #Sí no se trata de ninguna letra, entonces se convierte a entero directamente
            lista_digitos_hexadecimal_auxiliar[i] = int(lista_digitos_hexadecimal_auxiliar[i])

    numero_decimal = 0 3esta será la sumatoria de los dígitos con un 1
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


def conversion(option): #según la opción que haya ingresado el usuario manda a llamar la función correspondiente
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





