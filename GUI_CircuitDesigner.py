try:
    from Tkinter import *     ## Python 2.x
except ImportError:
    from tkinter import *    ## Python 3.x
import os

class DropDown():
    def __init__(self, root):
        self.root = root
        variable = StringVar(self.root)
        variable.set('Menu')
        w = OptionMenu(self.root, variable, "one", "two", "three")
        w.pack(fill = BOTH)

class MainPanel(Canvas):

    def grid(self):
        w = self.w
        h = self.h
        self.paintWindow.delete('grid_line') # Will only remove the grid_line
        for i in range(0, w, 50):
            self.paintWindow.create_line([(i, 0), (i, h)], tag='grid_line')
        for i in range(0, h, 50):
            self.paintWindow.create_line([(0, i), (w, i)], tag='grid_line')           

    def __init__(self, root):
        self.paintWindow = Canvas(root, width = 800, height = 600, bg = 'white')
        self.paintWindow.pack(side = LEFT)
        self.w = 800       
        self.h = 600
        

class SideBar():
    def cargarimg(self, archivo): # Se carga imagen
        ruta = os.path.join('img', archivo)
        imagen = PhotoImage(file = ruta)
        return imagen

    def createImageButtons(self):
        resImage = self.cargarimg('Res.png')
        volImage = self.cargarimg('FuenteVoltaje.png')
        resBut = Button(self.window, image = resImage)
        resBut.image = resImage
        resBut.place(anchor = CENTER, x = 100, y = 200)
        volBut = Button(self.window, text = "Fuente", image = volImage)
        volBut.image = volImage
        volBut.place(anchor = CENTER, x = 100, y = 400)
        

    def __init__(self, root):
        self.root = root
        self.window = Canvas(self.root,width=200, height = 600)
        self.window.pack(side = RIGHT, fill = Y)
        self.createImageButtons()

class MainApplication():
    def __init__(self, parent):
        self.parent = parent
        self.DD = DropDown(self.parent)
        self.MP = MainPanel(self.parent)
        self.MP.grid()
        self.SB = SideBar(self.parent)
        


if __name__ == "__main__":
    root = Tk()
    root.geometry('1000x600')
    root.resizable(height= NO, width = YES)
    MainApplication(root)
    root.mainloop()
