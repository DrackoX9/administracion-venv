from tkinter import *



class ventanaCategorias:
    #constructor
    def __init__(self, window):
        self.win=window
        #self.win.title('OnFit App')

        #Creacion de un frame container
        frame = LabelFrame(self.win,text='Registrar Nueva Categoría')
        frame.grid(row=0, column=0,columnspan=3,pady=25,padx=25)

        #input para nombre
        Label(frame,text='Nombre de Categoría').grid(row=1,column=0)
        self.categoryName = Entry(frame)
        self.categoryName.grid(row=1,column=1,padx=15)

