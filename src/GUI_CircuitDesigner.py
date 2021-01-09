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
        self.cbValue = BooleanVar()
        self.CB = Checkbutton(top, text = 'Vertical', variable = self.cbValue)
        self.CB.pack()
        self.b = Button(top, text = 'Ok', command = self.accept)
        self.b.pack()

    
    def accept(self):
        MA.SB.createResistor(self.e2.get(), self.e.get(), self.cbValue.get())
        print(self.cbValue.get())
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
        self.cbValue = BooleanVar()
        self.CB = Checkbutton(top, text = 'Vertical', variable = self.cbValue)
        self.CB.pack()
        self.b2 = Button(top, text = 'Ok', command = self.accept2)
        self.b2.pack()


    def accept2(self):
        MA.SB.createFuenteVoltaje(self.e4.get(), self.e3.get(), self.cbValue.get())
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
        self.cleanBut = Button(self.window, text = "clean window", command = self.cleanWin)
        self.cleanBut.place(anchor = CENTER, x = 100, y = 100)
        
    def nameRes(self):
        self.w = popupWindow(self.root)
        self.resBut["state"] = "disabled" 
        self.root.wait_window(self.w.top)
        self.resBut["state"] = "normal"

    def createResistor(self, value, name, vertical):       
        Res1 = Resistor(self.root, value, name, vertical)
        MA.resList.append(Res1)
        print(Res1.name)
        print(Res1.resistance)

    def nameVol(self):
        self.w = popupWindowVol(self.root)
        self.volBut["state"] = "disabled" 
        self.root.wait_window(self.w.top)
        self.volBut["state"] = "normal"

    def createFuenteVoltaje(self, value, name, vertical):       
        Vol1 = FuenteVoltaje(self.root, value, name, vertical)
        MA.volList.append(Vol1)
        print(Vol1.name)
        print(Vol1.voltage)    

    def cleanWin(self):
        MA.resImg.clear()
        MA.resList.clear()
        MA.volImg.clear()
        MA.volList.clear()
        MA.MP.paintWindow.delete("resistance")
        MA.MP.paintWindow.delete("voltage")
       

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
        if self.vertical == False:
            resImage = self.cargarimg('Res.png') #Resistencia horizontal
            MA.resImg.append(resImage)        
            MA.MP.paintWindow.image = resImage            
            imgRes = MA.MP.paintWindow.create_image(random.randint(100, 600), random.randint(100,600), image = resImage, tag = "resistance")                
            self.corners = MA.MP.paintWindow.bbox(imgRes) 
        else:
            resImage2 = self.cargarimg('Res2.png') #Resistencia vertical
            MA.resImg.append(resImage2)
            MA.MP.paintWindow.image = resImage2
            imgRes2 = MA.MP.paintWindow.create_image(random.randint(100, 600), random.randint(100,600), image = resImage2, tag = "resistance")
            self.corners = MA.MP.paintWindow.bbox(imgRes2)     
        
        print("Se puso el resistor")    
        #print(type(imgRes))


    def drag_start(self, event):
        """Begining drag of an object"""
        # record the item and its location
        self._drag_data["item"] = MA.MP.paintWindow.find_closest(event.x, event.y)[0]
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def drag_stop(self, event):
        """End drag of an object"""
        # reset the drag information
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0

    def drag(self, event):
        """Handle dragging of an object"""
        # compute how much the mouse has moved
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]
        # move the object the appropriate amount
        MA.MP.paintWindow.move(self._drag_data["item"], delta_x, delta_y)
        # record the new position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y
        self.corners = MA.MP.paintWindow.bbox(self._drag_data["item"])

    def phb(self, event):        
        if self.vertical == False:
            if event.x > self.corners[0] and event.x < self.corners[0] + 20 and event.y > self.corners[1] and event.y < self.corners[3]:
            #print(event.x , event.y)
            #self.x+=1
                print("max garro")
            if event.x < self.corners[2] and event.x > self.corners[2] - 20 and event.y > self.corners[1] and event.y < self.corners[3]:
                print("cr7")        
            else:
                pass
        else:
            if event.x > self.corners[0] and event.x < self.corners[2] and event.y > self.corners[1] and event.y < self.corners[1] + 20:
            #print(event.x , event.y)
            #self.x+=1
                print("matt garro")
            if event.x > self.corners[0] and event.x < self.corners[2] and event.y < self.corners[3] and event.y > self.corners[3] - 20:
                print("cr9")        
            else:
                pass
            
    def __init__(self, root, resistance, name, vertical):
        self.vertical = vertical
        self.root = root
        self._drag_data = {"x": 0, "y": 0, "item": None}
        self.resistance = resistance
        self.name = name
        self.x = 50
        self.y = 50
        self.corners = None
        MA.MP.paintWindow.tag_bind("resistance", "<ButtonPress-1>", self.drag_start)
        MA.MP.paintWindow.tag_bind("resistance", "<ButtonRelease-1>", self.drag_stop)
        MA.MP.paintWindow.tag_bind("resistance", "<B1-Motion>", self.drag)
        MA.MP.paintWindow.tag_bind("resistance", "<Button-3>", self.phb)
        #MA.MP.paintWindow.tag_bind("resistance", "<Button-3>", self.nhb)
        self.show_res()
        
        #MA.MP.paintWindow.tag_bind("resistance", "<Button-1>", self.nhb)
        #MA.MP.paintWindow.bind('<B1-Motion>', self.move)
        

        

