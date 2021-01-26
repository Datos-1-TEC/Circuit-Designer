try:
    from Tkinter import *     ## Python 2.x
except ImportError:
    from tkinter import *    ## Python 3.x
import os

import random
from Graph import *
from ElectricCircuit import *
from CanvasToolTip import *
from NetlistExporter import *
from NetlistImporter import * 
from tkinter import filedialog 
from Dijkstra2 import * 
from SortingAlgorithms import *
Simulating = False
from tkinter import messagebox  


class DropDown():
    def simulate(self):
        global Simulating
        Simulating = True
        MA.SB.createImageButtons()
        print("Simulando...")

        cables_list = MA.cablesList
        canvas = MA.MP.paintWindow

        if Simulating:
            for cable in cables_list:
                canvas.itemconfig(cable.get_canvas_cable(), fill='green')


    def design(self):
        global Simulating
        Simulating = False

        cables_list = MA.cablesList
        canvas = MA.MP.paintWindow

        if not Simulating:
            for cable in cables_list:
                canvas.itemconfig(cable.get_canvas_cable(), fill='black')
                cable.showToolTipForNotSimulating()

        MA.SB.createImageButtons()

    def generate_netlist(self):
       #netlist_dict =  MA.ElectricCircuit.get_connections_for_netlist()
       netlist_dictionary = MA.ElectricCircuit.get_dict_netlist()
       #print("Print from menu ")
       #print(netlist_dict)
       parent = MA.parent
       netlist_generator = NetlistExporter(netlist_dictionary,parent)
       netlist_generator.create_netlist_file()

    def import_netlist(self):
        print("Import netlist file")
        netlist_file = filedialog.askopenfilename(filetypes = (("Netlist Files", "*.txt")
                                                         ,("All files", "*.*") ))
        print(netlist_file)

        parent = MA.parent

        netlist_importer = NetlistImporter(netlist_file,parent)
        electric_components = netlist_importer.get_electric_components_to_create()

        print(electric_components)

        for electric_comp in electric_components:
            value,component,name = electric_comp
            print(electric_comp)
            if "Resistor" in component:
                MA.SB.createResistor(int(value),name,False)
                #r = ResistorGUI(parent,int(value),name,False)
                print("Resistor created")
            elif "Source" in component:
                MA.SB.createFuenteVoltaje(int(value),name,True)
                #s = FuenteVoltajeGUI(parent,int(value),name,True)
                print("Source created")
                MA.SB.createGround()
                

        netlist_importer.show_connections_from_netlist()


    def test_dict(self):
        graph = MA.ElectricCircuit.get_graph_as_dict()
        dj = Dijkstra2(graph, 'C0', 'C5')
        dj.get_shortest_path()

    def __init__(self, root):
        self.root = root
        #self.simulating = False
        #Simulating = True
        #self.simulate = True
        dd = Menubutton(self.root, text = "Menu", anchor=W)
        dd.menu = Menu(dd)
        dd["menu"] = dd.menu

        dd.menu.add_command(label = "Simular", command = self.simulate)
        dd.menu.add_command(label = "Export Netlist File",command = self.generate_netlist)
        dd.menu.add_command(label = "Import Netlist File",command = self.import_netlist)
        dd.menu.add_command(label = "Diseño", command = self.design)
        dd.menu.add_command(label = "Prueba dijsktra", command = self.test_dict)

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

class popupWindow():
    def __init__(self,master):
        top = self.top = Toplevel(master)
        self.l = Label(top,text="Inserte un nombre para la resistencia")
        self.l.pack()
        self.e = Entry(top)
        self.e.pack()
        self.l2 = Label(top,text="Inserte un valor para la resistencia" + "(\u03A9)")
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
        self.l4 = Label(top,text="Inserte un valor para la fuente de voltaje" + "(V)")
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

