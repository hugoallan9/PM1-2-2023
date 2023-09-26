

class Poste:
    def __init__(self, nombre):
        self.nombre = nombre
        self.discos = []

    def getNombre(self):
        return self.nombre

    def isEmpty(self):
        respuesta = None
        if len(self.discos) == 0:
            respuesta = True
        else:
            respuesta = False
        return respuesta

    def insertar(self, disco):
        #Hay que validar, primero si el poste está vacío.
        if self.isEmpty() == True:
            self.discos.append(disco)
            disco.asociarPoste(self.nombre)
        else:
            #Validar que el disco que está en el top, sea de radio mayor que el que estoy intentando insertar.
            if self.discos[-1].getRadio() > disco.getRadio():
                #se hace la inserción
                self.discos.append(disco)
                disco.asociarPoste(self.nombre)
            else:
                print("La insersión no es posible debido a que el radio del disco es más grande que el que está en la cima")

    def sacar(self):
        #Hay que validar que el poste no esté vacío
        if self.isEmpty() == True:
            print("No hay discos en este poste")
        else:
            self.discos[-1].asociarPoste("")
            disco = self.discos[-1]
            self.discos.remove(disco)
            return disco

    def pintaPoste(self, espacioInicial = 0):
        for disco in self.discos:
            print("{disco:>{espacio}}".format(disco = disco.getRadio(), espacio = espacioInicial))