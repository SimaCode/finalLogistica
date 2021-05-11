# Importo los Modulos que Utiliza la Clase Despacho

from bodega import *
from producto import *
from destinatario import *
from transporte import *
from cliente import *







class Despacho:

    def __init__(self):
        self.cliente = Cliente()
        self.producto = Producto()
        self.bodega = Bodega()
        self.transporte = Transporte()
        self.destinatario = Destinatario()
        self.fecha = ""
        self.entregado = False




    # Metodos
        
    # Asigna el Tipo de Transporte según el Tamaño del Producto
    def asignaTransporte(self):
        if self.producto.getTamaño() <= 2:
            self.transporte.setTipo("moto")

        if self.producto.getTamaño() > 2 and self.producto.getTamaño() < 5:
             self.transporte.setTipo("camioneta")

        if self.producto.getTamaño() > 4:
             self.transporte.setTipo("camion")

    # Asigna la Bodega donde se Guardara el Producto según su Tamaño
    def asignaBodega(self):
        if self.producto.getTamaño() <= 2:
            self.bodega.setNumeroBodega("1")

        if self.producto.getTamaño() > 2 and self.producto.getTamaño() < 5:
            self.bodega.setNumeroBodega("2")

        if self.producto.getTamaño() > 4:
            self.bodega.setNumeroBodega("3")
    
    # Verifica si el Despacho ha sido Entregado o no
    def verificarEntrega(self):
        if self.entregado == True:
            return ("El producto ha sido entregado")
        if self.entregado == False:
            return ("El producto no ha sido entregado")

    
    # Muestra la informacion del Despacho
    def mostrarInfo(self):
        informacion="Nombre Cliente: " + self.cliente.getNombre() +" Rut Cliente: " + self.cliente.getRut() + " Producto: " + self.producto.getDescripcion() + " Transporte: " + self.transporte.getTipo() + " Numero Bodega: "+ self.bodega.getNumeroBodega()+  " Nombre Destinatario: " + self.destinatario.getNombre() + " Direccion dest: " + self.destinatario.getDireccionEntrega() + " Fecha de Registro: " + self.fecha + " Estado del Despacho: " + self.verificarEntrega()
        return informacion





    # Getters
    def getCliente(self):
        return self.cliente
    def getProducto(self):
        return self.producto
    def getDestinatario(self):
        return self.destinatario
    def getTransporte(self):
        return self.transporte
    def getFecha(self):
        return self.fecha
    def getEntregado(self):
        return self.entregado

    # Setters
    def setEntregado(self,entregado):
        self.entregado = entregado
    def setCliente(self, cliente):
        self.cliente = cliente
    def setDestinatario(self, destinatario):
        self.destinatario = destinatario
    def setProducto(self, producto):
        self.producto = producto
    def setTransporte(self, transporte):
        self.transporte = transporte
    def setBodega(self, bodega):
        self.bodega = bodega
    def setFecha(self, fecha):
        self.fecha = fecha
