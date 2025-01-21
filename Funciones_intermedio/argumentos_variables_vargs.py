print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha:  21 de Enero del 2025                                     * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Argumentos variables vargs                                       * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")



def colores_favoritos(persona:str, *vargs) -> None:
    """

    :param persona:
    :param vargs:
    :return:
    """
    print(f"{persona}: {vargs}")



#Argumentos variables
if __name__ == '__main__':
    colores_favoritos("Jenifer", "Morado","Negro","Blanco","Rosa")
    colores_favoritos("Addi","Azul","Blanco","Negro","Rojo")
    colores_favoritos("yamileth", "Lila")


def sumar(*vargs):
    resultado = 0
    for i in  vargs:
        resultado += i
    return resultado



res= sumar(5,3,4,1,1,1)
print(res)



