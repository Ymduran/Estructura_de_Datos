print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 17 octubre del 2024                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Sentencia if elif y else;                                        * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

'''
if condición : 
    #Código a ejecutar si
elif condición2 :
    #Código si ejecución 1 es falsa y condición dos es verdadera
elif condición3: 
    #Código si la condición 1 y la condición 2 son falsas y la tercera es verdadera
else :
    #Código si ninguna condición es verdadera
    
'''

'''
    La sentencia "elif" es como "si no, sí" adicional. Se utiliza junto con if y else para crear estructuras de decisión más complejas, es como el if else de c
'''
#PROBRAMA PARA DETERMINAR A QUÉ GRUPO DE EDAD PERTENECES
edad = int(input("ingrese edad: ")) # Se lee la edad por teclado
if edad<=14 : #Condición 1. Si la edad es menor o igual que 14, arroja un resultado true/false
    print(f" Ud tiene {edad}, pertenece a adolescentes ")  #Código a ejecutar si se cumple/ es verdadera la condición .
elif (edad>=15) and (edad<=25) : #Condición 2. Sí edad está entre 15 y 25, arroja resultado true/false
    print(f" Ud tiene {edad}, pertenece a jóvenes ") #Código a ejecutar sí se cumple/ es verdadera la condición 2.
elif (edad>=46) and (edad<=60): #Condición 3. Sí la edad está entre 46 y 60, arroja un resultado de true/false
    print(f" Ud tiene {edad}, pertenece a adultos maduros ") #Código a ejecutar si se cumple la condicón 3.
elif edad>60:
    print(f" Ud tiene {edad}, pertenece a adultos mayores ")