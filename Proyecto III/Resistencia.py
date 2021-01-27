class Resistencia:

    def __init__(self, name, resistencia):
        
        self.name = name
        self.resistencia = resistencia

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name
    
    def setResistencia(self, resistencia):
        self.resistencia = resistencia

    def getResistencia(self):
        return self.resistencia
