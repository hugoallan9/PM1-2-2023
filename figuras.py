'''
Este programa imprime un rectángulo de 10x5 y un cuadrado de 3x3.
@Autor: Hugo García
@Versión: 1.0
@Fecha: 08/08/2023
'''

baseRectangulo = '{figura:*^10}'.format(figura = "*" ) + "\n"
alturaRectangulo = '{figura:<9}'.format(figura = "*" ) + "*" "\n"
rectangulo = baseRectangulo + 3*alturaRectangulo + baseRectangulo
print(rectangulo)

