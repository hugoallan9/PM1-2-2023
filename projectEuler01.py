"""
If we list all the natural numbers below that are multiples of or , we get and . The sum of these multiples is
Find the sum of all the multiples of
or below 100.
https://projecteuler.net/problem=1
"""

n = 1000
suma = 0
for x in range(1,n):
    #Acá reviso si el número es múltiplo de 3
    if x % 3 ==0:
        suma = suma + x
    elif x % 5 ==0:
        suma = suma + x
print(suma)

