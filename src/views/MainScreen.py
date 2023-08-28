from tkinter import *
from tkinter import ttk
from src.views.ProductScreen import ventanaProductos
from src.utilities.utilities import sideBarView
from src.utilities.sideMenu import sideMenu

class mainScreen:
    
    def __init__(self, window):
        productScreen = ventanaProductos(window)
        menu =sideMenu() 
        menu.sideMenuContainer.grid(row=0,column=0)
        productScreen.container.grid(row=0,column=1,sticky=S+N+W+E)

        #self.mainWin.config(width=900,height=500)
        

        
    
 
        


