print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 14 octubre del 2024                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Operadores Asignación compuesta                                  * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

numero_entero1 , numero_entero2= input("ingresa número entero 1:  ") , input("ingresa número entero 2:  ")
#conversión a enteros
numero1 = int(numero_entero1)
numero2 = int(numero_entero2)
print(f"ud ingresó los múmeros {numero1} y {numero2}")#muestra números que se ingresaron

numero1 += 3
print(f"numero1 += 3: {numero1}")
numero2 -= 5
print(f"numero2 -= 5: {numero2}")
numero1 /= 4
print(f"numero1 /= 4: {numero1}")

numero_entero1 , numero_entero2= input("ingresa número entero 1:  ") , input("ingresa número entero 2:  ")
#conversión a enteros
numero1 = int(numero_entero1)
numero2 = int(numero_entero2)
print(f"ud ingresó los múmeros {numero1} y {numero2}")
#en python en vez de escribir " numero1 = numero1 + número2 " se puede escribir "numero1+=numero2"
numero1 += numero2
numero1 *= numero1
numero1 -= numero2
numero1 += 3
numero1 /= 2
print(f"resultado final {numero1}")