class popupWindowNode():
    def __init__(self, master, x, y):
        top = self.top = Toplevel(master)
        self.l5 = Label(top,text="Inserte un nombre para el nodo")
        self.l5.pack()
        self.nombreNodo = Entry(top)
        self.nombreNodo.pack()
        self.cbValue1 = BooleanVar()
        self.cbValue2 = BooleanVar()
        self.CBInicio = Checkbutton(top, text = 'Inicio', variable = self.cbValue1)
        self.CBInicio.pack()
        self.CBFinal = Checkbutton(top, text = 'Final', variable = self.cbValue2)
        self.CBFinal.pack()
        self.b3 = Button(top, text = 'Ok', command = self.accept)
        self.b3.pack()
        self.x = x
        self.y = y
    
    def addName(self, name):
        labelNode = Label(MA.MP.paintWindow, text = name, background = "green")
        labelNode.place(x = self.x, y = self.y)
    
    def accept(self):
        self.addName(self.nombreNodo.get())
        print("Inicio? ", self.cbValue1.get())
        print("Final? ", self.cbValue2.get())
        self.cleanup()

    def cleanup(self):
        self.value = self.nombreNodo.get()
        self.top.destroy() 

class SideBar():
    def cargarimg(self, archivo): # Se carga imagen
        ruta = os.path.join('img', archivo)
        imagen = PhotoImage(file = ruta)
        return imagen

    def createImageButtons(self):    
        global Simulating    
        if Simulating == False: 
            self.resBut.place_forget()
            self.volBut.place_forget()
            self.cleanBut.place_forget()
            self.groundBut.place_forget()
            self.addName.place_forget()
            self.resistancesList.place_forget()
            self.plusVolt.place_forget()
            self.minusVolt.place_forget()         
            self.resBut.place(anchor = CENTER, x = 100, y = 200)                    
            self.volBut.place(anchor = CENTER, x = 100, y = 350)            
            self.cleanBut.place(anchor = CENTER, x = 100, y = 100)
            self.groundBut.place(anchor = CENTER, x = 100, y = 500)
        else:
            #**********EN CASO QUE SEA SIMULACION***********#
            self.resBut.place_forget()
            self.volBut.place_forget()
            self.cleanBut.place_forget()
            self.groundBut.place_forget()
            self.addName.place_forget()
            self.resistancesList.place_forget()
            self.plusVolt.place_forget()
            self.minusVolt.place_forget()
            self.addName.place(anchor = CENTER, x = 100, y = 50) 
            self.plusVolt.place(anchor = CENTER, x = 100, y = 100) 
            self.minusVolt.place(anchor = CENTER, x = 100, y = 150) 
            self.resistancesList.place(anchor = CENTER, x = 100, y = 200)

            for Cable in MA.cablesList:
                Cable.showToolTip()             
                    
    def nameRes(self): #Max Garro
        self.w = popupWindow(self.root)
        self.resBut["state"] = "disabled" 
        self.root.wait_window(self.w.top)
        self.resBut["state"] = "normal"

    def get_connection_name(self):
        name = 'C' + str(self.nodeConnectionCounter)
        self.nodeConnectionCounter += 1

        return name

    def createResistor(self, value, name, vertical):       
        Res1 = ResistorGUI(self.root, value, name, vertical)
        # Se llama al metodo ElectricCircuit.create_resistor_link pasando como parametros Res1.resistorNode y self.connectionName
        MA.ElectricCircuit.create_resistor_link(Res1.resistorNode, self.get_connection_name())
        MA.resList.append(Res1)
        self.allElements.append(Res1)
        print(Res1.name)
        print(Res1.resistance)

    def nameVol(self):
        self.w = popupWindowVol(self.root)
        self.volBut["state"] = "disabled" 
        self.root.wait_window(self.w.top)
        self.volBut["state"] = "normal"

    def createFuenteVoltaje(self, value, name, vertical):       
        Vol1 = FuenteVoltajeGUI(self.root, value, name, vertical)
        MA.ElectricCircuit.create_voltage_link(Vol1.voltageNode, self.get_connection_name())
        MA.volList.append(Vol1)
        self.allElements.append(Vol1)
        print(Vol1.name)
        print(Vol1.voltage)    

    def cleanWin(self):
        MA.resImg.clear()
        MA.resList.clear()
        MA.volImg.clear()
        MA.volList.clear()
        MA.ElectricCircuit.dict_netlist = {}
        MA.MP.paintWindow.delete("resistance")
        MA.MP.paintWindow.delete("voltage")
        MA.MP.paintWindow.delete("cable")
        MA.MP.paintWindow.delete("label")

    def addNameToNode(self):
        pass

    def minus_dijsktra(self):
        top = self.top = Toplevel(self.root)
        self.front_label = Label(top, text = "Nombre del nodo inicio")
        self.front_label.pack()
        self.front_entry = Entry(top)
        self.front_entry.pack()
        self.end_label = Label(top, text = "Nombre del nodo final")
        self.end_label.pack()
        self.end_entry = Entry(top)
        self.end_entry.pack()
        self.ok_buttton = Button(top, text = "Ok", command = self.accept_dijkstra)
        self.ok_buttton.pack()

    def search_nodes(self):
        start = self.front_entry.get()
        end = self.end_entry.get()
        self.C1 = ""
        self.C2 = ""
        for component in self.allElements:
            if start == component.user_node_name and isinstance(component, ResistorGUI):
                self.C1 = component.resistorNode.get_adjacent_nodes_info()[0] + component.voltageNode.get_adjacent_nodes_info()[1]
            elif start == component.user_node_name and isinstance(component, FuenteVoltajeGUI):
                self.C1 = component.voltageNode.get_adjacent_nodes_info()[0] + component.voltageNode.get_adjacent_nodes_info()[1]
                                 
            print("Nombre  nodo: ", self.C1)  

        for component in self.allElements:
            if end == component.user_node_name and isinstance(component, ResistorGUI):
                self.C2 = component.resistorNode.get_adjacent_nodes_info()[0] +component.resistorNode.get_adjacent_nodes_info()[1]
            elif end == component.user_node_name and isinstance(component, FuenteVoltajeGUI):
                self.C2 = component.voltageNode.get_adjacent_nodes_info()[0] + component.voltageNode.get_adjacent_nodes_info()[1]
                
            print("Nombre  nodo: ", self.C2)
    
    def accept_dijkstra(self):
        self.search_nodes()
        C = ""
        graph = MA.ElectricCircuit.get_graph_as_dict()
        dj = Dijkstra2(graph, self.C1, self.C2)
        dj.get_shortest_path()
        pathNodes = dj.get_route()
        
        for node in pathNodes:
            for component in self.allElements:
                if isinstance(component, ResistorGUI):
                    C = component.resistorNode.get_adjacent_nodes_info()[0] + component.resistorNode.get_adjacent_nodes_info()[1]
                    if C == node:
                        self.shortestpath += component.name + "->"

                elif isinstance(component, FuenteVoltajeGUI):
                    C = component.voltageNode.get_adjacent_nodes_info()[0] + component.voltageNode.get_adjacent_nodes_info()[1]
                    if C == node:
                        self.shortestpath += component.name + "->"

        self.top.destroy()
        messagebox.showinfo("Shortest path", "El camino más corto es: \n" + self.shortestpath)

    def show_res_names(self):
        resistorsList = MA.resList

        names_list = LinkedList()
        for i in range(resistorsList.get_size()):
            name = resistorsList.index(i).get_data().name
            names_list.append(name)

        sort = SortingAlgorithms(names_list)
        
        start = sort.get_list().get_head()
        end = sort.get_list().get_tail()
        sort.quick_sort(start, end)
        asc_list = sort.get_list()
        result_asc = self.string_results(asc_list )

        sort.insertion_Sort()
        desc_list = sort.get_list()
        result_desc = self.string_results(desc_list)
        
        messagebox.showinfo("Lista", "Ascendente: " + result_asc + "\n" + "Descendente: " + result_desc)
    
    def string_results(self, asc_list):
        result = ""
        for i in range(asc_list.get_size()):
            result += " | " + asc_list.index(i).get_data()

        return result

    def createGround(self):
        MA.SB.createFuenteVoltaje(0, "V0", True)

    def __init__(self, root):
        self.root = root
    
        self.window = Canvas(self.root,width=200, height = 600)
        self.window.pack(side = RIGHT, fill = Y)
        self.label = Label(self.root, text = "")
        self.label.pack(pady = 20)
        self.allElements = []
        self.nodeConnectionCounter = 0         
        resImage = self.cargarimg('Res.png')
        volImage = self.cargarimg('FuenteVoltaje.png')  
        gndImage = self.cargarimg('GND.png')
        self.resBut = Button(self.window, image = resImage, command = self.nameRes)            
        self.volBut = Button(self.window, text = "Fuente", image = volImage, command = self.nameVol)             
        self.cleanBut = Button(self.window, text = "clean window", command = self.cleanWin) 
        self.groundBut = Button(self.window, text = "Tierra", image = gndImage, command = self.createGround)
        self.resBut.image = resImage             
        self.volBut.image = volImage
        self.groundBut.image = gndImage
        self.addName = Button(self.window, text = "Add name to node", command = self.addNameToNode)                           
        self.resistancesList = Button(self.window, text = "Lista de resistencias", command = self.show_res_names)                           
        self.plusVolt = Button(self.window, text = "Buscar camino + tension", command = self.addNameToNode)                           
        self.minusVolt = Button(self.window, text = "Buscar camino - tension", command = self.minus_dijsktra)                           
        
        self.createImageButtons()
        self.x = 50
        self.y = 50
        self.shortestpath = ""

