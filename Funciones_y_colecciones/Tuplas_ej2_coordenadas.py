print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 25 noviembre del 24                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Conjuntos                                                        * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")


'''
print("** EJEMPLOS CON COORDENADAS ** ")
punto1 = (1,0)
punto2 = (5,3)

print(f"coordenadas en tuplas: {punto1} y {punto2}")
#Desempaquetado de tuplas
x1, y1 = punto1
x2, y2 = punto2

#Expresión de la recta: y=mx+b
m = (y2-y1)/(x2-x1)
b = y1 - (m*x1)
print(f"el valor de la recta es: y = {m}x + {b}")
'''

'''
Escribe un programa de nombre Tuplas_ej2_coordenadas.py que realice lo siguiente:
Este programa almacena diversos puntos como coordenadas y
 permite obtener la ecuación de la recta entre dos de los puntos.
Se debe mostrar el siguiente menú:
  ***  Rectas a partir de puntos (coordenadas) en el plano cartesiano  ***
1) Ver coordenadas almacenadas.
2) Agregar coordenada (x,y).
3) Calcular la pendiente y la ecuación de la recta entre dos coordenadas.
4) Eliminar coordenada (x,y).
0) Salir.
Cualquier otro caso -> Opción no válida.
Para ello:
a) Utilice funciones para modular el código.
b) Utilice una tupla para almacenar las coordenadas (x,y) del punto.
c) Utilice una lista para almacenar las tuplas de las coordenadas.

'''
lista_de_coordenas = []
def menu():
    print(" ** Menú: ** ")
    print("[1].- Ver coordenadas almacenadas")
    print("[2].- Agregar coordenada (x,y)")
    print("[3].- Calcular la pendiente y la ecuación de la recta entre dos coordenadas")
    print("[4].- Eliminar coordenada (x,y) ")
    print("[0].- Salir")

def funcion_operacion_del_menu (opcion):
    count = 0
    if opcion == 1:
        if not lista_de_coordenas: #Sí la lista está vacía
            print("No hay coordenadas para mostrar: ")
        for cordenada in lista_de_coordenas: #Imprime cada coordenada en la lista de coodenadas
            print(f"Coordenada {count}.- {cordenada}")
            count += 1
    if opcion == 2:
        punto_x = int(input("Ingresa coordenada -x- del punto: "))
        punto_y = int(input("Ingresa cordenada -y- del punto: "))
        lista_de_coordenas.append((punto_x, punto_y))
        print("Se agregaron coordenas x y y :)")
    if opcion == 3:
        #Esta parte imprime para que el usuario elija los puntos entre los cuales hará la ecuacuón
        if not lista_de_coordenas: #Sí la lista está vacía
            print("No hay coordenadas para mostrar: ")
        for cordenada in lista_de_coordenas:
            print(f"Punto {count}.- {cordenada}")
            count += 1

        punto1_indice = int(input("Ingrese el número del punto 1: "))
        punto2_indice = int(input("Ingrese el número del punto 2: "))
        #Desempaquetado de tuplas
        x1,y1 = lista_de_coordenas[punto1_indice]
        x2,y2 = lista_de_coordenas[punto2_indice]
        # Espresión de la recta: y = m1 + b
        m = (y2 - y1) / (x2 - x1)
        b = y1 - (m * x1)
        print(f"el valor de la recta es: y = {m}x + {b}")
    if opcion == 4:
        # Esta parte imprime para que el usuario elija el punto a eliminar
        if not lista_de_coordenas:  # Sí la lista está vacía
            print("No hay coordenadas para mostrar: ")
        for cordenada in lista_de_coordenas:
            print(f"Punto {count}.- {cordenada}")
            count += 1


        #Para eliminar
        coordenada_eliminar = int(input("Ingrese el número del punto a eliminar: "))
        del lista_de_coordenas[coordenada_eliminar]


#Código nivel de módulo
flag = 0
while flag == 0:
    menu()
    opcion = int(input("Ingrese una opción: "))
    funcion_operacion_del_menu(opcion)
    if opcion == 0:
        print("Saliendo...")
        flag = 1
