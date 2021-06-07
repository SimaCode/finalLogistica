# ---------------------- Importaciones -------------------------------------------

from listado import *
from tkinter import *
from tkinter import ttk
from tkinter import font
from despacho import *
from datetime import date
from datetime import datetime


# ----------------------------- Variables Globales --------------------------------------

listadoDespachos= Listado()

def current_date_format(date): # Me entrega la fecha actual
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = "{} de {} del {}".format(day, month, year)

    return messsage

#---------------------------------------------------------------------------------------------------------- Inicio de la Vista del Administrador --------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



def creaVistaAd(): # Crea la vista del administrador, contiene sus propias Funciones
    vAd = Toplevel(root)
    vAd.geometry("1152x700")
    vAd.resizable(0,0)


    def buscarElemento(): #Busca un elemento determinado y lo muestra en la tabla
        registros = tree.get_children()
        for elemento in registros:
            tree.delete(elemento)

        for despacho in listadoDespachos.getLista():
            if despacho.getCliente().getRut()==buscadorRut.get():
                tree.insert("",END,text=despacho.getCliente().getNombre(),values=(despacho.getCliente().getDireccion(),despacho.getCliente().getRut(),despacho.getProducto().getDescripcion(),despacho.getTransporte().getTipo(),despacho.getDestinatario().getNombre(),despacho.getDestinatario().getDireccionEntrega(),despacho.getFecha(),despacho.verificarEntrega()))


    def mostrarTodo(): # Muestra los valores de cada despacho en una tabla
        registros = tree.get_children()
        for elemnto in registros:
            tree.delete(elemnto)
        #for despacho in listadoDespachos.getLista():
                #tree.insert("",END,text=despacho.getCliente().getNombre(),values=(despacho.getCliente().getDireccion(),despacho.getCliente().getRut(),despacho.getProducto().getDescripcion(),despacho.getTransporte().getTipo(),despacho.getDestinatario().getNombre(),despacho.getDestinatario().getDireccionEntrega(),despacho.getFecha(),despacho.verificarEntrega()))
                

        if opcion == 1:
            for despacho in listadoDespachos.getLista():
                tree.insert("",END,text=despacho.getCliente().getNombre(),values=(despacho.getCliente().getDireccion(),despacho.getCliente().getRut(),despacho.getProducto().getDescripcion(),despacho.getTransporte().getTipo(),despacho.getDestinatario().getNombre(),despacho.getDestinatario().getDireccionEntrega(),despacho.getFecha(),despacho.verificarEntrega()))

        elif opcion == 2:
            for despacho in listadoDespachos.getLista():
                if despacho.getTransporte().getTipo() == "camioneta":
                    tree.insert("",END,text=despacho.getCliente().getNombre(),values=(despacho.getCliente().getDireccion(),despacho.getCliente().getRut(),despacho.getProducto().getDescripcion(),despacho.getTransporte().getTipo(),despacho.getDestinatario().getNombre(),despacho.getDestinatario().getDireccionEntrega(),despacho.getFecha(),despacho.verificarEntrega()))
        elif opcion == 3:
            for despacho in listadoDespachos.getLista():
                if despacho.getTransporte().getTipo() == "camion":
                    tree.insert("",END,text=despacho.getCliente().getNombre(),values=(despacho.getCliente().getDireccion(),despacho.getCliente().getRut(),despacho.getProducto().getDescripcion(),despacho.getTransporte().getTipo(),despacho.getDestinatario().getNombre(),despacho.getDestinatario().getDireccionEntrega(),despacho.getFecha(),despacho.verificarEntrega()))
        elif opcion == 4:
            for despacho in listadoDespachos.getLista():
                if despacho.getTransporte().getTipo() == "moto":
                    tree.insert("",END,text=despacho.getCliente().getNombre(),values=(despacho.getCliente().getDireccion(),despacho.getCliente().getRut(),despacho.getProducto().getDescripcion(),despacho.getTransporte().getTipo(),despacho.getDestinatario().getNombre(),despacho.getDestinatario().getDireccionEntrega(),despacho.getFecha(),despacho.verificarEntrega()))
        else:
             for despacho in listadoDespachos.getLista():
                tree.insert("",END,text=despacho.getCliente().getNombre(),values=(despacho.getCliente().getDireccion(),despacho.getCliente().getRut(),despacho.getProducto().getDescripcion(),despacho.getTransporte().getTipo(),despacho.getDestinatario().getNombre(),despacho.getDestinatario().getDireccionEntrega(),despacho.getFecha(),despacho.verificarEntrega()))
                


    def seleccionarElemento(): # Me permite Registrar una Seleccion en la tabla
        item = tree.item(tree.selection())['values'][1]
        return item


    def eliminarElemento(): # Elimina el elemnto que seleccione el usuario en la Tabla
        for despacho in listadoDespachos.getLista():
            data = seleccionarElemento()
            if despacho.getCliente().getRut()==data:
                listadoDespachos.eliminarDespacho(despacho)
                mostrarTodo()




    #------------------------------------------------------------------------------------- Inicio de la Vista del Formulario --------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    
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
            vistaformulario.destroy() 

        vistaformulario = Toplevel(vAd) # Crea la Sub ventana "Registro de Despacho"
        vistaformulario.title('Registro de Despacho')
        vistaformulario.geometry('330x460')
        vistaformulario.config(bg="#649FB1")
        vistaformulario.resizable(0,0)
        
        # REGISTRO DE CLIENTE 

        labelframe1 = ttk.LabelFrame(vistaformulario, text="Registro de Cliente")
        labelframe1.grid(column=0,row=0,padx=5,pady=5)
        label1 = ttk.Label(labelframe1, text="Nombre Cliente:") 
        label1.grid(column=0,row=0,padx=4,pady=4)
        eNombreCliente = Entry(labelframe1) # Entry de Nombre Cliente
        eNombreCliente.grid(column=1,row=0,padx=4,pady=4)

        label2 = ttk.Label(labelframe1, text="Rut:")
        label2.grid(column=0,row=1,padx=4,pady=4)
        eRut= Entry(labelframe1)
        eRut.grid(column=1,row=1,padx=4,pady=4)

        label3 = ttk.Label(labelframe1, text="Direccion:")
        label3.grid(column=0,row=2,padx=4,pady=4)
        eDireccion = Entry(labelframe1)  # Entry de Direccion Cliente 
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
        #--------------------------------------------------------------------------- Fin de la Vista de Formulario ---------------------------------------------------------------------------------------------




    #  ------------------------- Frame titulo ----------------------------
    ft = Frame(vAd)
    ft.config(bg="#7264B1",width=1152,height=78)
    ft.pack()
    ft.pack_propagate(False)

    imgTitulo = PhotoImage(file='imagenes/adpeque.png', master=ft)
    lbltit = Label(ft,image=imgTitulo, bg="#7264B1")
    lbltit.image = imgTitulo
    lbltit.pack()
    
    # --------------------- Frame contenido ------------------------------
    fc = Frame(vAd)
    fc.config(bg="#649FB1",width=1152,height=622)
    fc.pack()
    fc.pack_propagate(False)
    imgFondo = PhotoImage(file='imagenes/fondocielo.png', master = fc)
    lblFondo = Label(fc, image= imgFondo)
    lblFondo.image = imgFondo
    lblFondo.place(x = 0, y = 0, relwidth = 1, relheight = 1)



    

    # Boton Agregar
    imgBtnAdd = PhotoImage(file='imagenes/btnagregar.png', master=fc) # Para que se muetre una imagen dentro de una subventana debo poner el parametro "master=lugar donde ira la imagen" dentro del metodo PhotoImage 
    labelAdd = Button(fc, image=imgBtnAdd,bd=0,command=abrirVistaDespacho)
    labelAdd.image = imgBtnAdd # Luego de cargar el label con una imagen debo volver a referenciarlo como imagen y listo
    labelAdd.place(x=85,y=15)

    # Boton Buscar
    imgBtnSearch = PhotoImage(file='imagenes/btnbuscar.png',master=fc)
    labelSearch = Button(fc, image=imgBtnSearch,bd=0,command=buscarElemento)
    labelSearch.image = imgBtnSearch
    labelSearch.place(x=240,y=15)

    buscadorRut = Entry(fc) # Entry para que ingresen un rut buscador
    buscadorRut.place(x=240 , y=100)
    Font_tuple3 = ("Dungeon", 13, "normal")
    lbBuscar = Label(fc,text="Ingrese un rut ej: 20734727-2",font= Font_tuple3, bg="#1E92DA")
    lbBuscar.place( x =240, y =115 )
    
    # Boton Eliminar
    imgBtnElimina = PhotoImage(file='imagenes/btneliminar.png',master=fc)
    labelElimina = Button(fc, image=imgBtnElimina,bd=0,command=eliminarElemento)
    labelElimina.image = imgBtnElimina
    labelElimina.place(x=395,y=15)
    
    # Boton Mostrar Todo
    imgBtnMostrar = PhotoImage(file='imagenes/btnmostrar.png',master=fc)
    labelMostrar = Button(fc, image=imgBtnMostrar,bd=0,command=mostrarTodo)
    labelMostrar.image = imgBtnMostrar
    labelMostrar.place(x=550,y=15)

    # Radiobutton
    def seleccionar():
        monitor.config(text="{}".format(opcion.get()))

    opcion = IntVar()

    Radiobutton(fc, text="Mostrar Todos los Despachos", variable=opcion,   
                value=1).place(x=678,y=15)
    Radiobutton(fc, text="Mostrar Solo Despachos de Camionetas", variable=opcion, 
                value=2,command=seleccionar).place(x=678,y=45)
    Radiobutton(fc, text="Mostrar Solo Despachos de Camiones", variable=opcion,   
                value=3).place(x=678,y=75)
    Radiobutton(fc, text="Mostrar Solo Despachos de Motos", variable=opcion, 
                value=4).place(x=678,y=105)
    
    monitor = Label(fc)


    # Label Estadisticas de Despachos
    fuenteEstadistica = ("Dungeon", 17, "normal")
    lblEst = Label(fc,text="Estadisticas de Los Despachos",font= fuenteEstadistica, bg="#19E9EE")
    lblEst.place( x =395, y =380)

     # Boton Estadisticas Cantidad de Despachos VS Tipo
    imgGTorta = PhotoImage(file='imagenes/gtorta.png',master=fc)
    btnGTorta= Button(fc, image=imgGTorta,bd=0)
    btnGTorta.image = imgGTorta
    btnGTorta.place(x=85,y=450)
    lblDvT = Label(fc,text="Canridad de Despachos VS Tipo",font=("Dungeon", 11, "normal"),bg="#19E9EE")
    lblDvT.place(x=20,y=550 )

    # Boton Estadisticas Cantidad de Despachos VS Mes
    imgGbarras = PhotoImage(file='imagenes/gbarras.png',master=fc)
    btnGbarras= Button(fc, image=imgGbarras,bd=0)
    btnGbarras.image = imgGbarras
    btnGbarras.place(x=385,y=450)
    lblDvT = Label(fc,text="Cantidad de Despachos VS Mes",font=("Dungeon", 11, "normal"),bg="#19E9EE")
    lblDvT.place(x=320,y=550 )

    

    


    # ---------------------- Frame tabla -------------------------------

    ftabla = Frame(fc)
    ftabla.config(bg="white",width=1000,height=220,relief="groove",bd=3)
    ftabla.place(x=85,y=150,width=1000, height=220)


    tree=ttk.Treeview(ftabla,height=10,columns=('#0','#1','#2','#3','#4','#5','#6','#7','#8')) # Creacion de una Tabla
    horscrlbar = ttk.Scrollbar(ftabla, orient="horizontal", command=tree.xview) # Scrollbar X
    horscrlbar.pack(side='bottom', fill='x')
    verscrlbar = ttk.Scrollbar(ftabla, orient="vertical", command=tree.yview) #Scrollbar Y
    verscrlbar.pack(side='right', fill='y')
    tree.configure(yscrollcommand=verscrlbar.set)
    tree.configure(xscrollcommand=horscrlbar.set)
    tree.pack(side='left')

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


