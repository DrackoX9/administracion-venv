from tkinter import *
from tkinter import ttk
from src.utilities.productsTable import TablaProductos
from src.utilities.searchBar import searchBar
from src.views.newOrdersScreen import nuevoPedidos

class VentanaPedidos():
    def __init__(self,window):
        self.win=window
        self.container=Frame(self.win)
        topMenuContainer = Frame(self.container,bg='blue')
        topMenuContainer.pack(padx=15,pady=15,ipadx=8)
        #filtros de busqueda
        #Radio buttons de opciones de filtrado
        radio_var= StringVar(topMenuContainer,"1")
        option1=Radiobutton(topMenuContainer,
                    text="En Transito",
                    variable=radio_var,
                    value="Transito").grid(row=0,column=0,padx=2.5)
        option2=Radiobutton(topMenuContainer,
                    text="Entregado",
                    variable=radio_var,
                    value="Entregado").grid(row=0,column=1,padx=2.5)
        option3=Radiobutton(topMenuContainer,
                    text="Todo",
                    variable=radio_var,
                    value="Todo").grid(row=0,column=2,padx=2.5)



        #hacer con radio buttom

        #barra de busqueda
        self.searchBar=searchBar(topMenuContainer)
        self.searchBar.searchBarContainer.grid(row=0,column=3)

        #boton de agregar nuevo producto
        Button(self.container,
               width=13,
               height=1,
               text="Agregar Pedido",
               command=self.newOrderWIndow).pack(pady=8)
        
        

        #tabla de productos
        self.tablaPedidos = TablaProductos(self.container)

        #CONTENEDOR BOTONES
        buttonContainer = Frame(self.container,bg="red")
        buttonContainer.pack(padx=15,pady=15)
        Button(buttonContainer,text="Editar",width=16,height=2).grid(column=0,row=0,padx=60,columnspan=2,sticky="we")
        Button(buttonContainer,text="Eliminar",width=16,height=2).grid(column=2,row=0,padx=60,columnspan=2,sticky="we")

    def newOrderWIndow(self):
         newProductWIn=Tk()
         newProductWIn.geometry("800x650")
         newProductWIn.title("Pedido")
         frameProductos = nuevoPedidos(newProductWIn)
         frameProductos.container.pack(fill="x")
         Button(newProductWIn,text='Guardar y Salir',height=2,command=newProductWIn.destroy).pack(pady=10)
         newProductWIn.mainloop()
    def saveExit(self,root):
        #POner aqui el codigo para guardar los productos en la base de datos
        print("abierto")
