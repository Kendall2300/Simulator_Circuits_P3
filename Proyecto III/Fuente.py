class Fuente:
    def __init__(self, name, tension):
        
        self.name = name
        self.tension = tension

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name
    
    def setTension(self, tension):
        self.tension = tension

    def getTension(self):
        return self.tension
