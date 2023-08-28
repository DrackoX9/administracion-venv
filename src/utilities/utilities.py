from tkinter import *
from tkinter import ttk


class sideBarView:
    #Constructor
    def __init__(self):
        self.sideBarContainer =Frame(bg="purple")
        self.sideBarContainer.pack(side="top")
        self.frame = LabelFrame(self.sideBarContainer,text='Registrar Nuevo Producto')
        self.frame.pack(side="top",padx=15,pady=15,ipadx=8)
        Label(self.frame,text='Nombre del Producto').grid(row=1,column=0,pady=15,padx=8)
        #self.productName = Entry(self.frame)
        self.productName = Entry(self.frame)
        self.productName.grid(row=1,column=1)