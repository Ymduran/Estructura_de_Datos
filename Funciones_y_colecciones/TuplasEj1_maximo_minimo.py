print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 21 noviembre del 24                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Tuplas_ejercicio1                                                * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

'''
Este programa muestra el valor máximo y mínimo de una lista de números. 
En este caso, la tupla se utiliza para devolver los valores máximo y mínimo de la función.
Se debe mostrar el siguiente menú:
  ***  Valor máximo y mínimo de una lista de números del usuario  ***
1) Ver lista de números.
2) Añadir número a la lista.
3) Determinar el valor máximo y mínimo de la lista de números.
0) Salir.
Cualquier otro caso -> Opción no válida.

Para ello:
a) Se sugiere utilizar una función para mostrar el menú.
b) Se debe utilizar una única función para devolver el valor máximo y mínimo en una tupla.
'''


lista_de_numeros = []
#Función menú:
def menu():
    print(" ***  Valor máximo y mínimo de una lista de números del usuario  *** ")
    print("[1].- Ver lista de números.")
    print("[2].- Añadir número a la lista.")
    print("[3].- Determinar el valor máximo y mínimo de la lista de números.")
    print("[4].- Salir.")



#Función que hace las operaciones correspondientes
def operacion_segun_opcion_usuario(option):
    if option == 1: # Ver lista de números
        print("La lista es la siguiente: ")
        for i in lista_de_numeros:
            print(f"{i}, ", end="") #Imprime la lista de números
        if not lista_de_numeros:
            print("No hay elementos a mostrar")
        print()
    elif option == 2: # Añadir número a la lista
        numero_anadir = float(input("Ingrese el número que desea añadir: "))
        lista_de_numeros.append(numero_anadir) #AÑade el nuevo número a la lista con .append
        print("Número agregado :)")
    elif option == 3: #  Determinar el valor máximo y mínimo de la lista de números
        if not lista_de_numeros: #Si la lista está vacía
            print("No hay elementos a mostrar")
        else:
            tupla_receptora = maximo_minimo(lista_de_numeros) #La tupla recibe los números que retornó la función, mentiéndolas en éstas
            print(f"El número máximo es: {tupla_receptora[0]}")
            print(f"El número mínimo es: {tupla_receptora[1]}")
    else:
        print("Opción no válida :(")

def maximo_minimo(lista_de_numeros): #Función que determina el máximo y el mínimo de la lista
    numero_maximo = lista_de_numeros[0] #Se define al primero como el máximo para que se compare posteriormente
    numero_minimo = lista_de_numeros[0]
    for i in lista_de_numeros:
        if i > numero_maximo:
            numero_maximo = i #Se compara con cada elemento y si encuentra uno mayor, lo asigna como número máximo
        if i < numero_minimo:
            numero_minimo = i #Se compara con cada elemento y si encuentra uno menor, lo asigna como número mínimo
    return numero_maximo,numero_minimo #Retorna dos elementos que posteriormente se agregarán a una tupla


flag = 0 #Bandera
while flag == 0: #Mientras que bandera sea cero
    menu()
    option = int(input("Ingresa una opción: "))
    if option == 4: #Cuando la opción sea de salida entonces la bandera cambia de estado y rompe el ciclo
        print("Saliendo del programa... ")
        flag = 1
    else:
        operacion_segun_opcion_usuario(option) #Se manda a llamar la función y se le manda como argumento la opción pues trabajará en torno a esta
    print("------------------------------------------------")
    print(" ")



