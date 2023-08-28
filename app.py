from tkinter import ttk
from tkinter import *
import mysql.connector
from src.views.MainScreen import mainScreen



if __name__=='__main__':
    window = Tk() 
    window.title('OnFit Application')
    window.geometry("1000x700")
    #window.columnconfigure(0,weight=0)
    window.columnconfigure(1,weight=1)
    application = mainScreen(window)
    window.mainloop()