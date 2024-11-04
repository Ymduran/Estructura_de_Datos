print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 28  octubre del 2024                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * ciclo while (mientras)                                          * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")


'''
while condición:
--> #Código a hacer mientras
#tabulacción 

'''

print("* * PROGRAMA QUE IMPRIME UN EJEMPLO DE CICLO WHILE * * ")
numero = int(input("ingrese un número entero: "))
contador=1
#EJEMPLO 1
print(f"los número que hay del 1 al {numero} son : ")
while contador<=numero:
    print(contador)
    contador+=1 #nota: en python no hay "contador ++", "++contador"
print("fin de la cuenta")


#EJEMPLO 2
numero = int(input("ingrese otro número entero: "))
contador=1
print(f"los número que hay del 1 al {numero} son : ")
while contador<=numero:
    print(contador, end= " ") #end= significa que imprimir en reemplazo del salto de línea, en este caso solo quiero que imprima un espacio, y lo hará en horizaontal
    contador+=1
print(" fin de la cuenta")



#EJEMPLO 3
numero = int(input("ingrese un número entero: "))
contador=0
print(f"los número pares que hay hasta el número {numero} son : ")
while contador<=numero:
    print(contador, end=" ")
    contador+=2 #nota: en python no hay "contador ++", "++contador"
print("fin de la cuenta")

