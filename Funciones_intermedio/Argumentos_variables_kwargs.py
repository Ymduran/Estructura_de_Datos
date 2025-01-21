print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha:  21 de Enero del 2025                                     * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Argumentos variables kwargs                                       * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

def preferencias(tema:str, **kwargs):
    print(f"El tema es {tema}")
    for key, value in kwargs.items():
        print(f"Nombre: {key} prefiere {value}")


if __name__ == '__main__':
    preferencias("Comida", Rebecca="Mole", Juan="Tacos", Bryan="Tlayudas",Jamilet="Tamales" )