class Cable():
    def drawCable(self, x1, y1, x2, y2):
        global Simulating
        self.cable = MA.MP.paintWindow.create_line(x1, y1, x2, y2, tag = "cable", width = 5)

    def get_canvas_cable(self):
        return self.cable
        
    def showToolTip(self):
        CanvasTooltip(MA.MP.paintWindow, self.cable, text = 'V = ' + str(self.voltage) + "V" +  '\n' + 'I = ' + str(self.current) + "mA")
        print('V = ' + str(self.voltage) + '\n' + 'I = ' + str(self.current))

    def showToolTipForNotSimulating(self):
        CanvasTooltip(MA.MP.paintWindow, self.cable, text = "Select simulate to show the values of the cable")

    

    def __init__(self, root, x1, y1, x2, y2, component1, component2):
        self.root = root
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.component1 = component1
        self.component2 = component2
        self.voltage = MA.ElectricCircuit.search_connection(self.component1).get_voltage()
        self.current = MA.ElectricCircuit.search_connection(self.component1).get_current()
        self.drawCable(self.x1, self.y1, self.x2, self.y2)
    
class ResistorGUI():
    def cargarimg(self, archivo): # Se carga imagen
        ruta = os.path.join('img', archivo)
        imagen = PhotoImage(file = ruta)
        return imagen

    def show_res(self):
        if self.vertical == False:
            resImage = self.cargarimg('Res.png') #Resistencia horizontal
            MA.resImg.append(resImage)        
            MA.MP.paintWindow.image = resImage            
            imgRes = MA.MP.paintWindow.create_image(random.randint(100, 600), random.randint(100,500), image = resImage, tag = "resistance") 
            self.img = imgRes               
            self.corners = MA.MP.paintWindow.bbox(imgRes)             
            l = Label(MA.MP.paintWindow, text = self.name + "\n" + str(self.resistance) + '\u03A9')
            self.namelabel = MA.MP.paintWindow.create_window(self.corners[0], self.corners[1], window = l, anchor = SW, tag = "label")
            #lv = Label(MA.MP.paintWindow, text = self.resistance)
            #self.resistancelabel = MA.MP.paintWindow.create_window(self.corners[0], self.corners[1], window = lv, anchor = NW, tag = "label")
        else:
            resImage2 = self.cargarimg('Res2.png') #Resistencia vertical
            MA.resImg.append(resImage2)
            MA.MP.paintWindow.image = resImage2
            imgRes2 = MA.MP.paintWindow.create_image(random.randint(100, 600), random.randint(100,500), image = resImage2, tag = "resistance")
            self.img = imgRes2
            self.corners = MA.MP.paintWindow.bbox(imgRes2)   
            l = Label(MA.MP.paintWindow, text = self.name + "\n" + str(self.resistance) + '\u03A9')  
            self.namelabel = MA.MP.paintWindow.create_window(self.corners[0], self.corners[1], window = l, anchor = SW, tag = "label")
            #lv = Label(MA.MP.paintWindow, text = self.resistance)
            #self.resistancelabel = MA.MP.paintWindow.create_window(self.corners[0], self.corners[1], window = lv, anchor = SE, tag = "label")
        
        print("Se puso el resistor")    
        #print(type(imgRes))

    def drawCable(self, side):
        global Simulating
        if MA.click == False:
            if side == 'right':
                MA.x1 = self.corners[2]
                MA.y1 = self.corners[1] + 12
                MA.component1 = self.resistorNode
                if Simulating:
                    self.w = popupWindowNode(self.root, MA.x1 + 10, MA.y1 - 10)
                    self.root.wait_window(self.w.top)
                    self.user_node_name = self.w.value

            elif side == 'left':
                MA.x1 = self.corners[0]
                MA.y1 = self.corners[1] + 12
                MA.component1 = self.resistorNode
                if Simulating:
                    self.w = popupWindowNode(self.root, MA.x1 - 10, MA.y1 - 10)
                    self.root.wait_window(self.w.top)
                    self.user_node_name = self.w.value


            elif side == 'top':
                MA.x1 = self.corners[0] + 12
                MA.y1 = self.corners[1]
                MA.component1 = self.resistorNode

                if Simulating:
                    self.w = popupWindowNode(self.root, MA.x1 + 10, MA.y1 )
                    self.root.wait_window(self.w.top)
                    self.user_node_name = self.w.value
            
            elif side == 'bottom':
                MA.x1 = self.corners[0] + 12
                MA.y1 = self.corners[3]
                MA.component1 = self.resistorNode
                if Simulating:
                    self.w = popupWindowNode(self.root, MA.x1 + 10, MA.y1 + 10)
                    self.root.wait_window(self.w.top)
                    self.user_node_name = self.w.value

        else:
            if not Simulating:
                if side == 'right':
                    c1 = Cable(self.root, MA.x1, MA.y1, self.corners[2], self.corners[1] + 12, MA.component1, self.resistorNode)
                    MA.ElectricCircuit.connect_components(MA.component1, self.resistorNode) 
                    MA.cablesList.append(c1)
                    
                
                elif side == 'left':
                    c2 = Cable(self.root, MA.x1, MA.y1, self.corners[0], self.corners[1] + 12, MA.component1, self.resistorNode)
                    MA.ElectricCircuit.connect_components(MA.component1, self.resistorNode)
                    MA.cablesList.append(c2)
                    
                
                
                elif side == 'top':
                    c3 = Cable(self.root, MA.x1, MA.y1, self.corners[0] + 12, self.corners[1], MA.component1, self.resistorNode)
                    MA.ElectricCircuit.connect_components(MA.component1, self.resistorNode)
                    MA.cablesList.append(c3)
                    

                elif side == 'bottom':
                    c4 = Cable(self.root, MA.x1, MA.y1, self.corners[0] +12, self.corners[3], MA.component1, self.resistorNode)
                    MA.ElectricCircuit.connect_components(MA.component1, self.resistorNode)
                    MA.cablesList.append(c4)
                
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
        #print(self._drag_data["item"])
        MA.MP.paintWindow.coords(self.namelabel, self.corners[0], self.corners[1])
        #MA.MP.paintWindow.coords(self.resistancelabel, self.corners[0], self.corners[1])

    def phb(self, event):
        if self.vertical == False:
            if event.x > self.corners[0] and event.x < self.corners[0] + 20 and event.y > self.corners[1] and event.y < self.corners[3]:
            #print(event.x , event.y)
            #self.x+=1
                print("max garro")
                self.drawCable('left')

                if MA.click == False:
                    MA.click = True
                else:
                    MA.click = False

            if event.x < self.corners[2] and event.x > self.corners[2] - 20 and event.y > self.corners[1] and event.y < self.corners[3]:
                print("cr7")    
                self.drawCable('right')  

                if MA.click == False:
                    MA.click = True
                else:
                    MA.click = False
        else:
            if event.x > self.corners[0] and event.x < self.corners[2] and event.y > self.corners[1] and event.y < self.corners[1] + 20:
            #print(event.x , event.y)
            #self.x+=1
                print("matt garro")
                self.drawCable('top')

                if MA.click == False:
                    MA.click = True
                else:
                    MA.click = False

            if event.x > self.corners[0] and event.x < self.corners[2] and event.y < self.corners[3] and event.y > self.corners[3] - 20:
                print("cr9")  
                self.drawCable('bottom')      

                if MA.click == False:
                    MA.click = True
                else:
                    MA.click = False
    
    def __init__(self, root, resistance, name, vertical):
        self.vertical = vertical
        self.root = root
        self._drag_data = {"x": 0, "y": 0, "item": None}
        self.resistance = int(resistance)
        self.name = name
        #self.cablesList = cablesList
        self.x = 50
        self.y = 50
        self.img = None
        self.corners = None
        self.namelabel = None
        self.resistancelabel = None
        self.resistorNode = Resistor(self.name, self.resistance)
        self.user_node_name = ""
        #self.negNode = Graph.Node()
        self.show_res()
        MA.MP.paintWindow.tag_bind(self.img, "<ButtonPress-1>", self.drag_start)
        MA.MP.paintWindow.tag_bind(self.img, "<ButtonRelease-1>", self.drag_stop)
        MA.MP.paintWindow.tag_bind(self.img, "<B1-Motion>", self.drag)
        MA.MP.paintWindow.tag_bind(self.img, "<Button-3>", self.phb)
        
