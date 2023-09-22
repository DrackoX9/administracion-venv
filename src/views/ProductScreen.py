from tkinter import *
from tkinter import ttk
from src.utilities.productsTable import TablaProductos
class ventanaProductos:
    def __init__(self,window):
        #Contenedor
        self.container = Frame(window,bg="green")
        #self.container.pack(side="top")
        
        #Creacion de un frame container para la informacion de registro
        frame = LabelFrame(self.container,text='Producto',bg="blue")
        frame.pack(side="top",padx=15,pady=15,ipadx=8)

        Label(frame,text='Nombre del Producto').grid(row=1,column=0,pady=15,padx=8)
        #self.productName = Entry(frame)
        self.productName = Entry(frame)
        self.productName.grid(row=1,column=1)

        Label(frame,text='SKU').grid(row=1,column=2,pady=15,sticky="e",padx=8)
        self.productSKU = Entry(frame)
        self.productSKU.grid(row=1,column=3)

        Label(frame,text='Talla').grid(row=2,column=0,pady=15,sticky="e",padx=8)
        self.productSize= ttk.Combobox(frame,
            state='readonly',
            values=['XS','S','M','L','XL','S/T'],
            width=8
        )
        self.productSize.grid(row=2,column=1,sticky="w")

        Label(frame,text='Color').grid(row=2,column=2,pady=15,padx=8,sticky="e")
        self.productColor= ttk.Combobox(frame,
            values=['Negro','Azul','Verde','Cafe','Rosado','Rojo','Gris','Naranja','Celeste','Gris Claro'],
            width=8
        )
        self.productColor.grid(row=2,column=3,sticky="w")

        Label(frame,text='Cantidad').grid(row=3,column=0,pady=15,padx=8,sticky="e")
        self.productQuantity = Entry(frame,width=5)
        self.productQuantity.grid(row=3,column=1,sticky="w")

        Label(frame,text='Categoria').grid(row=3,column=2,pady=15,padx=8,sticky="e")
        self.productCategory= ttk.Combobox(frame,
            values=['Accesorio','Set Short','Insumo','Pantalon Corto','Pantalon Largo'],
            width=8
        )
        self.productCategory.grid(row=3,column=3,sticky="w")

        Label(frame,text='Precio Unitario').grid(row=4,column=0,pady=15,padx=8,sticky="e")
        self.productQuantity = Entry(frame,width=10)
        self.productQuantity.grid(row=4,column=1,sticky="w")

        Button(frame,text='Aceptar').grid(row=5,column=1,columnspan=2,sticky="we",pady=10)

        #TABLA DE PRODUCTOS
        self.tablaProductos= TablaProductos(self.container)


        # #CONTENEDOR TABLA
        # tablecontainer=Frame(self.container,bg="yellow",height=260)
        # tablecontainer.pack(side="top",fill="x",padx=15)
        # #Creacion de la tabla
        # table=ttk.Treeview(tablecontainer,height=5,columns=[f"#{n}" for n in range(1, 10)])
        # table.place(x=0,y=0,relwidth=1,relheight=0.95)
        
        # #Asignando numbre a las columnas
        # for n1 in range(0, 10):
        #     table.column(f"#{n1}",anchor='c',width=120)
        #     table.heading(f"#{n1}",text=f"Columna {n1+1}")
        
        # #Creando el scrollbar
        # scrlbar=ttk.Scrollbar(tablecontainer,orient="horizontal",command=table.xview)
        # scrlbar.place(relx=0.125,rely=0.95,relwidth=0.75)
        
        # #Configurando la tabla
        # #self.table.configure(xscrollcommand=scrlbar.set)
    def __del__(self):
        print("metodo del")
        
        





        