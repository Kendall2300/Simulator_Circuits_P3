class Resistencia:

    def __init__(self, name, resistencia, tipo): 

        #Atributos de resistencia
        self.name = name #Nombre
        self.resistencia = resistencia #Valor de resistencia
        self.tipo = tipo #Tipo de resistencia (1 para serie 2 para paralelo)
        

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name
    
    def setResistencia(self, resistencia):
        self.resistencia = resistencia

    def getResistencia(self):
        return self.resistencia
    
    def setTipo(self, tipo):
        self.tipo = tipo

    def getTipo(self):
        return self.tipo
    
