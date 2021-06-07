# En este archivo estaran todas nuestras vistas de la aplicacion, dandole funcionalidad a la misma
# Deberia ser capaz de mostrar las siguientes ventanas:
# 1) Vista Principal
# 2) Registro de Despacho
# 3) Plataforma Transportistas

from listado import *
from tkinter import *
from tkinter import ttk
from despacho import *
from datetime import date
from datetime import datetime

# Variables
listadoDespachos= Listado()




# --------------------------------------------------------------------> Funciones <---------------------------------------------------------------------------------------------------------

def buscarElemento(): #Busca un elemento determinado y lo muestra en la tabla
    registros = tree.get_children()
    for elemnto in registros:
        tree.delete(elemnto)

    for despacho in listadoDespachos.getLista():
        if despacho.getCliente().getRut()==eBuscarRut.get():
            tree.insert("",END,text=despacho.getCliente().getNombre(),values=(despacho.getCliente().getDireccion(),despacho.getCliente().getRut(),despacho.getProducto().getDescripcion(),despacho.getTransporte().getTipo(),despacho.getDestinatario().getNombre(),despacho.getDestinatario().getDireccionEntrega(),despacho.getFecha(),despacho.verificarEntrega()))


def eliminarElemento(): # Elimina el elemnto que seleccione el usuario en la Tabla
    for despacho in listadoDespachos.getLista():
        data = seleccionarElemento()
        if despacho.getCliente().getRut()==data:
            listadoDespachos.eliminarDespacho(despacho)
            mostrarTodo()

def seleccionarElemento(): # Me permite Registrar una Seleccion
    item = tree.item(tree.selection())['values'][1]
    return item


def mostrarTodo(): # Muestra los valores de cada despacho en una tabla
    registros = tree.get_children()
    for elemnto in registros:
        tree.delete(elemnto)
    for despacho in listadoDespachos.getLista():
        tree.insert("",END,text=despacho.getCliente().getNombre(),values=(despacho.getCliente().getDireccion(),despacho.getCliente().getRut(),despacho.getProducto().getDescripcion(),despacho.getTransporte().getTipo(),despacho.getDestinatario().getNombre(),despacho.getDestinatario().getDireccionEntrega(),despacho.getFecha(),despacho.verificarEntrega()))

def current_date_format(date): # Me entrega la fecha actual
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = "{} de {} del {}".format(day, month, year)

    return messsage

