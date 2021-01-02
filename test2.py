from tkinter import *
import os

root = Tk()
canvas = Canvas(root)
canvas.pack()

def cargarimg(archivo): # Se carga imagen
    ruta = os.path.join('img', archivo)
    imagen = PhotoImage(file = ruta)
    return imagen
    
Res = cargarimg('FuenteVoltaje.png')
butRes = Button(root, image = Res)
butRes.pack()

root.mainloop()