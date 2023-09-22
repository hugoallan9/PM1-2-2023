"""
https://projecteuler.net/problem=3
V1.0
"""
from math import sqrt
from math import ceil
from time import time

maximo = 7
inicio = time()
for x in range(10,(600851475143-1)//2):
    #Buscando los divisores
    if 600851475143 % x == 0:
        #Revisando si el número es primo
        for y in range(3,ceil(sqrt(x))):
            if x % y == 0:
                break
            if y == ceil(sqrt(x))-1:
                maximo = x
fin = time()
print("El tiempo de ejecución fue de", fin-inicio)
print(maximo)