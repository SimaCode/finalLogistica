class Destinatario:

    def __init__(self):
        self.nombre = ""
        self.numeroTelefono = ""
        self.direccionEntrega = ""

    def setNombre(self, nombre):
        self.nombre = nombre

    def setNumeroTelefono(self, numeroTelefono):
        self.numeroTelefono = numeroTelefono

    def setDireccionEntrega(self, direccionEntrega):
        self.direccionEntrega = direccionEntrega

    def getNombre(self):
        return self.nombre

    def getNumeroTelefono(self):
        return self.numeroTelefono

    def getDireccionEntrega(self):
        return self.direccionEntrega

    def __str__(self):
        return self.nombre+" "+self.numeroTelefono+" "+self.direccionEntrega
