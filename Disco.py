
class Disco:
    def __init__(self, radio):
        self.radio = radio
        self.poste = None

    def setRadio(self, radio):
        self.radio = radio

    def getRadio(self):
        return self.radio

    def asociarPoste(self, poste):
        self.poste = poste
    def posteAsociado(self):
        return self.poste
