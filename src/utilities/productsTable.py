from tkinter import *
from tkinter import ttk
##clase tabla donde se muestran los articulos        
class TablaProductos():
    def __init__(self,container):
        #CONTENEDOR TABLA
        tablecontainer=Frame(container,bg="yellow",height=260)
        tablecontainer.pack(side="top",fill="x",padx=15)
        #Creacion de la tabla
        table=ttk.Treeview(tablecontainer,height=5,columns=[f"#{n}" for n in range(1, 10)])
        table.place(x=0,y=0,relwidth=1,relheight=0.95)
        
        #Asignando numbre a las columnas
        for n1 in range(0, 10):
            table.column(f"#{n1}",anchor='c',width=120)
            table.heading(f"#{n1}",text=f"Columna {n1+1}")
        
        #Creando el scrollbar
        scrlbar=ttk.Scrollbar(tablecontainer,orient="horizontal",command=table.xview)
        scrlbar.place(relx=0.125,rely=0.95,relwidth=0.75)
