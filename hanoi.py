"""
Este programa implementa una simulación de las torres de Hanoi.
En esta primera versión, se hará de manera funcional.
@Author: Hugo García
"""
#Vamos a implementar una función recursiva para resolver las torres de Hanoi de n discos

def resolverHanoi(n, posteInicial, posteIntermedio, posteFinal):
    if n == 1:
        print("Mover disco" ,n, "del poste", posteInicial, "a", posteFinal)
    if n >1:
        #Acá está la parte recursiva.
        resolverHanoi(n-1, posteInicial, posteFinal ,posteIntermedio)
        print("Mover disco", n, "del poste", posteInicial, "a", posteFinal)
        resolverHanoi(n-1, posteIntermedio,  posteInicial, posteFinal)

resolverHanoi(3, "A", "B", "C")

