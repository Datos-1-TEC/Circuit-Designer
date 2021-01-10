from LinkedList import LinkedList
import sys
import random


class Node:
    def __init__(self,name):
        self.name = name 
        self.shortesPath = LinkedList()
        self.current = random.randint(1, 5)
        self.voltage = random.randint(1, 2)
        self.distance = sys.maxsize
        self.adjacentNodes = {}

    def add_destination(self,destination,distance):
        self.distance = distance
        self.adjacentNodes[destination] = self.distance
        if self.distance != 0:
            destination.set_voltage(destination.get_current()*self.distance)

    def get_name(self):
        return self.name
    
    def set_name(self,name):
        self.name = name 

    def get_shortest_path(self):
        return self.shortesPath
    def get_voltage(self):
        return self.voltage
    def get_current(self):
        return self.current   
    def set_shortest_path(self,shortest_path):
        self.shortesPath = shortest_path
    def set_voltage(self, voltage):
        self.voltage = voltage

    def get_distance(self):
        return self.distance

    def set_distance(self,distance):
        self.distance = distance
    
    def get_adjacent_nodes(self):
        return self.adjacentNodes
    
    def set_adjacent_nodes(self,adjacent_nodes):
        self.adjacentNodes = adjacent_nodes

    def print_adjacent_nodes(self):
        adj_nodes = self.get_adjacent_nodes()
        for key, value in adj_nodes.items():
            print(key.get_name(), ' : ', value, "V: ", key.get_voltage())

    def get_adjacent_nodes_info(self):
        adj_nodes = self.get_adjacent_nodes()
        for key, value in adj_nodes.items():
            return key.get_name() + " " + str(value)


    def get_electric_component(self):
        return self.electric_component



class Graph:
    def __init__(self):

        self.nodes = set()
        self.edges  = {}

    def addNode(self,node):
        self.nodes.add(node)

    def add_edge(self, start, end, distance):   
        if start not in self.edges:
            self.edges[start] = {}

        self.edges[start][end] = distance

    def get_nodes(self):
        return self.nodes

    def print_edges(self):
        edges = self.edges
        for key, value in edges.items():
            print(key.get_name(), ' : ', value)

    def print_graph_nodes(self):
        printedSet = []
        for x in self.nodes:
            
            print("My node: " + x.get_name())
                
            print("nodos adyacentes: ")
            x.print_adjacent_nodes()
             

class Resistor(Node):
    def __init__(self, name, val): 
        self.name = name
        self.val = val
        self.unit = "Ohms"
        Node.__init__(self, name)

    def get_name(self):
        return self.name

    def get_val(self):
        return self.val
    
    def set_name(self, name):
        self.name = name
    
    def set_val(self, val):
        self.val = val

    def print_resistor(self):
        print("Resistor name: %s value: %s", self.get_name(), self.get_val(), self.unit)

class Voltage (Node):
    def __init__(self, name, val): 
        self.name = name
        self.val = val
        self.unit = "V"
        Node.__init__(self, name)

    def get_name(self):
        return self.name

    def get_val(self):
        return self.val
    
    def get_reference(self):
        return self.reference
    
    def set_name(self, name):
        self.name = name
    
    def set_val(self, val):
        self.val = val

    def print_voltage(self):
        print("Source name: %s value: %s", self.get_name(), self.get_val(), self.unit)

class CircuitExample:
    def __init__(self):
        self.name = "Ejemplo de circuito"
        self.resistorsList = LinkedList()
        self.voltSources = LinkedList()
        self.create_components()
        
    
    def create_components(self):
       
        C0 = Node("C0")
        C1 = Node("C1")
        C2 = Node("C2")
        C3 = Node("C3")     

        R1  = Resistor("R1", 100)
        R2  = Resistor("R2", 200)
        R3  = Resistor("R3", 300)
        V1 = Voltage("Source", 5)
        V0 = Voltage("Ref", 0)

        V0.add_destination(C0, 0)
        C0.add_destination(V1, 0)
        V1.add_destination(C1, 0)
        C1.add_destination(R1, R1.get_val())
        R1.add_destination(C2, 0)
        C2.add_destination(R2, R2.get_val())
        R2.add_destination(V0, 0)
        R1.add_destination(C3, 0)
        C3.add_destination(R3, R3.get_val())
        R3.add_destination(V0, 0)

        circuitGraph = Graph()
        circuitGraph.addNode(C0)
        circuitGraph.addNode(C1)
        circuitGraph.addNode(C2)
        circuitGraph.addNode(C3)
        print("Vista desde cada nodo")
        C0.print_adjacent_nodes()
        C1.print_adjacent_nodes()
        C2.print_adjacent_nodes()
        C3.print_adjacent_nodes()
        print("Vista desde el grafo")
        circuitGraph.print_graph_nodes()



#C1 = CircuitExample()
class ElectricCircuit:
    def __init__(self):
        self.graph_circuit = Graph()     

    def create_resistor_link(self, resistor, connection_name):
        connection = Node(connection_name)
        resistor.add_destination(connection, resistor.get_val())
        self.graph_circuit.addNode(connection)
    
    def create_voltage_link(self, voltage, connection_name):
        connection = Node(connection_name)
        voltage.add_destination(connection, 0)
        self.graph_circuit.addNode(connection)

    def connect_components(self, component1, component2):
        graph_nodes = self.graph_circuit.get_nodes()  
        connection1 = self.search_connection(component1)
        connection2 = self.search_connection(component2)

        if isinstance(component2, Resistor):
            connection1.add_destination(connection2, component2.get_val())
        else:
            connection1.add_destination(connection2, 0)

    def search_connection(self, component):
        nodes_dict = component.get_adjacent_nodes()
        for node, weight in nodes_dict.items():
            return node

    def search_ref_conn(self, element_name):
        nodes = self.graph_circuit.get_nodes()
        target = Node("target")
        for node in nodes:
            for key, value in node.get_adjacent_nodes().items():
                if key.get_name() == element_name:
                    target = node
        return target

    def print_info(self):
        print("visto desde el grafo:")
        self.graph_circuit.print_graph_nodes()

        """  print("visto desde los nodos conexion:")
        for node in self.graph_circuit.get_nodes():
            if node != None:
                print("node name: ", node.get_name())
                node.print_adjacent_nodes()
                 """
        

    def get_graph(self):
        return self.graph_circuit
    

    def print_graph(self):
        self.graph_circuit.print_graph_nodes()
    

R1  = Resistor("R1", 100)
R2  = Resistor("R2", 200)
R3  = Resistor("R3", 300)
R4 = Resistor("R4", 400)
V1 = Voltage("Source", 5)
V0 = Voltage("Ref", 0)
EC1 = ElectricCircuit()

EC1.create_voltage_link(V1, "C0")
EC1.create_resistor_link(R1, "C1")
EC1.create_resistor_link(R2, "C2")
EC1.create_resistor_link(R3, "C3")
EC1.create_resistor_link(R4, "C4")
EC1.create_voltage_link(V0, "C5")

EC1.connect_components(V0, V1)
EC1.connect_components(V1, R1)
EC1.connect_components(V1, R4)
EC1.connect_components(R1, R2)
EC1.connect_components(R1, R3)
EC1.connect_components(R4, V0)
EC1.connect_components(R3, V0)
EC1.connect_components(R2, V0)

EC1.print_info()

        


