print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 10 de diciembre de 24                                     * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Ej3_lenguaje_hacker_l33t_speak.py                                * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

'''
Lenguaje básico:
En el lenguaje básico se sustituye cada vocal por un número.
La A se convierte en un 4, la E en un 3, la I en un 1 y la O en un cero.
La letra U es una excepción, ya que no hay un número obvio, por lo que se sustituye por (_).

Lenguaje intermedio:
En el lenguaje intermedio también se sustituyen las consonantes por números o signos de puntuación.
Por ejemplo, la B se convierte en I3, la C en [, la D en ), la L en 1.
Revisa la "Leet speak alphabet" de la página anterior y toma la primera de las opciones para el lenguaje.
Nota que no hay caracteres acentuados, por lo no se deben de convertir.
Se debe mostrar el siguiente menú:
  ***  Ejercicio 3. Lenguaje hacker (l33t sp34k).  ***
1) Convertir un texto a lenguaje básico.
2) Convertir un texto a lenguaje intermedio.
0) Salir.
Cualquier otro caso -> Opción no válida.
Para ello:
a) Utilice la lógica adecuada para mostrar las conversiones. No utilice funciones como bin() o hex().
b) Utilice la lógica adecuada para convertir el texto al lenguaje hacker básico o intermedio, según sea el caso.
c) Se debe convertir los caracteres sin importar si son mayúsculas o minúsculas, 
sin modificar los caracteres que no se convirtieron. Ejemplos con el lenguaje básico: 
hola -> h0l4, Hola -> H0l4, HOLA -> H0L4.
'''
print("***  Ejercicio 3. Lenguaje hacker (l33t sp34k).  ***")


def menu():  # Función menú, se encarga de imprimir el menú
    print(" ")
    print("---------------------------------------- ")
    print("1) Convertir un texto a lenguaje básico.")
    print("2) Convertir un texto a lenguaje intermedio.")
    print("0) Salir.")


# Diccionario de los caracteres que se reemplazan en el nivel básico
diccionario_conversion_nivel_basico = {
    'a': '4',
    'A': '4',
    'e': '3',
    'E': '3',
    'i': '1',
    'o': '0',
    'O': '0',
    'u': '(_)',

    '0': 'o',
    '1': 'L',
    '2': 'R',
    '3': 'E',
    '4': 'A',
    '5': 'S',
    '6': 'p',
    '7': 'T',
    '8': 'B',
    '9': 'g'

}

# Diccionario de los caracteres que se reemplazarán en el nivel intermedio
diccionario_conversion_nivel_intermedio = {
    'a': '4',
    'A': '4',

    'b': 'l3',
    'B': 'l3',

    'c': '[',
    'C': '[',

    'd': ')',
    'D': ')',

    'e': '3',
    'E': '3',

    'f': '|=',
    'F': '|=',

    'g': '&',
    'G': '&',

    'h': '#',
    'H': '#',

    'i': '1',
    'I': '1',

    'j': ',_|',
    'J': ',_|',

    'k': '>|',
    'K': '>|',

    'l': '1',
    'L': '1',

    'm': '/\/\ ',
    'M': '/\/\ ',

    'n': '^/',
    'N': '^/',

    'o': '0',
    'O': '0',

    'p': '|*',
    'P': '|*',

    'q': '(_,)',
    'Q': '(_,)',

    'r': 'l2',
    'R': 'l2',

    's': '5',
    'S': '5',

    't': '7',
    'T': '7',

    'u': '(_)',
    'U': '(_)',

    'v': '\/',
    'V': '\/',

    'w': '\/\/',
    'W': '\/\/',

    'x': '><',
    'X': '><',

    'y': 'j',
    'Y': 'j',

    'z': '2',
    'Z': '2',

    '0': 'o',
    '1': 'L',
    '2': 'R',
    '3': 'E',
    '4': 'A',
    '5': 'S',
    '6': 'p',
    '7': 'T',
    '8': 'B',
    '9': 'g'

}


# Función para convertir el texto en lenguaje básico
def convertir_texto_basico(texto, diccionario_basico):
    texto_convertido = ""  # Texto_convertido inica como cadena vacía
    for caracter in texto:
        # Reemplaza el carácter si está en el diccionario, si no, queda igual
        texto_convertido += diccionario_basico.get(caracter, caracter)
    return texto_convertido


# Fución para convertir el texto a lenguaje intermedio
def convertir_texto_intermedio(texto, diccionario_intermedio):
    texto_convertido = ""  # Texto_convertido inica como cadena vacía
    for caracter in texto:
        # Reemplaza el carácter si está en el diccionario, si no, queda igual
        texto_convertido += diccionario_intermedio.get(caracter, caracter)
    return texto_convertido


def conversion(option):
    texto_original = input("Ingresa texto a convertir: ")  # El usuario ingresa el texto
    if option == 1:  # Llama a la fución que convierte el texto a básico
        texto_covertido = convertir_texto_basico(texto_original, diccionario_conversion_nivel_basico)
    elif option == 2:  # Llama a la función que convierte el texto a intermedio
        texto_covertido = convertir_texto_intermedio(texto_original, diccionario_conversion_nivel_intermedio)
    else:
        print("Opción no válida :(")
    return texto_covertido  # Retorna el texto convertido según la función


# Código nivel de módulo
flag = 0
while flag == 0:
    menu()
    option = int(input("Ingresa una opción: "))
    if option == 0:
        print("Saliendo...")
        flag = 1  # Rompe el ciclo
    else:
        print(f"Texto convertido : {conversion(option)}")
