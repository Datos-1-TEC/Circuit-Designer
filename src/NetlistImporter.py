from tkinter import messagebox
from tkinter import *


class NetlistImporter:
    def __init__(self,file,parent):
        self.parent = parent
        self.file = file
        self.splited_list = self.file.split("/")
        self.file_name = self.splited_list[len(self.splited_list)-1]
        self.electric_components_list = []
        

    def enlist_electric_components(self):
        self.file = open(self.file_name, "r")
        self.lines = self.file.readlines()

        if self.lines == []:
            messagebox.showerror('Netlist File Reading Error', "Netlist file can't be read because the file is empty, make sure the Netlist File does not have any errors", parent=self.parent)
        else:
            for line in self.lines:
                self.electric_components_list += [line]

        print("Returned list")
        self.electric_components_list.pop(0)
        print(self.electric_components_list)
        return self.electric_components_list

    def get_electric_components_to_create(self):
        self.electric_elements_to_create = []
        self.elements_to_be_created =  set()
        self.components_list = self.enlist_electric_components()

        for component in self.components_list: 
            #print("Show name from netlist")
            #print(str(component).split(" ")[0])
            component_name = str(component).split(" ")[0]
            #print(str(component).split(";")[1])
            electric_component = str(component).split(";")[1]
            #print(electric_component.split(" "))
            electric_component = electric_component.split(" ")
            #print(electric_component[1],electric_component[3].replace("\n",""))
            self.electric_elements_to_create.append((electric_component[1],electric_component[3].replace("\n",""),component_name))

            self.elements_to_be_created.add((electric_component[1],electric_component[3].replace("\n",""),component_name))

        #print(self.electric_elements_to_create)
        
        return self.elements_to_be_created


    def show_connections_from_netlist(self):
        self.connections_list = self.electric_components_list
        #print(connections_list
        message = "Netlist connections\n"

        for connection in self.connections_list:
            #print(connection.split(" "))
            components_connections = connection.split(" ")
            #print(components_connections[0],components_connections[1])
            message += components_connections[0] + " -> " + components_connections[1] + "\n"

        popup = popupWindowConnections(self.parent,message)

class popupWindowConnections(object):
    def __init__(self, master,message):
        top = self.top = Toplevel(master)
        top.geometry("200x100")
        self.label = Label(top,text=message)
        self.label.pack()




            




    
        