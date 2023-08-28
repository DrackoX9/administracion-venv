from tkinter import *
from tkinter import ttk


class sideMenu:
    #Constructor
    def __init__(self):
        self.sideMenuContainer =Frame(bg="purple")
        self.sideMenuContainer.pack(side="top")
        Label(self.sideMenuContainer,text='Menu Principal',width=28,height=3,pady=25).pack()
        Button(self.sideMenuContainer,
               text='Inventario',
               width=28,
               height=3,
               bg="gray",).pack(pady=5)
        Button(self.sideMenuContainer,
               text='Ventas',
               width=28,
               height=3,
               bg="gray").pack(pady=5)
        Button(self.sideMenuContainer,
               text='Pedidos',
               width=28,
               height=3,
               bg="gray").pack(pady=5)
        Button(self.sideMenuContainer,
               text='Reportes',
               width=28,
               height=3,
               bg="gray").pack(pady=5)