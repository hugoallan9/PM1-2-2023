"""
https://projecteuler.net/problem=3
V1.0
"""
maximo = 2
for x in range(3,600851475143):
    #Buscando los divisores
    if 600851475143 % x == 0:
        #Revisando si el número es primo
        for y in range(3,x):
            if x % y == 0:
                break
            if y == x-1:
                maximo = x
print(maximo)



