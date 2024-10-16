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
#conversión a enteros
numero1 = float(numero_1)
numero2 = float(numero_2)
print(f"ud ingresó los múmeros {numero1:.2f} y {numero2:.2f}")

print(f"¿ el primer número {numero1:.2f} es mayor a {numero2:.2f}?           {numero1>numero2}")
print(f"¿ el primer número {numero1:.2f}  es mayor o igual a {numero2:.2f}?  {numero1>=numero2}")
print(f"¿ el primer número {numero1:.2f} es menor a {numero2:.2f}?           {numero1<numero2}")
print(f"¿ el primer número {numero1:.2f} es menor o igual a {numero2:.2f}?   {numero1<=numero2}")
print(f"¿ Son iguales el número {numero1:.2f} al número {numero2:.2f}?       {numero1==numero2}")
print(f"¿ Son diferentes los números {numero1:.2f} y {numero2:.2f}?          {numero1!=numero2}")