def abrirVistaDespacho(): # Abre el formulario para agregar un nuevo despacho
    def capturarValores(): # Captura los valores de los entry y crea un despacho para agregarlo a la lista de despachos
        now= datetime.now()
        fechaActual = current_date_format(now)
        despacho = Despacho()
        despacho.setFecha(fechaActual)
        despacho.getCliente().setNombre(eNombreCliente.get())
        despacho.getCliente().setRut(eRut.get())
        despacho.getCliente().setDireccion(eDireccion.get())
        despacho.getProducto().setDescripcion(eDescripcion.get())
        despacho.getProducto().setTamaño(int(eTamaño.get()))
        despacho.getDestinatario().setNombre(eNombreDes.get())
        despacho.getDestinatario().setDireccionEntrega(eDireccionDes.get())
        despacho.getDestinatario().setNumeroTelefono(eNumeroDes.get())
        despacho.asignaBodega()
        despacho.asignaTransporte()
        listadoDespachos.agregarDespacho(despacho)
        mostrarTodo()
        print(listadoDespachos.mostrarDespachos()) 

    vistaformulario = Toplevel(vistaPrincipal) # Crea la Sub ventana "Registro de Despacho"
    vistaformulario.title('Registro de Despacho')
    vistaformulario.geometry('330x460')
    
    # REGISTRO DE CLIENTE

    labelframe1 = ttk.LabelFrame(vistaformulario, text="Registro de Cliente")
    labelframe1.grid(column=0,row=0,padx=5,pady=5)
    label1 = ttk.Label(labelframe1, text="Nombre Cliente:")
    label1.grid(column=0,row=0,padx=4,pady=4)
    eNombreCliente = Entry(labelframe1)
    eNombreCliente.grid(column=1,row=0,padx=4,pady=4)

    label2 = ttk.Label(labelframe1, text="Rut:")
    label2.grid(column=0,row=1,padx=4,pady=4)
    eRut= Entry(labelframe1)
    eRut.grid(column=1,row=1,padx=4,pady=4)

    label3 = ttk.Label(labelframe1, text="Direccion:")
    label3.grid(column=0,row=2,padx=4,pady=4)
    eDireccion = Entry(labelframe1)
    eDireccion.grid(column=1,row=2,padx=4,pady=4)

    label4 = ttk.Label(labelframe1, text="Mail:")
    label4.grid(column=0,row=3,padx=4,pady=4)
    eMail = Entry(labelframe1)
    eMail.grid(column=1,row=3,padx=4,pady=4)

    label5 = ttk.Label(labelframe1, text="Numero:")
    label5.grid(column=0,row=4,padx=4,pady=4)
    eNumero = Entry(labelframe1)
    eNumero.grid(column=1,row=4,padx=4,pady=4)


    # REGISTRO DE PRODUCTO
    labelframe2 = ttk.LabelFrame(vistaformulario, text="Registro de Producto")
    labelframe2.grid(column=0,row=1,padx=5,pady=7)

    label6 = ttk.Label(labelframe2, text="Descripcion:")
    label6.grid(column=0,row=0,padx=4,pady=4)
    eDescripcion= Entry(labelframe2)
    eDescripcion.grid(column=1,row=0,padx=4,pady=4)

    label7 = ttk.Label(labelframe2, text="Tamaño(mt2):")
    label7.grid(column=0,row=1,padx=4,pady=4)
    eTamaño= Entry(labelframe2)
    eTamaño.grid(column=1,row=1,padx=4,pady=4)

    # REGISTRO DE DESTINATARIO
    labelframe3 = ttk.LabelFrame(vistaformulario, text="Registro de Destinatario")
    labelframe3.grid(column=0,row=2,padx=5,pady=7)

    label8 = ttk.Label(labelframe3, text="Nombre Cliente:")
    label8.grid(column=0,row=0,padx=4,pady=4)
    eNombreDes = Entry(labelframe3)
    eNombreDes.grid(column=1,row=0,padx=4,pady=4)

    label9 = ttk.Label(labelframe3, text="Direccion:")
    label9.grid(column=0,row=1,padx=4,pady=4)
    eDireccionDes= Entry(labelframe3)
    eDireccionDes.grid(column=1,row=1,padx=4,pady=4)

    label10 = ttk.Label(labelframe3, text="Numero:")
    label10.grid(column=0,row=2,padx=4,pady=4)
    eNumeroDes = Entry(labelframe3)
    eNumeroDes.grid(column=1,row=2,padx=4,pady=4)

    btnAgregar = ttk.Button(vistaformulario, text="Agregar",command=capturarValores)
    btnAgregar.grid(column=1,row=3)
    

