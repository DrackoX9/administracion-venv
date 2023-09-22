from tkinter import *
from tkinter import ttk

##clase de la barra de busqueda
class searchBar():
    def __init__(self,window):
        self.win =window
        self.searchBarContainer=Frame(self.win,padx=10)
        searchEntry=Entry(self.searchBarContainer).grid(row=0,column=0,padx=6)
        searchButton = Button(self.searchBarContainer,
                                   text='Buscar').grid(row=0,column=1)
        