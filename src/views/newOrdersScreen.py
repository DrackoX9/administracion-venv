from tkinter import *
from tkinter import ttk
from src.utilities.productsTable import TablaProductos

class nuevoPedidos:
    def __init__(self,window):
        self.win=window
        #Creacion de un frame container
        self.container=Frame(self.win)
        frame = LabelFrame(self.container,text='Registrar Nuevo Pedido')
        frame.pack(side="top",padx=15,pady=15,ipadx=8)

        Label(frame,text='Fecha de pedido').grid(row=1,column=0,pady=15,padx=8)
        self.orderDate = Entry(frame)
        self.orderDate.grid(row=1,column=1)

        Label(frame,text="Estado").grid(row=1,column=2,padx=8)
        self.state=ttk.Combobox(frame,
            state='readonly',
            values=['Transito','Entregado'],
            width=10
        
        ).grid(row=1,column=3)

        Label(frame,text='Costo de inversion').grid(row=3,column=0,pady=15,padx=8)
        self.investment = Entry(frame)
        self.investment.grid(row=3,column=1)

        Label(frame,text='Envio Aprox').grid(row=4,column=0,padx=8,pady=15)
        self.delivery = Entry(frame)
        self.delivery.grid(row=4,column=1)
        #Tabla para mostrar los pedidos agregados
        self.tablaPedidos=TablaProductos(self.container)

        
    def cerrarPedidos(self):
        self.container.destroy
        print('ventana pedidos destruida')