print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 02 de diciembre del 2024                                  * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Introducción a diccionarios                                      * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")
'''
Un diccionario es ordenado, según como se añade, a diferencia de las listas, este se añade como 
"par clave_valor", según le haya nombrado.
Para crear un diccionario, se hace con {}
'''
print("** Ejemplos de uso **  ")
# A cada elemento de la lista se le asigna una clave, las claves ya no son mutables, pero su valor si
#Se accede a cada elemento según su índice
diccionario_profesor = {'nombre': "Alberto", 'primer_apellido': "Martinez", 'edad':31,'correo':"alberto.mba@unsij.edu.mx", 'cubo':12}
diccionario_yamileth = {} #Diccionario vacío

#Para añadir elementos:
diccionario_yamileth['nombre'] = "Yamileth"
diccionario_yamileth['primer_apellido'] = "Durán"
diccionario_yamileth['grupo'] = 303
print(diccionario_yamileth)
print(diccionario_profesor)

#Para acceder hay dos distintas formas
#1)
nombre_alumno = diccionario_yamileth['nombre'] #Se le asigna a una variable
print(nombre_alumno)
#2)
apellido_alumno = diccionario_yamileth.get('primer_apellido')
print(apellido_alumno)

#Para modificar los elementos
diccionario_yamileth['nombre'] = "Lourdes"
diccionario_yamileth['grupo'] = 403
print(diccionario_yamileth)

diccionario_yamileth['segundo_apellido'] = "Breceda"
diccionario_yamileth['materia_favorita'] = "álgebra"
print(diccionario_yamileth)

#Para elimar el par clave_valor
del diccionario_yamileth['segundo_apellido']
print(diccionario_yamileth)
#Otra forma para eliminar
diccionario_yamileth.pop('grupo')
print(diccionario_yamileth)

#Se accede a cada par clave_valor
for clave,valor in diccionario_yamileth.items(): #. item para las claves
    print(f"clave:{clave} y valor:{valor}")

#si solo se quiere acceder al valor
for valor in diccionario_yamileth.values():  # . item para las claves
    print(f"valor:{valor}")

#Si solo se quiere acceder a la clave
for clave in diccionario_yamileth.keys():  # . item para las claves
    print(f"clave:{clave}")
print(" ")
#Combinación con tuplas
#Se puede usar un tupla como una clave
diccionario_egresado = {'nombre': "Químico", ('primer_apellido','segundo_apellido'): "rodriguez remirez", 'edad': 23 }
print(diccionario_egresado)
#Se accede a cada par clave_valor
for clave,valor in diccionario_egresado.items(): #. item para las claves
    print(f"clave:{clave} y valor:{valor}")

diccionario_informatica = {'grupo_303':{'no_alumnos':12,'no_materias':5, 'promedio_grupal':7.99}, 'grupo_503':{'no_alumnos':8,'no_materias':4, 'promedio_grupal':3.99}, 'grupo_703':{'no_alumnos':4,'no_materias':5, 'promedio_grupal':8.99}, 'grupo_903':{'no_alumnos':4,'no_materias':5, 'promedio_grupal':8.91}}
print(diccionario_informatica)
for grupo in enumerate(diccionario_informatica): #. item para las claves
    print(f"Grupo: {grupo}")

#Acceder a los valores
promedio_303 = diccionario_informatica['grupo_303']['promedio_grupal']
print(f"promedio 303 : {promedio_303}")
promedio_503 = diccionario_informatica['grupo_503']['promedio_grupal']
print(f"promedio 503 : {promedio_503}")
promedio_703 = diccionario_informatica['grupo_703']['promedio_grupal']
print(f"promedio 703 : {promedio_703}")
promedio_903 = diccionario_informatica['grupo_903']['promedio_grupal']
print(f"promedio 903 : {promedio_903}")