class FuenteVoltajeGUI():
    def cargarimg(self, archivo): # Se carga imagen
        ruta = os.path.join('img', archivo)
        imagen = PhotoImage(file = ruta)
        return imagen

    def show_vol(self):
        if self.vertical == True:
            if self.name == "V0":
                volImage = self.cargarimg('GND.png')
                MA.volImg.append(volImage)
                MA.MP.paintWindow.image = volImage
                imgVol = MA.MP.paintWindow.create_image(random.randint(100, 600), random.randint(100,600), image = volImage, tag = "voltage")
                self.img = imgVol
                self.corners = MA.MP.paintWindow.bbox(imgVol)
                l = Label(MA.MP.paintWindow, text = self.name + "\n" + str(self.voltage) + "V")
                self.namelabel = MA.MP.paintWindow.create_window(self.corners[0], self.corners[1], window = l, anchor = SW, tag = "label")
            else: 
                volImage = self.cargarimg('FuenteVoltaje.png')
                MA.volImg.append(volImage)
                MA.MP.paintWindow.image = volImage
                imgVol = MA.MP.paintWindow.create_image(random.randint(100, 600), random.randint(100,600), image = volImage, tag = "voltage")
                self.img = imgVol
                self.corners = MA.MP.paintWindow.bbox(imgVol)
                l = Label(MA.MP.paintWindow, text = self.name + "\n" + str(self.voltage) + "V")
                self.namelabel = MA.MP.paintWindow.create_window(self.corners[0], self.corners[1], window = l, anchor = SW, tag = "label")
                #lv = Label(MA.MP.paintWindow, text = self.voltage)
                #self.voltagelabel = MA.MP.paintWindow.create_window(self.corners[0], self.corners[1], window = lv, anchor = SE, tag = "label")
        else:
            volImage2 = self.cargarimg('FuenteVoltaje2.png')            
            MA.volImg.append(volImage2)
            MA.MP.paintWindow.image = volImage2
            imgVol2 = MA.MP.paintWindow.create_image(random.randint(100, 600), random.randint(100,600), image = volImage2, tag = "voltage")
            self.img = imgVol2
            self.corners = MA.MP.paintWindow.bbox(imgVol2)
            l = Label(MA.MP.paintWindow, text = self.name + "\n" + str(self.voltage) + "V")  
            self.namelabel = MA.MP.paintWindow.create_window(self.corners[0], self.corners[1], window = l, anchor = SW, tag = "label")
             #lv = Label(MA.MP.paintWindow, text = self.voltage)
            #    self.voltagelabel = MA.MP.paintWindow.create_window(self.corners[0], self.corners[1], window = lv, anchor = SE, tag = "label")
        print("Se puso la fuente de voltaje")

    def drawCable(self, side):
        global Simulating
        if MA.click == False:
            if side == 'right':
                MA.x1 = self.corners[2]
                MA.y1 = self.corners[1] + 35
                MA.component1 = self.voltageNode

                if Simulating:
                    self.w = popupWindowNode(self.root, MA.x1 + 10, MA.y1 - 10)
                    self.root.wait_window(self.w.top)
                    self.user_node_name = self.w.value
                    print(self.user_node_name)

            elif side == 'left':
                MA.x1 = self.corners[0]
                MA.y1 = self.corners[1] + 35
                MA.component1 = self.voltageNode
                if Simulating:
                    self.w = popupWindowNode(self.root, MA.x1 - 10, MA.y1 - 10)
                    self.root.wait_window(self.w.top)
                    self.user_node_name = self.w.value
                    print(self.user_node_name)


            elif side == 'top':
                MA.x1 = self.corners[0] + 35
                MA.y1 = self.corners[1]
                MA.component1 = self.voltageNode
                if Simulating:
                    self.w = popupWindowNode(self.root, MA.x1 + 10, MA.y1)
                    self.root.wait_window(self.w.top)
                    self.user_node_name = self.w.value
                    print(self.user_node_name)
            
            elif side == 'bottom':
                MA.x1 = self.corners[0] + 35
                MA.y1 = self.corners[3]
                MA.component1 = self.voltageNode
                if Simulating:
                    self.w = popupWindowNode(self.root, MA.x1 + 10, MA.y1 + 10)
                    self.root.wait_window(self.w.top)
                    self.user_node_name = self.w.value
                    print(self.user_node_name)

        else:
            if not Simulating:
                if side == 'right':
                    c1 = Cable(self.root, MA.x1, MA.y1, self.corners[2], self.corners[1] + 35, MA.component1, self.voltageNode)
                    MA.ElectricCircuit.connect_components(MA.component1, self.voltageNode)
                    c1.voltage = self.voltageNode.get_val() 
                    MA.cablesList.append(c1)
                
                elif side == 'left':
                    c2 = Cable(self.root, MA.x1, MA.y1, self.corners[0], self.corners[1] + 35, MA.component1, self.voltageNode)
                    MA.ElectricCircuit.connect_components(MA.component1, self.voltageNode)
                    c2.voltage = self.voltageNode.get_val()
                    MA.cablesList.append(c2)
                
                elif side == 'top':
                    c3 = Cable(self.root, MA.x1, MA.y1, self.corners[0] + 35, self.corners[1], MA.component1, self.voltageNode)
                    MA.ElectricCircuit.connect_components(MA.component1, self.voltageNode)
                    c3.voltage = self.voltageNode.get_val()
                    MA.cablesList.append(c3)

                elif side == 'bottom':
                    c4 = Cable(self.root, MA.x1, MA.y1, self.corners[0] + 35, self.corners[3], MA.component1, self.voltageNode)
                    MA.ElectricCircuit.connect_components(MA.component1, self.voltageNode)
                    c4.voltage = self.voltageNode.get_val()
                    MA.cablesList.append(c4)

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
        MA.MP.paintWindow.coords(self.namelabel, self.corners[0], self.corners[1])
        #MA.MP.paintWindow.coords(self.voltagelabel, self.corners[0], self.corners[1])

    def phb(self, event):        
        if self.vertical == False:
            if event.x > self.corners[0] and event.x < self.corners[0] + 15 and event.y > self.corners[1] and event.y < self.corners[3]:
            #print(event.x , event.y)
            #self.x+=1
                print("max garro")
                self.drawCable('left')

                if MA.click == False:
                    MA.click = True
                else:
                    MA.click = False

            if event.x < self.corners[2] and event.x > self.corners[2] - 15 and event.y > self.corners[1] and event.y < self.corners[3]:
                print("cr7")        
                self.drawCable('right')  

                if MA.click == False:
                    MA.click = True
                else:
                    MA.click = False
        else:
            if event.x > self.corners[0] and event.x < self.corners[2] and event.y > self.corners[1] and event.y < self.corners[1] + 15:
            #print(event.x , event.y)
            #self.x+=1
                print("matt garro")
                self.drawCable('top')

                if MA.click == False:
                    MA.click = True
                else:
                    MA.click = False
                    
            if event.x > self.corners[0] and event.x < self.corners[2] and event.y < self.corners[3] and event.y > self.corners[3] - 15:
                print("cr9")        
                self.drawCable('bottom')      

                if MA.click == False:
                    MA.click = True
                else:
                    MA.click = False
    
     
    def __init__(self, root, voltage, name, vertical):
        self.vertical = vertical
        self.root = root
        self.voltage = int(voltage)
        self.name = name
        self.x = 50
        self.y = 50
        self.img = None
        self.corners = None
        self.namelabel = None
        self.voltagelabel = None
        self.user_node_name = ""
        self._drag_data = {"x": 0, "y": 0, "item": None}
        self.voltageNode = Voltage(self.name, self.voltage)
        self.show_vol()
        MA.MP.paintWindow.tag_bind(self.img, "<ButtonPress-1>", self.drag_start)
        MA.MP.paintWindow.tag_bind(self.img, "<ButtonRelease-1>", self.drag_stop)
        MA.MP.paintWindow.tag_bind(self.img, "<B1-Motion>", self.drag)
        MA.MP.paintWindow.tag_bind(self.img, "<Button-3>", self.phb)
        
class MainApplication():

    def __init__(self, parent):
        self.parent = parent
        self.nodeCount = 0
        self.DD = DropDown(self.parent)
        #self.simulating = self.DD.getsimulating()
        self.MP = MainPanel(self.parent)
        self.MP.grid()
        self.SB = SideBar(self.parent)
        #self.SB.grid()
        self.resList = LinkedList()
        self.resImg = []
        self.volList = []  
        self.volImg = []  
        self.cablesList = []
        self.click = False
        self.x1 = None
        self.y1 = None
        self.component1 = None
        self.ElectricCircuit = ElectricCircuit()
        
if __name__ == "__main__":
    root = Tk()
    root.geometry('1000x600')
    root.resizable(height= YES, width = YES)
    MA = MainApplication(root)
    root.mainloop()
