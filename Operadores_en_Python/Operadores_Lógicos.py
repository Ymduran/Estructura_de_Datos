print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 17 octubre del 2024                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Operadores Operadores lógicos                                    * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

variable_bool=input("1 ingrese si/no: ") #Se lee por teclado si o no
variable_bool=variable_bool.lower()== "si"
variable_bool2=input("2 ingrese si/no: ")
variable_bool2=variable_bool2.lower()== "si"
#lower convierte a minúscula  y despues se puede comparar dos cadenas
print(f"su respuesta 1 fue: {variable_bool}") #si las cadenas son iguales entonce simprime true si no pues false
print(f"su respuesta 2 fue: {variable_bool2}") #si las cadenas son iguales entonce simprime true si no pues false

print(f"ambas respuestas fueron si? {variable_bool and variable_bool2}")
print(f"alguna de las dos respuestas fueron si? {variable_bool or variable_bool2}")
print(f"La primer respuesta fue no? {not variable_bool}") #Negar la respuesta, es decir, "La primer respuesta fue no?" en caso de que sea true entonces lo ideal es imprimir que no fue no
print(f"La segunda respuesta fue no? {not variable_bool2}")