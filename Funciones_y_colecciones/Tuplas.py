print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 19 noviembre del 24                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * Tuplas                                                           * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

'''
- Ordenada
- Inmutable
- Los elementos se encierran entre parentesis (a diferencia de las listas que se encierran en corchetes)

'''

print("** EJEMPLO DE TUPLA ** ")
fechas_cumple = ("12-19", "12-27","01-10","10-18","11-01","09-30","08-25","01-06","10-21","04-11","03-06", "08-02")
print(f"Las fechas de cumpleaños del grupo son: {fechas_cumple}")

for fecha in fechas_cumple:
    print(fecha)
print(" ")
pi_serie = (4,-4/3,4/5,-4/7,4/9,-4/11,4/13,-4/15,4/17,-4/19,4/21,-4/23)
print(f"El valor de pi considerando 3 elementos: {(sum(pi_serie[0:2])):.4f}")
print(f"El valor de pi considerando 5 elementos: {(sum(pi_serie[0:4])):.4f}")
print(f"El valor de pi considerando 8 elementos: {(sum(pi_serie[0:7])):.4f}")
print(f"El valor de pi considerando 10 elementos: {(sum(pi_serie[0:9])):.4f}")
print(f"El valor de pi considerando todos elementos: {(sum(pi_serie)):.4f}")
print(" ")
print(" ")



print("** EJEMPLOS CON COORDENADAS ** ")
punto1 = (1,0)
punto2 = (5,3)

print(f"coordenadas en tuplas: {punto1} y {punto2}")
#Desempaquetado de tuplas
x1, y1 = punto1
x2, y2 = punto2

#Expresión de la recta: y=mx+b
m = (y2-y1)/(x2-x1)
b = y1 - (m*x1)
print(f"el valor de la recta es: y = {m}x + {b}")




