

print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha:  18 de Enero del 2025                                     * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Argumentos por nombre                                            * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

def main() -> None:
    if __name__ == '__main__':
        nombre = "Yamileth"
        edad = 19
        matricula = 2103232005
        grupo = 303
        semestre = 3
        imprimir_alumno(nombre, edad, matricula, grupo, semestre)



def imprimir_alumno (nombre : str, edad: int, matricula: int, grupo: int, semeste: int) -> None:
    """
    Función que muestra en pantalla los datos personales del alumno
    :param nombre:
    :param edad:
    :param matricula:
    :param grupo:
    :param semeste:
    :return:
    """
    print("Datos del personales: ")
    print(f"Nombre: {nombre} ")
    print(f"Edad: {edad}")
    print(f"Matrícula:  {matricula}")
    print(f"Grupo:  {grupo}")
    print(f"Semestre: {semeste}")


main()