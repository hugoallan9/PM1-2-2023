"""
Este programa recibe de entrada números a, b, c y calcula las soluciones reales de la ecuación cuadrática
ax^2 + bx +c =0
@Author: Hugo García
@Fecha: 14/08/2023
@a Coeficiente del x^2
@b Coeficiente del x
@c El término independiente
"""
from math import sqrt
a = float(input("Ingrese el coeficiente del término cuadrático \n"))
b = float(input("Ingrese el coeficiente del término lineal \n"))
c = float(input("Ingrese el término independiente \n"))

discriminante = b**2 - 4*a*c

if discriminante <0:
    print("La ecuación no tienen soluciones reales")
else:
    x1 = (-b + sqrt(discriminante))/(2*a)
    x2 = (-b - sqrt(discriminante))/(2*a)
    print("Las soluciones son {x1:.2f} y {x2:.2f}".format(x1=x1, x2=x2))