def creaVistaTransportista():

    def seleccionarElementoT(): # Me permite Registrar una Seleccion
        item1 = tree1.item(tree1.selection())['values'][1]
        return item1

    def mostrarTodoT(): # Muestra los valores de cada despacho en una tabla
        registros = tree1.get_children()
        for elemnto in registros:
            tree1.delete(elemnto)
        for despacho in listadoDespachos.getLista():
            tree1.insert("",END,text=despacho.getCliente().getNombre(),values=(despacho.getCliente().getDireccion(),despacho.getCliente().getRut(),despacho.getProducto().getDescripcion(),despacho.getTransporte().getTipo(),despacho.getDestinatario().getNombre(),despacho.getDestinatario().getDireccionEntrega(),despacho.getFecha(),despacho.verificarEntrega()))

    def soloMoto(): # Mustra solo los despachos en moto
        registros = tree1.get_children()
        for elemnto in registros:
            tree1.delete(elemnto)
        for despacho in listadoDespachos.getLista():
            if despacho.getTransporte().getTipo()=="moto":
                tree1.insert("",END,text=despacho.getCliente().getNombre(),values=(despacho.getCliente().getDireccion(),despacho.getCliente().getRut(),despacho.getProducto().getDescripcion(),despacho.getTransporte().getTipo(),despacho.getDestinatario().getNombre(),despacho.getDestinatario().getDireccionEntrega(),despacho.getFecha(),despacho.verificarEntrega()))

    def soloCamioneta(): # Muestra solo los despachos en Camioneta
        registros = tree1.get_children()
        for elemnto in registros:
            tree1.delete(elemnto)
        for despacho in listadoDespachos.getLista():
            if despacho.getTransporte().getTipo()=="camioneta":
                tree1.insert("",END,text=despacho.getCliente().getNombre(),values=(despacho.getCliente().getDireccion(),despacho.getCliente().getRut(),despacho.getProducto().getDescripcion(),despacho.getTransporte().getTipo(),despacho.getDestinatario().getNombre(),despacho.getDestinatario().getDireccionEntrega(),despacho.getFecha(),despacho.verificarEntrega()))

    def soloCamion(): # Muestra solo los despachos en camion
        registros = tree1.get_children()
        for elemnto in registros:
            tree1.delete(elemnto)
        for despacho in listadoDespachos.getLista():
            if despacho.getTransporte().getTipo()=="camion":
                tree1.insert("",END,text=despacho.getCliente().getNombre(),values=(despacho.getCliente().getDireccion(),despacho.getCliente().getRut(),despacho.getProducto().getDescripcion(),despacho.getTransporte().getTipo(),despacho.getDestinatario().getNombre(),despacho.getDestinatario().getDireccionEntrega(),despacho.getFecha(),despacho.verificarEntrega()))

    def buscarElementoT():
        registros = tree1.get_children()
        for elemnto in registros:
            tree1.delete(elemnto)

        for despacho in listadoDespachos.getLista():
            if despacho.getCliente().getRut()==eBuscaRutT.get():
                tree1.insert("",END,text=despacho.getCliente().getNombre(),values=(despacho.getCliente().getDireccion(),despacho.getCliente().getRut(),despacho.getProducto().getDescripcion(),despacho.getTransporte().getTipo(),despacho.getDestinatario().getNombre(),despacho.getDestinatario().getDireccionEntrega(),despacho.getFecha(),despacho.verificarEntrega()))

    def despachaElemento():
        data = seleccionarElementoT()
        for despacho in listadoDespachos.getLista():
            if despacho.getCliente().getRut()==data:
                despacho.setEntregado(True)
                mostrarTodoT()
                print(listadoDespachos.mostrarDespachos())

    vTrans = Toplevel(vistaPrincipal) # Crea la Sub ventana "Transportistas"
    vTrans.title('Vista Transportista')
    vTrans.geometry('1270x720')
    vTrans.config(bg='#ADD8E6')

    labelframe1 = ttk.LabelFrame(vTrans, text="Seleccione su tipo de Transporte")
    labelframe1.grid(column=0,row=0,padx=5,pady=5)
    Button(labelframe1, text="Moto",command=soloMoto).grid(column=0,row=0,padx=7,pady=4)
    Button(labelframe1, text="Camioneta",command=soloCamioneta).grid(column=1,row=0,padx=7,pady=4)
    Button(labelframe1, text="Camion",command=soloCamion).grid(column=2,row=0,padx=7,pady=4)

    labelframe2 = ttk.LabelFrame(vTrans, text="Lista de Despachos")
    labelframe2.grid(column=0,row=2,padx=5,pady=9)
    tree1=ttk.Treeview(labelframe2, height=10,columns=('#0','#1','#2','#3','#4','#5','#6','#7','#8')) # Creacion de una Tabla
    tree1.grid(column=0,row=0)
    tree1.column('#0', width=150)     # Configuraciones de la Tabla
    tree1.column('#1', width=150)
    tree1.column('#2', width=150)
    tree1.column('#3', width=150)
    tree1.column('#4', width=150)
    tree1.column('#5', width=150)
    tree1.column('#6', width=150)
    tree1.column('#7', width=150)
    tree1.column('#8', width=150)

    tree1.heading('#0',text='Nombre Cliente', anchor='c')
    tree1.heading('#1',text='Direccion Cliente', anchor='c')
    tree1.heading('#2',text='Rut Cliente', anchor='c')
    tree1.heading('#3',text='Producto', anchor='c')
    tree1.heading('#4',text='Transporte', anchor='c')
    tree1.heading('#5',text='Nombre Destinatario', anchor='c')
    tree1.heading('#6',text='Direccion Destinatario', anchor='c')
    tree1.heading('#7',text='Fecha de Registro', anchor='c')
    tree1.heading('#8',text='Estado del Despacho', anchor='c')
    mostrarTodoT()


    labelframe3 = ttk.LabelFrame(vTrans, text="Seleccione una Accion")
    labelframe3.grid(column=0,row=3,padx=5,pady=9)
    Button(labelframe3, text="Despachado",command=despachaElemento).grid(column=0,row=0,padx=4,pady=4)
    Button(labelframe3, text="Buscar",command=buscarElementoT).grid(column=0,row=1,padx=4,pady=4)
    eBuscaRutT= Entry(labelframe3)
    eBuscaRutT.grid(column=1,row=1,padx=4,pady=4)
    Label(labelframe3, text="Ingrese un Rut").grid(column=2,row=1,padx=4,pady=4)

