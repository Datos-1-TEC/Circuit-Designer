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
        resBut = Button(self.window, image = resImage, command = self.createResistor)        
        resBut.image = resImage
        resBut.place(anchor = CENTER, x = 100, y = 200)
        volBut = Button(self.window, text = "Fuente", image = volImage)
        volBut.image = volImage
        volBut.place(anchor = CENTER, x = 100, y = 400)
        
        

    def createResistor(self):       
        Res1 = Resistor(self.root, 10, "max")
        

    def __init__(self, root):
        self.root = root
        self.window = Canvas(self.root,width=200, height = 600)
        self.window.pack(side = RIGHT, fill = Y)
        self.label = Label(self.root, text = "")
        self.label.pack(pady = 20)
        self.createImageButtons()
        self.x = 50
        self.y = 50


class Resistor():
    def cargarimg(self, archivo): # Se carga imagen
        ruta = os.path.join('img', archivo)
        imagen = PhotoImage(file = ruta)
        return imagen

    def show_res(self):
        resImage = self.cargarimg('Res.png')
        MA.MP.paintWindow.image = resImage
        MA.MP.paintWindow.create_image(200, 100, image = resImage, anchor = NW)
        MA.MP.paintWindow.create_line(0,0,100,100)
        print("Se puso el resistor")
    
    def __init__(self, root, resistance, name):
        self.root = root
        self.resistance = resistance
        self.name = name
        self.x = 50
        self.y = 50
        self.show_res()


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
    root.resizable(height= YES, width = YES)
    MA = MainApplication(root)
    root.mainloop()
