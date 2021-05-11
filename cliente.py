class Cliente:

    def __init__(self):
        self.nombre = ""
        self.rut = ""
        self.direccion = ""

    def setNombre(self, nombre):
        self.nombre = nombre

    def setRut(self, rut):
        self.rut = rut

    def setDireccion(self, direccion):
        self.direccion = direccion

    def getNombre(self):
        return self.nombre

    def getRut(self):
        return self.rut

    def getDireccion(self):
        return self.direccion

    def __str__(self):
        return self.nombre+" "+self.rut+" "+self.direccion
