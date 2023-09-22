from tkinter import *
from tkinter import ttk
from src.views.ProductScreen import ventanaProductos
from src.views.orderScreen import VentanaPedidos
from src.views.inventoryScreen import VentanaInventario

class mainScreen:
    
    
    def __init__(self, window):
        self.win=window
        self.sideMenu()
        self.frameProductos=VentanaInventario(self.win).container.grid(row=0,column=1,sticky=S+N+W+E)

    def sideMenu(self):
        sideMenuContainer =Frame(bg="purple")
        sideMenuContainer.grid(row=0,column=0)
        Label(sideMenuContainer,text='Menu Principal',width=28,height=3,pady=25).pack()
        Button(sideMenuContainer,
               text='Inventario',
               width=28,
               height=3,
               bg="gray",
               command=self.abrirInventario).pack(pady=5)
        Button(sideMenuContainer,
               text='Ventas',
               width=28,
               height=3,
               bg="gray").pack(pady=5)
        Button(sideMenuContainer,
               text='Pedidos',
               width=28,
               height=3,
               bg="gray",
               command=self.abrirPedidos).pack(pady=5)
        Button(sideMenuContainer,
               text='Reportes',
               width=28,
               height=3,
               bg="gray").pack(pady=5)
    def abrirInventario(self):
        self.frameInventario = VentanaInventario(self.win)
        self.frameInventario.container.grid(row=0,column=1,sticky=S+N+W+E)   
    def abrirPedidos(self):
        self.framePedidos=VentanaPedidos(self.win)
        self.framePedidos.container.grid(row=0,column=1,sticky=S+N+W+E)
        


        
        

        
    
 
        


