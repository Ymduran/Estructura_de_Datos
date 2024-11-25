'''
Nombre:
Fecha:
Descripción:
Conversión de cadenas a int, float y boolean mediante la interacción con consola.
'''

# Comentar sobre las funciones anidadas.
print("****   Datos de los alumnos    *****")
nombre = input("Ingresa el nombre: ")
semestre = int(input("Ingresa el no. de semestre: "))
promedio = float(input("Ingresa el promedio: "))
es_mujer = input("¿Es mujer (Si/No)?: ")


# No es posible convertir directamente una cadena a un valor booleano.
# Por ello, utilizamos la misma variable, convertimos a  minúsculas y lo comparamos con la cadena "si".
es_mujer = es_mujer.lower() == "si"

# Se imprimen los datos del alumno.
# Comentar  qué es lo que realiza {promedio:.2f} probando con números diferentes.
print()
print(f"El alumno {nombre} cursa el {semestre} semestre con un promedio de {promedio:.2f}. Además, es mujer: {es_mujer}.")



'''
    Mis cursos
    Estructura de datos 2024
    Parcial 1
    Entrada de datos por consola en Python.

Entrada de datos por consola en Python.
Requisitos de finalización
Hecho: Ver Por hacer: Ir por toda la actividad hasta el final
Entrada de datos por consola en Python.

Tiempo estimado para completar la actividad: 50 minutos.

Esta es una lección que muestra la entrada de datos por consola para interacturar con el usuario con valores dinámicos. La entrada de datos por consola es una herramienta versátil y esencial, que permite crear programas interactivos, realizar pruebas y automatizar tareas.

Instrucciones:

    Revisa el código fuente proporcionado en la lección y reprodúcelo en PyCharm.
    Avanza en la lección y verifica el comportamiento del código agregado en cada caso.
    Realiza los comentarios que crea pertinentes a su propio código, de acuerdo a lo observado.

Entrada_conversiones_ejercicio.py

Escribe un programa de nombre Entrada_conversiones_ejercicio.py que realice lo siguiente:

a) Pida los datos de los profesores utilizando nombres de variables adecuadas, la función input y el casting:

        Nombre (cadena).
        No. de cubículo (int).
        Horas de que imparte clase a la semana (float con 3 decimales).
        ¿Tiene más de 5 años en la unsij? (booleno).

b) Muestre los datos en consola de forma adecuada.

Nota: Asuma que el usuario siempre va a ingresar números cuando se requiera. 

'''