'''
Su objetivo en esta kata es implementar
 una función de diferencia, que resta una lista de otra y devuelve el resultado.
Debe eliminar todos los valores de la lista a, que están presentes en la lista
bmanteniendo su orden.

Si un valor está presente en b, todos sus sucesos deben ser retirados de la otra:
'''

primera_lista_numeros = (1,10,31,40,5.2,6.8,7.2,18,9.9)
count = 0
for i in primera_lista_numeros:
    print(f"{count}) {i}")
    count += 1


elemento_a_eliminar = int(input("Ingrese el índice del elemento a eliminar: "))
primera_lista_numeros.pop(elemento_a_eliminar)
