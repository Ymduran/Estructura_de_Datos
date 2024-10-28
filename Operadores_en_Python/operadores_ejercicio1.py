print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 17 octubre del 2024                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Operadores Operadores lógicos  ejercicio                         * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

compras=input("ingrese cantidad de sus compras ") #Se lee la cantidad de compras por teclado
compras=int(compras) #Se convierte a entero
meses_sin_intereses=input("las compras con a meses sin intereses? si/no: ") #Se lee una respuesta
meses_sin_intereses=meses_sin_intereses.lower()== "si" #Respuesta se convierte a minúsculas y posteriormente se compara con la cadena "si"
print(f"aplica bonificacion? {(compras>5000) and meses_sin_intereses}") #Compara si la cantidad de compras es mayor que cinco mil y si la respuesta a la pregunta fue si
                              #  true         and         true = true
                              #  true         and         False =false
                              #  False        and         False =false