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
    """****************************************************************************
    Methods----------
    1. simulate(self)
        Este metodo se activa cuando se presiona el boton "Simular", lo que hace es crear los botones del
        side bar que corresponden a cuando se pone en modo simulacion, ademas que colorea todos los cables
        en verde para demostrar que se estan asignando y activa el showtooltip.

    2. design(self)
        Se activa cuando se presiona el boton de "diseño" (se notan los cambios en el sidebar solo si
        se esta antes en el modo de simulacion). Lo que hace es poner los cables en negro y desactiva el
        showtooltip.

    3. generate_netlist(self)
        Se activa cuando se presiona el boton "generar netlist", y se encarga de crear un netlist.

    @method: import_netlist(self)
            permite que el usuario seleccione un archivo .txt para leerlo y hacer que los componentes electronicos aparezcan en el panel de diseño 

    @method: generate_netlist(self) 
        permite que se genere un archivo netlist con extension .txt, en este metodo se obtiene la información de las conexiones entre los componentes 

    @method: design(self) 
        permite alternar los modos diseño y simulación, en diseño los botones de creación de fuente de voltaje y resistencias y limpiar el panel de diseño aparecen disponibles 

    @method: simulate(self)
        permite alternar los modos diseño y simulación, en simulación aparecen los botones de obtención de camino más corto y más largo, nombrar nodos, y ordenar el nombre de las resistencias, ademas se permite que los cables del circuito se coloreen en verde para dar a entender al usuario que el modo simulación esta activo. Se hace disponible un tool tip al mover el mouse encima de los cables que muestra los valores en V y mA de cada cable

    ****************************************************************************"""
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
        #dd.menu.add_command(label = "Prueba dijsktra", command = self.test_dict)

        dd.pack(fill = BOTH)

