

class Producto:

    def __init__(self):
        
        self.tamaño = 0
        self.descripcion = ""

    

    def setTamaño(self, tamaño):
        self.tamaño = tamaño

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    
    def getTamaño(self):
        return self.tamaño

    def getDescripcion(self):
        return self.descripcion

    def __str__(self):
        return self.tamaño+" "+self.descripcion