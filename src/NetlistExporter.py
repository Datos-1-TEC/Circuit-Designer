from tkinter import messagebox
from Graph import *

#Clase que permite crear un netlist file con la información del circuito 
class NetlistExporter:

    """
    Class used to create or export a netlist file with a .txt extension 
    Atributtes------------------- 
    parent: Tk(), window root
    electric_components_list : dictionary, connections made during the components connections
    file: list, file, file to write the data 
    lines_on_file : list, list with the lines to write in the file
    
    Methods----------------------
    1. create_netlist_file() 
        create a txt file with the info from the circuit
    """

    def __init__(self,connections_dictionary,parent):
        self.parent = parent 
        self.electric_components_list = connections_dictionary
        self.file = open("netlist_file.txt", "w")
        self.lines_on_file = []

    def create_netlist_file(self):
        if self.electric_components_list == {}:
            print("Netlist file can't be created because there are not electric elements or electric elements are not connected")
            messagebox.showerror('Netlist File Creation Error', "Netlist file can't be created because there are no electric elements or electric elements are not connected \nCreate a circuit to export a Netlist File", parent=self.parent)
        else:
            lines = "* electric circuit representation \n"
            for component,tuple in self.electric_components_list.items():
                component_connected,component_value,component_connected_value= tuple
                
                if "V" in component.get_name(): 
                    elecric_component_description = str(component_connected_value) + " Volt Source"
                else:
                    elecric_component_description = str(component_connected_value) + " Ohm Resistor"

                lines += component.get_name() + " " + component_connected + " " + str(component_value) + " ; " + elecric_component_description + "\n"

                self.lines_on_file.append(lines)
            
            print("Printing from NetlistExporter Class")
            print(lines)
            print("Generating file...")
            self.file.writelines(lines)
            self.file.close()
            print("Done")
            messagebox.showinfo("Netlist Created", "Netlist File has been created succesfully")

