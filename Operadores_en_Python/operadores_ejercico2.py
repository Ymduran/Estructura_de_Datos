print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 17 octubre del 2024                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Operadores Operadores logicos  ejercicio 2                       * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

respuesta1=input("Es profesor de la unsij si/no: ") #Se lee por teclado la primera respuesta si/no
respuesta1=respuesta1.lower()== "si" #Se convierte a minúsculas y se compara con la cadena si, esto dará un resultado booleano true/False
respuesta2=input("Es estudiante de la unsij? si/no: ") #Se lee por teclado la segunda respuesta si/no
respuesta2=respuesta2.lower()== "si"#Se convierte a minúsculas y se compara con la cadena si, esto dará un resultado booleano true/False
print(f"forma parte de la comunidad de la unsij? {respuesta1 or respuesta2}") #Cuando alguna de las dos respuesatas sea correcta
                                                #Algunos casos son:
                                                # true or true = true
                                                # true or false = true
                                                # False or false = False
