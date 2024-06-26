from Poste import Poste
from Disco import Disco

cantidadDiscos = int(input("Ingrese la cantidad de discos que desea\n"))

#Creamos los tres
posteA = Poste("A")
posteB = Poste("B")
posteC = Poste("C")

#Creamos los discos.
discos = []
for i in range(cantidadDiscos):
    discoTemporal = Disco(i+1)
    discos.append(discoTemporal)

#Insertamos todos los discos en el poste A
for i in range(1,cantidadDiscos+1):
    posteA.insertar(discos[-i])
def resolverHanoi(n, posteInicial, posteIntermedio, posteFinal):
    if n == 1:
        posteFinal.insertar(posteInicial.sacar())
        nombrePI = posteInicial.getNombre()
        nombrePIM = posteIntermedio.getNombre()
        nombrePF = posteFinal.getNombre()
        diccionarioNombres = {}
        diccionarioNombres[nombrePI] = posteInicial.pintaPoste(cantidadDiscos)
        diccionarioNombres[nombrePIM] = posteIntermedio.pintaPoste(cantidadDiscos)
        diccionarioNombres[nombrePF] = posteFinal.pintaPoste(cantidadDiscos)
        pintado = ""
        for i in range(cantidadDiscos+1):
            pintado = pintado + "{a:>12} {b:^12} {c:<12} \n".format(a = diccionarioNombres["A"][i],
                                                       b = diccionarioNombres["B"][i],
                                                        c = diccionarioNombres["C"][i])
        print(pintado)
    if n >1:
        #Acá está la parte recursiva.
        resolverHanoi(n-1, posteInicial, posteFinal ,posteIntermedio)
        posteFinal.insertar(posteInicial.sacar())
        nombrePI = posteInicial.getNombre()
        nombrePIM = posteIntermedio.getNombre()
        nombrePF = posteFinal.getNombre()
        diccionarioNombres = {}
        diccionarioNombres[nombrePI] = posteInicial.pintaPoste(cantidadDiscos)
        diccionarioNombres[nombrePIM] = posteIntermedio.pintaPoste(cantidadDiscos)
        diccionarioNombres[nombrePF] = posteFinal.pintaPoste(cantidadDiscos)
        pintado = ""
        for i in range(cantidadDiscos+1):
            pintado = pintado + "{a:>12} {b:^12} {c:<12} \n".format(a = diccionarioNombres["A"][i],
                                                       b = diccionarioNombres["B"][i],
                                                        c = diccionarioNombres["C"][i])
        print(pintado)
        resolverHanoi(n - 1, posteIntermedio, posteInicial, posteFinal)

resolverHanoi(cantidadDiscos, posteA, posteB, posteC)


