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
