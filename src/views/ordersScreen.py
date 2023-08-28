from tkinter import *


class ventanaPedidos:
    def __init__(self, window):
        self.win=window

        #Creacion de un frame container
        frame = LabelFrame(self.win,text='Registrar Nuevo Pedido')
        frame.grid(row=0, column=0,columnspan=3,pady=25,padx=150)

        Label(frame,text='Fecha de pedido').grid(row=1,column=0,pady=15)
        self.orderDate = Entry(frame)
        self.orderDate.grid(row=1,column=1,padx=15)

        Label(frame,text='Fecha de LLegada').grid(row=2,column=0)
        self.arrivalDate = Entry(frame)
        self.arrivalDate.grid(row=2,column=1,padx=15)

        Label(frame,text='Costo de inversion').grid(row=3,column=0,pady=15)
        self.investment = Entry(frame)
        self.investment.grid(row=3,column=1,padx=15)

        Label(frame,text='Envio Aprox').grid(row=4,column=0)
        self.delivery = Entry(frame)
        self.delivery.grid(row=4,column=1,padx=15)