# ---------------------------------------------------------------------------- Inicia la Vista de los Transportistas ---------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def creaVistaTrans():
    vTrans = Toplevel(root)
    vTrans.geometry("1152x700")
    vTrans.resizable(0,0)
    
    def buscarElemento(): #Busca un elemento determinado y lo muestra en la tabla
        registros = tree.get_children()
        for elemento in registros:
            tree.delete(elemento)

        for despacho in listadoDespachos.getLista():
            if despacho.getCliente().getRut()==eBuscart.get():
                tree.insert("",END,text=despacho.getCliente().getNombre(),values=(despacho.getCliente().getDireccion(),despacho.getCliente().getRut(),despacho.getProducto().getDescripcion(),despacho.getTransporte().getTipo(),despacho.getDestinatario().getNombre(),despacho.getDestinatario().getDireccionEntrega(),despacho.getFecha(),despacho.verificarEntrega()))


    def mostrarTodo(): # Muestra los valores de cada despacho en una tabla
        registros = tree.get_children()
        for elemnto in registros:
            tree.delete(elemnto)
        for despacho in listadoDespachos.getLista():
            tree.insert("",END,text=despacho.getCliente().getNombre(),values=(despacho.getCliente().getDireccion(),despacho.getCliente().getRut(),despacho.getProducto().getDescripcion(),despacho.getTransporte().getTipo(),despacho.getDestinatario().getNombre(),despacho.getDestinatario().getDireccionEntrega(),despacho.getFecha(),despacho.verificarEntrega()))


    def seleccionarElemento(): # Me permite Registrar una Seleccion en la tabla
        item = tree.item(tree.selection())['values'][1]
        return item
    
    def soloMoto(): # Mustra solo los despachos en moto
        registros = tree.get_children()
        for elemnto in registros:
            tree.delete(elemnto)
        for despacho in listadoDespachos.getLista():
            if despacho.getTransporte().getTipo()=="moto":
                tree.insert("",END,text=despacho.getCliente().getNombre(),values=(despacho.getCliente().getDireccion(),despacho.getCliente().getRut(),despacho.getProducto().getDescripcion(),despacho.getTransporte().getTipo(),despacho.getDestinatario().getNombre(),despacho.getDestinatario().getDireccionEntrega(),despacho.getFecha(),despacho.verificarEntrega()))

    def soloCamioneta(): # Muestra solo los despachos en Camioneta
        registros = tree.get_children()
        for elemnto in registros:
            tree.delete(elemnto)
        for despacho in listadoDespachos.getLista():
            if despacho.getTransporte().getTipo()=="camioneta":
                tree.insert("",END,text=despacho.getCliente().getNombre(),values=(despacho.getCliente().getDireccion(),despacho.getCliente().getRut(),despacho.getProducto().getDescripcion(),despacho.getTransporte().getTipo(),despacho.getDestinatario().getNombre(),despacho.getDestinatario().getDireccionEntrega(),despacho.getFecha(),despacho.verificarEntrega()))

    def soloCamion(): # Muestra solo los despachos en camion
        registros = tree.get_children()
        for elemnto in registros:
            tree.delete(elemnto)
        for despacho in listadoDespachos.getLista():
            if despacho.getTransporte().getTipo()=="camion":
                tree.insert("",END,text=despacho.getCliente().getNombre(),values=(despacho.getCliente().getDireccion(),despacho.getCliente().getRut(),despacho.getProducto().getDescripcion(),despacho.getTransporte().getTipo(),despacho.getDestinatario().getNombre(),despacho.getDestinatario().getDireccionEntrega(),despacho.getFecha(),despacho.verificarEntrega()))

    def despachaElemento():
        data = seleccionarElemento()
        for despacho in listadoDespachos.getLista():
            if despacho.getCliente().getRut()==data:
                despacho.setEntregado(True)
                mostrarTodo()
                print(listadoDespachos.mostrarDespachos())
    # -------- Frame Titulo -------------
    ft = Frame(vTrans)
    ft.config(bg="#7264B1",width=1152,height=78)
    ft.pack()
    ft.pack_propagate(False)

    imgTitulo = PhotoImage(file='imagenes/transpeque.png', master=ft)
    lbltit = Label(ft,image=imgTitulo, bg="#7264B1")
    lbltit.image = imgTitulo
    lbltit.pack()

    # ---------------------------------------- Frame contenido -----------------------------------------
    fc = Frame(vTrans)
    fc.config(bg="#649FB1",width=1152,height=622)
    fc.pack()
    fc.pack_propagate(False)
    imgFondo = PhotoImage(file='imagenes/fondocielo.png', master = fc)
    lblFondo = Label(fc, image= imgFondo)
    lblFondo.image = imgFondo
    lblFondo.place(x = 0, y = 0, relwidth = 1, relheight = 1)

    Font_tuple = ("Dungeon", 33, "normal")
    lbSelec = Label(fc, text = 'Seleccione su tipo de Transporte', font = Font_tuple,bg="#1E92DA")
    lbSelec.place( x = 180 , y = 12)
    #1E92DA
    #7264B1
    # ----------------------------------------- Botones ---------------------------------------------------

    # Boton Despachos de Moto
    imgMoto = PhotoImage(file='imagenes/btnmoto.png',master=fc)
    btnMoto = Button(fc, image=imgMoto,bg="#1E92DA", command=soloMoto)
    btnMoto.image = imgMoto
    btnMoto.place( x = 200 , y = 85)

    # Boton Despachos de Camioneta
    imgCamioneta = PhotoImage(file='imagenes/btncamioneta.png',master=fc)
    btnCamioneta = Button(fc,image=imgCamioneta,bg="#1E92DA", command=soloCamioneta)
    btnCamioneta.image = imgCamioneta
    btnCamioneta.place( x = 500 , y = 85)

    # Boton Despachos de Camion
    imgCamion = PhotoImage(file='imagenes/btncamion.png',master=fc)
    btnCamion = Button(fc,image=imgCamion,bg="#1E92DA", command=soloCamion)
    btnCamion.image = imgCamion
    btnCamion.place( x = 800 , y = 85)

    # Boton Para Despachar un Producto
    imgEnviado = PhotoImage(file='imagenes/enviado.png',master=fc)
    btnEnviado = Button(fc, image=imgEnviado,bg="#1E92DA", command = despachaElemento)
    btnEnviado.image = imgEnviado
    btnEnviado.place( x = 960 , y = 440)
    Font_tuple1 = ("Dungeon", 13, "normal")
    lbBuscar = Label(fc,text="Despachado",font= Font_tuple1, bg="#1E92DA")
    lbBuscar.place( x =960, y =550 )

    # Boton para Buscar un Producto
    imgBus = PhotoImage(file='imagenes/btnbusca.png',master=fc)
    btnBus = Button(fc, image=imgBus,bg="#1E92DA", command=buscarElemento)
    btnBus.image = imgBus
    btnBus.place( x = 85 , y = 440)
    eBuscart = Entry(fc)
    eBuscart.place( x = 85, y = 550)
    Font_tuple2 = ("Dungeon", 13, "normal")
    lbBuscar = Label(fc,text="Ingrese un rut ej: 20734727-2",font= Font_tuple2, bg="#1E92DA")
    lbBuscar.place( x =85, y =580 )


    # ------------------------ Tabla -------------------------------
    ftabla = Frame(fc)
    ftabla.config(bg="white",width=1000,height=220,relief="groove",bd=3)
    ftabla.place(x=85,y=200,width=1000, height=220)
   
    

    tree=ttk.Treeview(ftabla,height=10,columns=('#0','#1','#2','#3','#4','#5','#6','#7','#8')) # Creacion de una Tabla
    horscrlbar = ttk.Scrollbar(ftabla, orient="horizontal", command=tree.xview) # Scrollbar X
    horscrlbar.pack(side='bottom', fill='x')
    verscrlbar = ttk.Scrollbar(ftabla, orient="vertical", command=tree.yview) #Scrollbar Y
    verscrlbar.pack(side='right', fill='y')
    tree.configure(yscrollcommand=verscrlbar.set)
    tree.configure(xscrollcommand=horscrlbar.set)
    tree.pack(side='left')

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

    mostrarTodo()
        
 





# --------------------------------------------------------------------------------------------- Vista Principal - root -----------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
root = Tk()
root.geometry("1152x700")
root.resizable(0,0)
ta = PhotoImage(file="imagenes/transporte.png")
ad = PhotoImage(file="imagenes/administrador.png")
btnTra = Button(root, image=ta, command=creaVistaTrans, bg='#7264B1', width=576, height=700).grid(column=0, row=0)
btnAd = Button(root, image=ad, bg='#649FB1', command=creaVistaAd, width=576, height=700).grid(column=1, row=0)


root.mainloop()