class MainPanel(Canvas):
    """*********************************************************
    Methods-------------------
    1. grid(self)
        Crea lineas a lo largo y ancho de la pantalla para dar la ilusion que es un hoja cuadriculada.
    **********************************************************"""
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
    """**********************************************************
    Methods-------------------
    1. accept(self)
        crea el resistor con los valores que se ingresaron en los inputs.

    2. cleanup(self)
        limpia los inputs en los que se ingresan el nombre y valores de las resistencias.
    **********************************************************"""
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
    """***************************************************************************
    Methods--------------------------------
    1. accept2(self)
        crear las fuentes de voltaje con los nombres y valores ingresados en los inputs.

    2. cleanup2(self)
        limpia los inputs en los que se ingresan el nombre y valores de las fuentes de voltaje.
    ***************************************************************************"""
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
    """*******************************************************************
    Methods 
    1. addName(self, name)
        posiciona un label arriba del cable que muestra el nombre del nodo ingresado.
    
    2. accept(self)
        se agrega el nombre que se escribio en el input al label que se muestra arriba del cable.

    3. cleanup(self)
        limpia los inputs.
    *******************************************************************"""
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
    """*****************************************************************
    Methods---------------------------------
    1. cargarimg(self, archivo)
        se le ingresa una direccion de alguna imagen y retorna la imagen en cuestion.

    2. createImageButtons(self)
        crea los botones en el sidebar dependiendo de en cual condicion este el Simulating
    
    3. nameRes(self)
        se activa cuando se presiona el boton con la imagen de la resistencia

    4. get_connection_name(self)
        retorna el nombre del nodo conexion

    5. createResistor(self, value, name, vertical)
        -Se llama al metodo ElectricCircuit.create_resistor_link pasando como parametros Res1.resistorNode y self.connectionName
        -Agrega las imagenes a la pantalla y las agrega a una lista.
    
    6. nameVol(self)
        se activa cuando se presiona el boton con la imagen de la voltaje.

    7. createFuenteVoltaje(self, value, name, vertical)
        Agrega las imagenes a la pantalla y las agrega a una lista.

    8. cleanWin(self)
        elimina todas las imagenes y labels que se muestran en pantalla.
    
    9. minus_dijsktra(self)
        Despliega ventana para nombrar el nodo del principio y el del final.

    10. search_nodes(self)
        busca nodos ingresados en los entries, en el primer for se busca el nodo inicial
        y el otro for para el final del camino que se quiere recorrer.

    11. accept_dijkstra(self)
        Se llama al metodo search_nodes(self), y aplica el algoritmo de Dijsktra.

    12. show_res_names(self)
        Muestra la lista de resistencias de la forma ascendente y descendente dependiendo de cual boton presione.
    
    13. string_results(self, asc_list)
        Se encarga de concatenar los nombres para mostrarlos en un mensaje en la ventana de dialogo.

    14. createGround(self)
        Crea la tierra.

    *****************************************************************"""
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
        self.ok_buttton = Button(top, text = "Ok", command = self.accept_minus_dijkstra)
        self.ok_buttton.pack()
    
    def plus_dijsktra(self):
        top1 = self.top1 = Toplevel(self.root)
        self.front_label1 = Label(top1, text = "Nombre del nodo inicio")
        self.front_label1.pack()
        self.front_entry1 = Entry(top1)
        self.front_entry1.pack()
        self.end_label1 = Label(top1, text = "Nombre del nodo final")
        self.end_label1.pack()
        self.end_entry1 = Entry(top1)
        self.end_entry1.pack()
        self.ok_buttton1 = Button(top1, text = "Ok", command = self.accept_plus_dijkstra)
        self.ok_buttton1.pack()

    def search_nodes(self, start_entry, end_entry):
        start = start_entry
        end = end_entry
        self.C1 = ""
        self.C2 = ""
        for component in self.allElements:
            if len(self.allElements) > 10:
                if start == component.user_node_name and isinstance(component, ResistorGUI):
                    self.C1 = component.resistorNode.get_adjacent_nodes_info()[0] + component.resistorNode.get_adjacent_nodes_info()[1] + component.resistorNode.get_adjacent_nodes_info()[2]
                elif start == component.user_node_name and isinstance(component, FuenteVoltajeGUI):
                    self.C1 = component.voltageNode.get_adjacent_nodes_info()[0] + component.voltageNode.get_adjacent_nodes_info()[1] + component.voltageNode.get_adjacent_nodes_info()[2]
            else:
                if start == component.user_node_name and isinstance(component, ResistorGUI):
                    self.C1 = component.resistorNode.get_adjacent_nodes_info()[0] + component.resistorNode.get_adjacent_nodes_info()[1]
                elif start == component.user_node_name and isinstance(component, FuenteVoltajeGUI):
                    self.C1 = component.voltageNode.get_adjacent_nodes_info()[0] + component.voltageNode.get_adjacent_nodes_info()[1] 

                                 
            print("Nombre  nodo: ", self.C1)  

        for component in self.allElements:
            if len(self.allElements) > 10:
                if end == component.user_node_name and isinstance(component, ResistorGUI):
                    self.C2 = component.resistorNode.get_adjacent_nodes_info()[0] +component.resistorNode.get_adjacent_nodes_info()[1] + component.resistorNode.get_adjacent_nodes_info()[2]
                elif end == component.user_node_name and isinstance(component, FuenteVoltajeGUI):
                    self.C2 = component.voltageNode.get_adjacent_nodes_info()[0] + component.voltageNode.get_adjacent_nodes_info()[1] + component.voltageNode.get_adjacent_nodes_info()[2]
            else:
                if end == component.user_node_name and isinstance(component, ResistorGUI):
                    self.C2 = component.resistorNode.get_adjacent_nodes_info()[0] +component.resistorNode.get_adjacent_nodes_info()[1]
                elif end == component.user_node_name and isinstance(component, FuenteVoltajeGUI):
                    self.C2 = component.voltageNode.get_adjacent_nodes_info()[0] + component.voltageNode.get_adjacent_nodes_info()[1]

            print("Nombre  nodo: ", self.C2)
    
    def accept_minus_dijkstra(self):
        self.search_nodes(self.front_entry.get(), self.end_entry.get())
        C = ""
        graph = MA.ElectricCircuit.get_graph_as_dict()
        dj = Dijkstra2(graph, self.C1, self.C2, True)
        dj.get_path()
        pathNodes = dj.get_route()
        
        for node in pathNodes:
            for component in self.allElements:
                if isinstance(component, ResistorGUI):
                    if len(self.allElements) > 10: 
                        C = component.resistorNode.get_adjacent_nodes_info()[0] + component.resistorNode.get_adjacent_nodes_info()[1] + component.resistorNode.get_adjacent_nodes_info()[2]
                        if C == node:
                            self.shortestpath += component.name + "->"
                    else:
                        C = component.resistorNode.get_adjacent_nodes_info()[0] + component.resistorNode.get_adjacent_nodes_info()[1]
                        if C == node:
                            self.shortestpath += component.name + "->"

                elif isinstance(component, FuenteVoltajeGUI):
                    if len(self.allElements) > 10:
                        C = component.voltageNode.get_adjacent_nodes_info()[0] + component.voltageNode.get_adjacent_nodes_info()[1] + component.voltageNode.get_adjacent_nodes_info()[2]
                        if C == node:
                            self.shortestpath += component.name + "->"
                    else:
                        C = component.voltageNode.get_adjacent_nodes_info()[0] + component.voltageNode.get_adjacent_nodes_info()[1] 
                        if C == node:
                            self.shortestpath += component.name + "->"

        self.top.destroy()
        messagebox.showinfo("Shortest path", "El camino más corto es: \n" + self.shortestpath)
        self.shortestpath = " "
   
    def accept_plus_dijkstra(self):
        self.search_nodes(self.front_entry1.get(), self.end_entry1.get())
        C = ""
        graph = MA.ElectricCircuit.get_graph_as_dict()
        print("Las entradas son: ", self.C1, self.C2)
        dj = Dijkstra2(graph, self.C1, self.C2, False)
        dj.get_path()
        pathNodes = dj.get_route()
        
        for node in pathNodes:
            for component in self.allElements:
                if isinstance(component, ResistorGUI):
                    if len(self.allElements) > 10: 
                        C = component.resistorNode.get_adjacent_nodes_info()[0] + component.resistorNode.get_adjacent_nodes_info()[1] + component.resistorNode.get_adjacent_nodes_info()[2]
                        if C == node:
                            self.shortestpath += component.name + "->"
                    else:
                        C = component.resistorNode.get_adjacent_nodes_info()[0] + component.resistorNode.get_adjacent_nodes_info()[1]
                        if C == node:
                            self.shortestpath += component.name + "->"

                elif isinstance(component, FuenteVoltajeGUI):
                    if len(self.allElements) > 10:
                        C = component.voltageNode.get_adjacent_nodes_info()[0] + component.voltageNode.get_adjacent_nodes_info()[1] + component.voltageNode.get_adjacent_nodes_info()[2]
                        if C == node:
                            self.shortestpath += component.name + "->"
                    else:
                        C = component.voltageNode.get_adjacent_nodes_info()[0] + component.voltageNode.get_adjacent_nodes_info()[1] 
                        if C == node:
                            self.shortestpath += component.name + "->"

        self.top1.destroy()
        messagebox.showinfo("Longest path", "El camino más largo es: \n" + self.shortestpath)
        self.shortestpath = " "

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
        self.plusVolt = Button(self.window, text = "Buscar camino + tension", command = self.plus_dijsktra)                           
        self.minusVolt = Button(self.window, text = "Buscar camino - tension", command = self.minus_dijsktra)                           
        
        self.createImageButtons()
        self.x = 50
        self.y = 50
        self.shortestpath = ""

