
#from os import add_dll_directory
from Graph import *

#Clase que permite crear un netlist file con la información del circuito 
class NetlistExporter:
    def __init__(self,connections_dictionary):
        self.electric_components_list = connections_dictionary
        self.file = open("netlist_file.txt", "w")
        self.lines_on_file = []

    def create_netlist_file(self):
        lines = "* electric circuit representation \n"
        for component,tuple in self.electric_components_list.items():
            component_connected,component_value,component_connected_value= tuple
            
            if "V" in component: 
                elecric_component_description = component_connected_value + " Volt Source"
            else:
                elecric_component_description = component_connected_value + " Ohm Resistor"

            lines += component + " " + component_connected + " " + component_value + " ; " + elecric_component_description + "\n"

            self.lines_on_file.append(lines)
        
        print("Printing from NetlistExporter Class")
        print(lines)
        print("Generating file...")
        self.file.writelines(lines)
        self.file.close()
        print("Done")



