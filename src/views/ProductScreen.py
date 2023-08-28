from tkinter import *
from tkinter import ttk

class ventanaProductos:
    def __init__(self,window):

        #Contenedor
        self.container = Frame(window,bg="green")
        #self.container.pack(side="top")
        
        #Creacion de un frame container para la informacion de registro
        self.frame = LabelFrame(self.container,text='Registrar Nuevo Producto',bg="blue")
        self.frame.pack(side="top",padx=15,pady=15,ipadx=8)

        Label(self.frame,text='Nombre del Producto').grid(row=1,column=0,pady=15,padx=8)
        #self.productName = Entry(self.frame)
        self.productName = Entry(self.frame)
        self.productName.grid(row=1,column=1)

        Label(self.frame,text='SKU').grid(row=1,column=2,pady=15,sticky="e",padx=8)
        self.productSKU = Entry(self.frame)
        self.productSKU.grid(row=1,column=3)

        Label(self.frame,text='Talla').grid(row=2,column=0,pady=15,sticky="e",padx=8)
        self.productSize= ttk.Combobox(self.frame,
            state='readonly',
            values=['XS','S','M','L','XL','S/T'],
            width=8
        )
        self.productSize.grid(row=2,column=1,sticky="w")

        Label(self.frame,text='Color').grid(row=2,column=2,pady=15,padx=8,sticky="e")
        self.productColor= ttk.Combobox(self.frame,
            values=['Negro','Azul','Verde','Cafe','Rosado','Rojo','Gris','Naranja','Celeste','Gris Claro'],
            width=8
        )
        self.productColor.grid(row=2,column=3,sticky="w")

        Label(self.frame,text='Cantidad').grid(row=3,column=0,pady=15,padx=8,sticky="e")
        self.productQuantity = Entry(self.frame,width=5)
        self.productQuantity.grid(row=3,column=1,sticky="w")

        Label(self.frame,text='Categoria').grid(row=3,column=2,pady=15,padx=8,sticky="e")
        self.productCategory= ttk.Combobox(self.frame,
            values=['Accesorio','Set Short','Insumo','Pantalon Corto','Pantalon Largo'],
            width=8
        )
        self.productCategory.grid(row=3,column=3,sticky="w")

        Label(self.frame,text='Precio Unitario').grid(row=4,column=0,pady=15,padx=8,sticky="e")
        self.productQuantity = Entry(self.frame,width=10)
        self.productQuantity.grid(row=4,column=1,sticky="w")

        Button(self.frame,text='Guardar').grid(row=5,column=1,columnspan=2,sticky="we",pady=10)




        #CONTENEDOR TABLA
        tablecontainer=Frame(self.container,bg="yellow",height=260)
        tablecontainer.pack(side="top",fill="x",padx=15)
        #Creacion de la tabla
        self.table=ttk.Treeview(tablecontainer,height=5,columns=[f"#{n}" for n in range(1, 10)])
        self.table.place(x=0,y=0,relwidth=1,relheight=0.95)
        
        #Asignando numbre a las columnas
        for n1 in range(0, 10):
            self.table.column(f"#{n1}",anchor='c',width=120)
            self.table.heading(f"#{n1}",text=f"Columna {n1+1}")
        
        #Creando el scrollbar
        scrlbar=ttk.Scrollbar(tablecontainer,orient="horizontal",command=self.table.xview)
        scrlbar.place(relx=0.125,rely=0.95,relwidth=0.75)
        
        #Configurando la tabla
        #self.table.configure(xscrollcommand=scrlbar.set)



        #CONTENEDOR BOTONES
        self.buttonContainer = Frame(self.container,bg="red")
        self.buttonContainer.pack(padx=15,pady=15,after=tablecontainer)
        Button(self.buttonContainer,text="Editar",width=16,height=2).grid(column=0,row=0,padx=60,columnspan=2,sticky="we")
        Button(self.buttonContainer,text="Eliminar",width=16,height=2).grid(column=2,row=0,padx=60,columnspan=2,sticky="we")

        





        