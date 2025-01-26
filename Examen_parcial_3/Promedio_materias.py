print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 24 de diciembre del 2025                                  * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Promedio Materias                                                * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")



def cadena_a_flotante(cadena):
    """
    Convierte una cadena a un número flotante (como la caliifcaci{on) si es válido, esto para la perte de validación de datos.
    
    :param cadena: Cadena a convertir
    :return: El número flotante o None de no ser válido
    
    """
    numero_puntos = cadena.count(".")
    
    revisar_cadena = cadena.replace(".", "").lstrip("-")
    if revisar_cadena.isnumeric() and numero_puntos in (0, 1):
        return float(cadena)
    else:
        return None




def registrar_materias(**kwargs):
    """
    Recibe materias con sus respectivos promedios y calcula el promedio general
    :param kwargs: Materias y sus promedios
    """
    print("** PROMEDIO **")
    
    promedio_general = sum(kwargs.values()) / len(kwargs)
    print(f"\nEl promedio general es: {promedio_general:.2f}")


if __name__ == '__main__':
    materias = {} 
    flag = 0
    
    
    print("Registro de materias y promedios")
    
    while flag == 0:
        materia = input("Introduce el nombre de la materia (o escribe 'terminar' para terminar): ")
        
        if materia.lower() == 'terminar':
            flag = 1
            break

        promedio_cadena = input(f"Introduce el promedio de {materia}: ")
        
        promedio = cadena_a_flotante(promedio_cadena) 
        
        
        while promedio is None:
            print("Introduce un promedio válido")
            promedio_cadena = input(f"Introduce el promedio de {materia}: ")
            promedio = cadena_a_flotante(promedio_cadena)

        materias[materia] = promedio

    if materias:
        registrar_materias(**materias)
    else:
        print("No se registraron materias :(")
