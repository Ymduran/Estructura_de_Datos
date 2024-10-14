

# Durán Breceda Lourdes Jamileth
# 8 de septiembre de 2024
# En este archivo se ejemplifica el uso de variables en Python.

# Notas:
# En Python todo es un objeto.
# Variable - una variable es un nombre que almacena un valor guardado en la memoria temporal

# Toda variable requiere un valor inicial
semestre = 3        # es una variable que apunta a un objeto de tipo int con valor de 3
print(semestre)     # imprime el valor de la variable
semestre = 4        # la variable ya no apunta al objeto anterior, sino a uno nuevo, por lo que se pierde la referencia
print(semestre)

# Se crean varias variables para ejemplificar su uso
nombre = "Yamm"  # variable de tipo String, no es necesario declarar la cadena, sin embargo si las "" que indican que la variable es de tipo string
altura = 1.56       # variable de tipo Float, no es necesario declarar el float
edad = 18           # variable de tipo Int, no es necesario declarar el int

# Se imprimen las variables, añadiendo información adicional para comprender lo que se imprime

print("Nombre:", nombre) # la "," separa lo que se imprimirá y lo hará en la misma línea
print() #Para salto de línea
print("Semestre:", semestre)
print("Altura: ", altura, "cm.")
print("Edad: ", edad, "años.")

# Se modifican los valores de las variables y se mandan a imprimir
altura = 1.67 #Para modificar solo se usa el mismo identificador y se le asigna un nuevo valor
edad = 19
print() #Salto de línea
print("Valores modificados:") #Para que imprima de nueva cuenta los valores modificados
print("Nombre:", nombre)
print("Semestre:", semestre)
print("Altura: ", altura, "cm.")
print("Edad: ", edad, "años.")

# En Python, las variables son dinámicas, por lo que pueden almacenar otro tipo de dato en cualquier momento
edad = "diecinueve"      # edad antes tenía el valor de 31 (Int). Edad cambió de tipo de dato, cosa que en c o c++ no era posible a menos que se declare otra dirección de memoria
print()
print("Edad (con otro tipo de dato):", edad)

# Reglas para los nombres de las variables en Python:

# - Utilizar únicamente letras (mayúsculas o minúsculas), números y el guion bajo. No se puede declarar una variable de nombre 1edad (es este caso es mejor edad1)
# - La variable no puede iniciar con números. No se puede declarar una variable de nombre 1edad.
# - No se pueden utilizar palabras reservadas, ejemplos: if, else, True, class para una variables. No es lo mismo variable "class" a variable "clas". El primero es el erroneo
# - Es sensible a mayúsculas y minúsculas. Por ejemplo, las palabras "Hola", "hola" y "HOLA" son consideradas diferentes.

# Buenas prácticas

# - Utilizar minúsculas para las palabras.
# - Separar las palabras con el guion bajo. Ejemplo: Variable_entera = 1
# - Utilizar nombres descriptivos de acuerdo a su uso. Por ejemplo: edad, en lugar de e.

# Ejemplos correctos y con buenas prácticas
fecha_nacimiento = "18 de octubre del 2005"
clase = "Estructuras de Datos"
horas_estudio = 8
nombre = "Yamileth"
es_estudiante = True

# Ejemplos incorrectos (líneas comentadas porque marcan error) o de malas prácticas

f = "1 de enero del 2000 (mala práctica)"
fechanacimiento = "1 de enero del 2000 (mala práctica)"
# class = "Estructuras de Datos"
# 8horas_estudio = 8
Nombre = "Y a m m"
NOMBRE = "YAMM"


# Notar que las variables 'nombre', 'Nombre' y 'NOMBRE', son distintas.

print()
print("Las variables son sensibles a mayúsculas y minúsculas:")
print("Variable nombre:", nombre)
print("Variable Nombre:", Nombre)
print("Variable NOMBRE:", NOMBRE)

