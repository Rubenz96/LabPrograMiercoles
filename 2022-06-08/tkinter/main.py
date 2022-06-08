
import tkinter as tk
from tkinter import ttk

from matplotlib.pyplot import title

def imprimirTexto():
    texto_casilla = casilla.get()
    print(texto_casilla)

ventana = tk.Tk()
ventana.title('Primera ventana')
ventana.config(height=600,width=700)
###########################################################
texto = ttk.Label(text='Ingrese un valor')
texto.place(x=10,y=10)

casilla = ttk.Entry()
casilla.place(x=120, y=10)

boton = ttk.Button(text='Imprima', command=imprimirTexto)
boton.place(x=120, y=50)

###########################################################
ventana.mainloop()