# ---------------------------------------------------------------------------------> Fin Funciones <--------------------------------------------------------------------------------------------------
    




# ---------------------------------------------------------------------------------> Vista principal - Configuracion de ventana <-----------------------------------------------------------------
vistaPrincipal = Tk() # Creacion de ventana principal
vistaPrincipal.title('Vista Principal') # Titulo de Ventana
vistaPrincipal.iconbitmap('imagenes/descarga.ico') # Icono de Ventana
vistaPrincipal.resizable() # Extender ventana a gusto
vistaPrincipal.geometry('1270x720') # Dimensiones de Ventana
vistaPrincipal.config(bg='#EFEFEF') # Color de Fondo
mensajeAd=Label(vistaPrincipal, text='Esta es la ventana principal, Cerrar esta ventana cerrara la aplicacion')
mensajeAd.pack()
Button(vistaPrincipal, text='Plataforma Transportistas',command=creaVistaTransportista).place(x=0,y=0)



# -------------------------------------------------------------------> Creacion de Frames para la VP <-------------------------------------------------------------------

# Frame Titulo
frameTitulo = Frame()
frameTitulo.pack()
frameTitulo.config(bg='#ADD8E6') # Color del frame
frameTitulo.config(width='880', height='170') # Dimensiones del frame
frameTitulo.config(bd=0) # Tamaño del Borde
frameTitulo.config(relief='raised') # Tipo de Relieve
imgTitulo = PhotoImage(file='imagenes/titulo.png')
Label(frameTitulo, image=imgTitulo).place(x=0,y=0)


# Frame Botones
frameBotones = Frame()
frameBotones.config(width='880',height='200',bd=0,relief='raised',bg='#ADD8E6')
imgFondob = PhotoImage(file='imagenes/fondob.png')
Label(frameBotones, image=imgFondob).place(x=0,y=0)
frameBotones.pack(pady=10)
imgbtnadd = PhotoImage(file='imagenes/btnagregar.png')
imgbtnbuscar = PhotoImage(file='imagenes/btnbuscar.png')
imgbtneliminar = PhotoImage(file='imagenes/btneliminar.png')
imgbtnmostrar = PhotoImage(file='imagenes/btnmostrar.png')

Button(frameBotones,image=imgbtnadd, command=abrirVistaDespacho).place(x=75,y=50)
Button(frameBotones,image=imgbtnbuscar, command=buscarElemento).place(x=275,y=50)
Button(frameBotones,image=imgbtneliminar, command=eliminarElemento).place(x=475,y=50)
Button(frameBotones,image=imgbtnmostrar,command=mostrarTodo).place(x=675,y=50)

eBuscarRut = Entry(frameBotones) # Entry para ingresar un rut con el cual buscar
eBuscarRut.place(x=277,y=150)
Label(frameBotones,text='ej: 23457468-5').place(x=300,y=175)


# Frame Despachos
frameDespachos = Frame()
frameDespachos.config(width='1400',height='780',bd=0,relief='raised',bg='#ADD8E6')
frameDespachos.pack(pady=10)

tree=ttk.Treeview(frameDespachos,height=10,columns=('#0','#1','#2','#3','#4','#5','#6','#7','#8')) # Creacion de una Tabla
tree.place(x=0,y=0)

tree.column('#0', width=150)     # Configuraciones de la Tabla
tree.column('#1', width=150)
tree.column('#2', width=150)
tree.column('#3', width=150)
tree.column('#4', width=150)
tree.column('#5', width=150)
tree.column('#6', width=150)
tree.column('#7', width=150)
tree.column('#8', width=150)

tree.heading('#0',text='Nombre Cliente', anchor='c')
tree.heading('#1',text='Direccion Cliente', anchor='c')
tree.heading('#2',text='Rut Cliente', anchor='c')
tree.heading('#3',text='Producto', anchor='c')
tree.heading('#4',text='Transporte', anchor='c')
tree.heading('#5',text='Nombre Destinatario', anchor='c')
tree.heading('#6',text='Direccion Destinatario', anchor='c')
tree.heading('#7',text='Fecha de Registro', anchor='c')
tree.heading('#8',text='Estado del Despacho', anchor='c')

  

#-------------------------------------------------------> Fin del GUI <---------------------------------------------------------------------------------

vistaPrincipal.mainloop() # Fin del gui