class FuenteVoltaje():
    def cargarimg(self, archivo): # Se carga imagen
        ruta = os.path.join('img', archivo)
        imagen = PhotoImage(file = ruta)
        return imagen

    def show_vol(self):
        if self.vertical == True:
            volImage = self.cargarimg('FuenteVoltaje.png')
        else:
            volImage = self.cargarimg('FuenteVoltaje2.png')
            
        MA.volImg.append(volImage)
        MA.MP.paintWindow.image = volImage
        imgVol = MA.MP.paintWindow.create_image(random.randint(100, 600), random.randint(100,600), image = volImage, tag = "voltage")
        self.corners = MA.MP.paintWindow.bbox(imgVol)
        print("Se puso la fuente de voltaje")

    def drag_start(self, event):
        """Begining drag of an object"""
        # record the item and its location
        self._drag_data["item"] = MA.MP.paintWindow.find_closest(event.x, event.y)[0]
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def drag_stop(self, event):
        """End drag of an object"""
        # reset the drag information
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0

    def drag(self, event):
        """Handle dragging of an object"""
        # compute how much the mouse has moved
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]
        # move the object the appropriate amount
        MA.MP.paintWindow.move(self._drag_data["item"], delta_x, delta_y)
        # record the new position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def phb(self, event):    
        if event.x > self.corners[0] and event.x < self.corners[0] + 20 and event.y > self.corners[1] and event.y < self.corners[3]:
            #print(event.x , event.y)
            #self.x+=1
            print("cr34")
        #if event.x < self.corners[2] and event.x > self.corners[2] - 20 and event.y > self.corners[1] and event.y < self.corners[3]:
            #print("cr7")        
        else:
            pass
    
    def __init__(self, root, voltage, name, vertical):
        self.vertical = vertical
        self.root = root
        self.corners = None
        self._drag_data = {"x": 0, "y": 0, "item": None}
        MA.MP.paintWindow.tag_bind("voltage", "<ButtonPress-1>", self.drag_start)
        MA.MP.paintWindow.tag_bind("voltage", "<ButtonRelease-1>", self.drag_stop)
        MA.MP.paintWindow.tag_bind("voltage", "<B1-Motion>", self.drag)
        MA.MP.paintWindow.tag_bind("voltage", "<Button-3>", self.phb)
        self.voltage = voltage
        self.name = name
        self.x = 50
        self.y = 50
        self.show_vol()
        #MA.MP.paintWindow.bind('<B1-Motion>', self.move)

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
        self.volImg = []  
        self.click = False

if __name__ == "__main__":
    root = Tk()
    root.geometry('1000x600')
    root.resizable(height= YES, width = YES)
    MA = MainApplication(root)
    root.mainloop()
