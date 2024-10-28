
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 17 octubre del 2024                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Operadores Operadores lódicos  ejercicio 3                       * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

#Se leen por teclado los valores de las respuestas
primer_respuesta, segunda_respuesta, tercer_respuesta, cuarta_respuesta=input("ingrese primer respuesta si/no: "),input("ingrese segunda respuesta si/no: "),input("ingrese tercer respuesta si/no: "),input("ingrese cuarta respuesta si/no: ")
#Se convierten a minúscula y se comparan con la cadena "si" para determinar si es true / false
primer_respuesta, segunda_respuesta,tercer_respuesta,cuarta_respuesta = primer_respuesta.lower()=="si", segunda_respuesta.lower()=="si",tercer_respuesta.lower()=="si", cuarta_respuesta.lower()=="si"
#imprimir el resultado de la operación booleana
print(f"El resultado de la opración booleana es {(primer_respuesta or segunda_respuesta) and (tercer_respuesta or cuarta_respuesta)} ")
