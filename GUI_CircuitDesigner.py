try:
    from Tkinter import *     ## Python 2.x
except ImportError:
    from tkinter import *    ## Python 3.x
import os

import random

class DropDown():
    def simulate(self):
        print("Simulando...")

    def __init__(self, root):
        self.root = root
        dd = Menubutton(self.root, text = "Menu", anchor=W)
        dd.menu = Menu(dd)
        dd["menu"] = dd.menu

        dd.menu.add_command(label = "Simular", command = self.simulate)
        dd.pack(fill = BOTH)

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

class popupWindow(object):
    def __init__(self,master):
        top = self.top = Toplevel(master)
        self.l = Label(top,text="Inserte un nombre para la resistencia")
        self.l.pack()
        self.e = Entry(top)
        self.e.pack()
        self.l2 = Label(top,text="Inserte un valor para la resistencia")
        self.l2.pack()
        self.e2 = Entry(top)
        self.e2.pack()
        self.b = Button(top, text = 'Ok', command = self.accept)
        self.b.pack()

    
    def accept(self):
        MA.SB.createResistor(self.e2.get(), self.e.get())
        self.cleanup()

    def cleanup(self):
        self.value = self.e.get()
        self.top.destroy()      

    

class popupWindowVol(object):
    def __init__(self, master):
        top = self.top = Toplevel(master)
        self.l3 = Label(top,text="Inserte un nombre para la fuente de voltaje")
        self.l3.pack()
        self.e3 = Entry(top)
        self.e3.pack()
        self.l4 = Label(top,text="Inserte un valor para la fuente de voltaje")
        self.l4.pack()
        self.e4 = Entry(top)
        self.e4.pack()
        self.b2 = Button(top, text = 'Ok', command = self.accept2)
        self.b2.pack()

    def accept2(self):
        MA.SB.createFuenteVoltaje(self.e4.get(), self.e3.get())
        self.cleanup2()

    def cleanup2(self):
        self.value = self.e3.get()
        self.top.destroy()  

class SideBar():
    def cargarimg(self, archivo): # Se carga imagen
        ruta = os.path.join('img', archivo)
        imagen = PhotoImage(file = ruta)
        return imagen

    def createImageButtons(self):
        resImage = self.cargarimg('Res.png')
        volImage = self.cargarimg('FuenteVoltaje.png')
        self.resBut = Button(self.window, image = resImage, command = self.nameRes)        
        self.resBut.image = resImage
        self.resBut.place(anchor = CENTER, x = 100, y = 200)
        self.volBut = Button(self.window, text = "Fuente", image = volImage, command = self.nameVol)
        self.volBut.image = volImage
        self.volBut.place(anchor = CENTER, x = 100, y = 400)
        
    def nameRes(self):
        self.w = popupWindow(self.root)
        self.resBut["state"] = "disabled" 
        self.root.wait_window(self.w.top)
        self.resBut["state"] = "normal"

    def createResistor(self, value, name):       
        Res1 = Resistor(self.root, value, name)
        MA.resList.append(Res1)
        print(Res1.name)
        print(Res1.resistance)

    def nameVol(self):
        self.w = popupWindowVol(self.root)
        self.volBut["state"] = "disabled" 
        self.root.wait_window(self.w.top)
        self.volBut["state"] = "normal"

    def createFuenteVoltaje(self, value, name):       
        Vol1 = FuenteVoltaje(self.root, value, name)
        MA.volList.append(Vol1)
        print(Vol1.name)
        print(Vol1.voltage)    

    def __init__(self, root):
        self.root = root
        self.window = Canvas(self.root,width=200, height = 600)
        self.window.pack(side = RIGHT, fill = Y)
        self.label = Label(self.root, text = "")
        self.label.pack(pady = 20)
        self.createImageButtons()
        self.x = 50
        self.y = 50

class Resistor(object):
    def cargarimg(self, archivo): # Se carga imagen
        ruta = os.path.join('img', archivo)
        imagen = PhotoImage(file = ruta)
        return imagen

    def show_res(self):
        resImage = self.cargarimg('Res.png')
        MA.resImg.append(resImage)
        MA.MP.paintWindow.image = resImage
        imgRes = MA.MP.paintWindow.create_image(random.randint(100, 600), random.randint(100,600), image = resImage)
        print("Se puso el resistor")    
        #imgRes.bind("<Button-1>",drag_start)
        #imgRes.bind("<B1-Motion>",drag_motion)
        MA.MP.paintWindow.tag_bind(imgRes, '<Button-1>', self.drag_start)
        MA.MP.paintWindow.tag_bind(imgRes, '<B1-Motion>', self.drag_motion)
        print(type(imgRes))
    
    def move(self, e):
        resImage = self.cargarimg('Res.png')
        MA.MP.paintWindow.image = resImage
        MA.MP.paintWindow.create_image(e.x, e.y, image = resImage)

    def drag_start(self, event):
        widget = event.widget
        widget.startX = event.x
        widget.startY = event.y

    def drag_motion(self, event):
        widget = event.widget
        x = widget.winfo_x() - widget.startX + event.x
        y = widget.winfo_y() - widget.startY + event.y
        widget.place(x=x,y=y)
    
    def __init__(self, root, resistance, name):
        self.root = root
        self.resistance = resistance
        self.name = name
        self.x = 50
        self.y = 50
        self.show_res()
        #MA.MP.paintWindow.bind('<B1-Motion>', self.move)
        

        

class FuenteVoltaje():
    def cargarimg(self, archivo): # Se carga imagen
        ruta = os.path.join('img', archivo)
        imagen = PhotoImage(file = ruta)
        return imagen

    def show_vol(self):
        volImage = self.cargarimg('FuenteVoltaje.png')
        MA.MP.paintWindow.image = volImage
        MA.MP.paintWindow.create_image(100, 100, image = volImage)
        MA.MP.paintWindow.create_line(0,0,100,100)
        print("Se puso la fuente de voltaje")

    def move(self, e):
        volImage = self.cargarimg('FuenteVoltaje.png')
        MA.MP.paintWindow.image = volImage
        MA.MP.paintWindow.create_image(e.x, e.y, image = volImage)
    
    def __init__(self, root, voltage, name):
        self.root = root
        self.voltage = voltage
        self.name = name
        self.x = 50
        self.y = 50
        self.show_vol()
        MA.MP.paintWindow.bind('<B1-Motion>', self.move)

class MainApplication():
    def __init__(self, parent):
        self.parent = parent
        self.DD = DropDown(self.parent)
        self.MP = MainPanel(self.parent)
        self.MP.grid()
        self.SB = SideBar(self.parent)
        self.resList = []
        self.resImg = []
        self.volList = []    

if __name__ == "__main__":
    root = Tk()
    root.geometry('1000x600')
    root.resizable(height= YES, width = YES)
    MA = MainApplication(root)
    root.mainloop()
