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

edad = int(input("ingrese edad: "))
if edad<=14 :
    print(f" Ud tiene {edad}, pertenece a adolescentes ")
elif (edad>=15) and (edad<=25) :
    print(f" Ud tiene {edad}, pertenece a jóvenes ")
elif (edad>=46) and (edad<=60):
    print(f" Ud tiene {edad}, pertenece a adultos maduros ")
elif edad>60:
    print(f" Ud tiene {edad}, pertenece a adultos mayores ")