class Cable():
    """**********************************************************************
    Methods--------------------------------
    1. drawCable(self, x1, y1, x2, y2)
        Crea el cable en las coordenadas otorgadas.

    2. get_canvas_cable(self)
        Retorna el cable creado.

    3. showToolTip(self)
        Se activa cuando se posiciona el cursor encima de algun cable.

    4. showToolTipForNotSimulating(self)
        Si se posiciona el cursor encima de algun cable, se muestra un mensaje que 
        se debe cambiar a modo simulacion.

    **********************************************************************"""
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
    """*******************************************************
    Methods------------------------------
    1. cargarimg(self, archivo)
        se le ingresa una direccion de alguna imagen y retorna la imagen en cuestion.

    2. show_res(self)
        Carga la imagen de la resistencia y la muestra en pantalla, ademas que arriba de la imagen
        muestra el nombre y valor que se le asigno.

    3. drawCable(self, side)
        Dibuja un cable si se hace un click en alguno de los bordes de los dos objetos(resistencias o fuente de voltaje).

    4. drag_start(self, event)
        Se encarga de guardar el objeto y su localizacion para tener la referencia.

    5. drag_stop(self, event)
        Borra las referencias que se almacenaron en el drag_start(self, event) para poder
        volver a hacer drag a otros objetos.

    6. drag(self, event)
        Se encarga de mover el objeto con el mouse.

    7. phb(self, event)
        Dependiendo de en cual borde se haga click, se dibuja un cable hasta el segundo click en otro borde de otro elemento.

    *******************************************************"""
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
                print("Se ha efectuado un click")
                self.drawCable('left')

                if MA.click == False:
                    MA.click = True
                else:
                    MA.click = False

            if event.x < self.corners[2] and event.x > self.corners[2] - 20 and event.y > self.corners[1] and event.y < self.corners[3]:
                print("Se ha efectuado un click")    
                self.drawCable('right')  

                if MA.click == False:
                    MA.click = True
                else:
                    MA.click = False
        else:
            if event.x > self.corners[0] and event.x < self.corners[2] and event.y > self.corners[1] and event.y < self.corners[1] + 20:
            #print(event.x , event.y)
            #self.x+=1
                print("Se ha efectuado un click")
                self.drawCable('top')

                if MA.click == False:
                    MA.click = True
                else:
                    MA.click = False

            if event.x > self.corners[0] and event.x < self.corners[2] and event.y < self.corners[3] and event.y > self.corners[3] - 20:
                print("Se ha efectuado un click")  
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
    """***********************************************************************
    Methods------------------------------
    1. cargarimg(self, archivo)
        se le ingresa una direccion de alguna imagen y retorna la imagen en cuestion.

    2. show_vol(self)
        Carga la imagen de la fuente de voltaje y la muestra en pantalla, ademas que arriba de la imagen
        muestra el nombre y valor que se le asigno.

    3. drawCable(self, side)
        Dibuja un cable si se hace un click en alguno de los bordes de los dos objetos(resistencias o fuente de voltaje).

    4. drag_start(self, event)
        Se encarga de guardar el objeto y su localizacion para tener la referencia.

    5. drag_stop(self, event)
        Borra las referencias que se almacenaron en el drag_start(self, event) para poder
        volver a hacer drag a otros objetos.

    6. drag(self, event)
        Se encarga de mover el objeto con el mouse.

    7. phb(self, event)
        Dependiendo de en cual borde se haga click, se dibuja un cable hasta el segundo click en otro borde de otro elemento.
    ***********************************************************************"""
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
                print("Se ha efectuado un click")
                self.drawCable('left')

                if MA.click == False:
                    MA.click = True
                else:
                    MA.click = False

            if event.x < self.corners[2] and event.x > self.corners[2] - 15 and event.y > self.corners[1] and event.y < self.corners[3]:
                print("Se ha efectuado un click")        
                self.drawCable('right')  

                if MA.click == False:
                    MA.click = True
                else:
                    MA.click = False
        else:
            if event.x > self.corners[0] and event.x < self.corners[2] and event.y > self.corners[1] and event.y < self.corners[1] + 15:
            #print(event.x , event.y)
            #self.x+=1
                print("Se ha efectuado un click")
                self.drawCable('top')

                if MA.click == False:
                    MA.click = True
                else:
                    MA.click = False
                    
            if event.x > self.corners[0] and event.x < self.corners[2] and event.y < self.corners[3] and event.y > self.corners[3] - 15:
                print("Se ha efectuado un click")        
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
    root.title("Circuit Designer")
    root.geometry('1000x600')
    root.resizable(height= YES, width = YES)
    MA = MainApplication(root)
    root.mainloop()
