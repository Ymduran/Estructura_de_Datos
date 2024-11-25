
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 13- noviembre del 24                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * lista de compras                                                 * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

'''
'''
# Función para imprimir menú
def menu ():
    print(" ** Menú: ** ")
    print("[1].- Ver lista")
    print("[2].- Añadir producto a la lista")
    print("[3].- Eliminar producto")
    print("[4].- Salir")



# Función que hace todas las modificaciones a la lista
def modificar_lista_compras(option):
    if option == 1:
        len(lista_de_compras) # Acomodar según añadidos con la función len()
        len(lista_cantidad_compras)
    elif option == 2: #Añadir artículo
        articulo_añadir, cantidad_añadir = input("Ingrese nombre del artículo a añadir: "), int(input("Ingrese la cantidad a añadir: "))
        lista_de_compras.append(articulo_añadir)
        lista_cantidad_compras.append(cantidad_añadir)
    elif option == 3:
        articulo_eliminar = int(input("ingrese número de lista del artículo a eliminar: "))
        lista_de_compras.pop(articulo_eliminar)  # eliminación por índice
        lista_cantidad_compras.pop(articulo_eliminar)
    return lista_de_compras, lista_cantidad_compras


#Fun ción para mostrar la lista; solo imprime la lista
def mostrar_lista (lista_de_compras, lista_candidad_compras):
    count = 0
    for articulo in lista_de_compras:
        print(f"{count}.- {articulo}...............{lista_candidad_compras[count]}")
        count +=1
    print(" ")
    print(" ")



#Código nivel de módulo
lista_de_compras = []
lista_cantidad_compras = []


flag = 0
while flag == 0: # Hacer mientras que bandera sea igual a cero
    menu()
    option = int(input("Elige una opción: "))
    modificar_lista_compras(option)
    if option == 4:
        print("Saliendo...")
        flag = 1 #Si la opción es igual a 4 = Salir entonces la bandera cambia de valor y se rompe el ciclo
    elif option > 4 or option < 0:
        print("Opción no válida :( ")
    else: #Si la opción es otra que no sea 4, entonces muestra la lista y continúa el ciclo
        mostrar_lista(lista_de_compras, lista_cantidad_compras)




