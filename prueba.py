
from despacho import *
from listado import *



# Creo Despachos
d1 = Despacho()
d2 = Despacho()
d3 = Despacho()

# Le doy valor a sus Atributos

d1.getCliente().setNombre('Mauro Hernandez')
d1.getCliente().setRut('20.426.307-8')
d1.getCliente().setDireccion('Exposicion 1478')


d1.getProducto().setDescripcion('Celular')
d1.getProducto().setTamaño(1)

d1.getDestinatario().setNombre('Jose')
d1.getDestinatario().setDireccionEntrega('Calilas 1312')
d1.setFecha('12/5/2021')
d1.verificarEntrega()
d1.asignaTransporte()
d1.asignaBodega()


#print(d1.mostrarInfo())
#print(d1.getTransporte().getTipo())
lista=Listado()
lista.agregarDespacho(d1)
lista.agregarDespacho(d2)
print(lista.mostrarDespachos())


lista.despacharProducto(d1)

print("xxxxxxxxxxxxxxxxxxxxxxxx")
print(lista.mostrarDespachos())

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")



lista.eliminaEntregados()
print(lista.mostrarDespachos())


# tkinter cosas
t1 = Toplevel(vistaPrincipal)
t1.title('Registro de Despacho')
label2 = Label(t1, text='Esta es la ventana de Registro de Despacho')
label2.pack()





