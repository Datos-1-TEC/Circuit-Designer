
from os import add_dll_directory
from Graph import *

#Clase que permite crear un netlist file con la información del circuito 
class NetlistExporter:
    def __init__(self,electric_components):
        self.electric_components_list = electric_components
        self.file = open("netlist_file.txt", "w")
        self.lines_on_file = []

    def create_netlist_file(self):
        """
        graph_nodes = self.graph.get_nodes()
        self.lines_on_file.append("* Netlist solution for circuit \n")
        lines = ""
        for node in graph_nodes:
            node_name = node.get_name()
            print(node_name)
            adj_nodes =  node.get_adjacent_nodes()
            for key,value in adj_nodes.items():
                print((key.get_name(),value))
                lines = node.get_name() + " " + str(value) + " " + "\n"
                self.lines_on_file.append(lines)
        self.file.writelines(self.lines_on_file)
        self.file.close()
        """
        lines = ""
        
        for component in self.electric_components_list:
            lines = component.get_name() + " " + component.get_adjacent_nodes_info() + "\n"

            self.lines_on_file.append(lines)
            self.file.writelines(lines)
            print(lines)

            #self.file.close()



"""
V1 = Node("V1")
node0 = Node("0")
node1 = Node("1")
node2 = Node("2")
node3 = Node("3")

V1.add_destination(node1,0,"R1")
node1.add_destination(node2,10,"R1")
node1.add_destination(node3,20,"R3")
node2.add_destination(node0,30,"R2")
node2.add_destination(node3,7.5,"R5")
node3.add_destination(node0,5,"R4")
node0.add_destination(V1,0,"V1")

graph = Graph()
graph.addNode(V1)
graph.addNode(node0)
graph.addNode(node1)
graph.addNode(node2)
graph.addNode(node3)

print("Nodos adyacentes de V1")
V1.print_adjacent_nodes()
print("------------------------------------")

print("Nodos adyacentes de node1")
node1.print_adjacent_nodes()
print("------------------------------------")

print("Nodos adyacentes de node2")
node2.print_adjacent_nodes()
print("------------------------------------")

print("Nodos adyacentes de node3")
node3.print_adjacent_nodes()
print("------------------------------------")

print("Nodos adyacentes de node0")
node0.print_adjacent_nodes()
print("------------------------------------")

graph.print_graph_nodes()

"""
R1  = Resistor("R1", 100)
R2  = Resistor("R2", 200)
R3  = Resistor("R3", 300)
R4 = Resistor("R4", 400)
V1 = Voltage("Source", 5)
V0 = Voltage("Ref", 0)


electric_components = []
electric_components.append(R1)
electric_components.append(R2)
electric_components.append(R3)
electric_components.append(R1)
electric_components.append(R4)
electric_components.append(V0)
electric_components.append(V1)


EC1 = ElectricCircuit()


EC1.create_voltage_link(V1, "C0")
EC1.create_resistor_link(R1, "C1")
EC1.create_resistor_link(R2, "C2")
EC1.create_resistor_link(R3, "C3")
EC1.create_resistor_link(R4, "C4")
EC1.create_voltage_link(V0, "C5")

EC1.connect_components(V0, V1)
EC1.connect_components(V1, R1)
EC1.connect_components(R1, R2)
EC1.connect_components(R1, R3)
EC1.connect_components(V1, R4)
EC1.connect_components(R4, EC1.search_ref_conn(V0.get_name()))
EC1.connect_components(R3, EC1.search_ref_conn(V0.get_name()))
EC1.connect_components(R2, V0)

#EC1.print_info()

#EC1.print_graph()


#print("Printing info...")
#EC1.print_info() 
"""
print("Adjacentes de resistencias: ")
print("R1->")
R1.print_adjacent_nodes()
print("R2->")
R2.print_adjacent_nodes()
print("R3->")
R3.print_adjacent_nodes()
print("R4->")
R4.print_adjacent_nodes()  
print("V0->")
V0.print_adjacent_nodes()
print("V1->")
V1.print_adjacent_nodes()
"""


file1 = NetlistExporter(electric_components)
file1.create_netlist_file()
