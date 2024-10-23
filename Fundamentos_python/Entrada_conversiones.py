print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 10 octubre del 2024                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     *")
print(" * Entrada conversiones                                             * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

# Comentar sobre las funciones anidadas.
#Se leen los datos por consola al mismno tiempo que se realiza el casting al tipo de dato que corresponde, ahorrando líneas de código
print("****   Datos de los alumnos    *****")
nombre = input("Ingresa el nombre: ")  #El nombre se queda igual puesto que ya se lee como una cadena
semestre = int(input("Ingresa el no. de semestre: "))#El semestre se lee como un tipo de dato entero
promedio = float(input("Ingresa el promedio: "))#El promedio como un tipo de dato flootante
es_mujer = input("¿Es mujer (Si/No)?: ")# Y la respuesta se comparará posteriorteriomente con la dena "si", puesto que este no se puede convertir directamente
# Entonces se puede describir como: variable = tipo_de_dato(input("letrero a imprimir"))

# No es posible convertir directamente una cadena a un valor booleano.
# Por ello, utilizamos la misma variable, convertimos a  minúsculas y lo comparamos con la cadena "si".
es_mujer = es_mujer.lower() == "si" #Se convierte a minúscula y se compara con la cadena "si"


# Se imprimen los datos del alumno.
# Comentar  qué es lo que realiza {promedio:.2f} probando con números diferentes.
print()#Salto de línea
print(f"El alumno {nombre} cursa el {semestre} semestre con un promedio de {promedio:.2f}. Además, es mujer: {es_mujer}.")#Ya no necesario convertir en otra línea cada uno de los datos, y así se imprimen de forma correspondiente.



