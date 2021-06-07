class Transporte:

    def __init__(self):
        self.tipo = ""


    def setTipo(self, tipo):
        self.tipo = tipo

    def getTipo(self):
        return self.tipo

    def __str__(self):
        return self.tipo