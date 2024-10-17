print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 14 octubre del 2024                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Operadores Relacionales                                          * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

numero_1 , numero_2= input("ingresa número decimal 1:  ") , input("ingresa número decimal 2:  ")
#conversión a flotantes
numero1 = float(numero_1)  #después de leer un dato se debe convertir para realizar operaciones aritméticas con ellas
numero2 = float(numero_2) #En este caso se convierte en un flotante o decimal porque serán los números a comparar
print(f"ud ingresó los múmeros {numero1:.2f} y {numero2:.2f}") #nombre_variable:-2f para imprimir los primeros dos decimales


#Las comparaciones se pueden realizar dentro de las llaves
#el resultado de las comparaciones lógicas es una respuesta true or false
print(f"¿ el primer número {numero1:.2f} es mayor a {numero2:.2f}?           {numero1>numero2}") #mayor que
print(f"¿ el primer número {numero1:.2f}  es mayor o igual a {numero2:.2f}?  {numero1>=numero2}") #mayor o igual
print(f"¿ el primer número {numero1:.2f} es menor a {numero2:.2f}?           {numero1<numero2}")#menor que
print(f"¿ el primer número {numero1:.2f} es menor o igual a {numero2:.2f}?   {numero1<=numero2}")#menor o igual
print(f"¿ Son iguales el número {numero1:.2f} al número {numero2:.2f}?       {numero1==numero2}")#igual
print(f"¿ Son diferentes los números {numero1:.2f} y {numero2:.2f}?          {numero1!=numero2}")#diferente de

