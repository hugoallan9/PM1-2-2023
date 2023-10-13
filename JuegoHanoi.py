from Poste import Poste
from Disco import Disco

posteA = Poste("A")
posteB = Poste("B")
posteC = Poste("C")
disco1 = Disco(1)
disco2 = Disco(2)
disco3 = Disco(3)
disco4 = Disco(4)

#Asignar todos los discos al poste A.
posteA.insertar(disco4)
posteA.insertar(disco3)
posteA.insertar(disco2)
posteA.insertar(disco1)

#En qué poste está el disco 1.
print("El disco 1 está en el poste", disco1.poste)
#Mover el disco 1 al poste C.
posteC.insertar(posteA.sacar())
#Imprimir en que poste está el disco 1
print("El disco 1 está en el poste", disco1.poste)
#Imprimir todos los discos que están en el poste 1
for disco in posteA.discos:
    print(disco.getRadio())

