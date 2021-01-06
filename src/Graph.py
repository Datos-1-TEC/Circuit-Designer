from LinkedList import LinkedList
import sys


class Node:
    def __init__(self,name):
        self.name = name 
        self.shortesPath = LinkedList()
        self.distance = sys.maxsize
        self.adjacentNodes = {}

    def add_destination(self,destination,distance):
        self.distance = distance
        self.adjacentNodes[destination] = self.distance

    def get_name(self):
        return self.name
    
    def set_name(self,name):
        self.name = name 

    def get_shortest_path(self):
        return self.shortesPath

    def set_shortest_path(self,shortest_path):
        self.shortesPath = shortest_path
    
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
            print(key.get_name(), ' : ', value)

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
            print(x.get_name(), ";", x.get_distance())
            printedSet += [x.get_name()]
        print(printedSet)

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
        self.V0 = Voltage("Ref", 0)
        self.graph_circuit.addNode(self.V0)        

    def create_resistor_link(self, resistor, connection_name):
        connection = Node(connection_name)
        connection.add_destination(resistor, resistor.get_val())
        self.graph_circuit.addNode(connection)
    
    def create_voltage_link(self, voltage, connection_name):
        connection = Node(connection_name)
        connection.add_destination(voltage, 0)
        self.graph_circuit.addNode(connection)

    def connect_components(self, component1, component2):
        graph_nodes = self.graph_circuit.get_nodes()  

        for node in graph_nodes:
            for adjNode in node.get_adjacent_nodes():
                if adjNode.get_name() == component2.get_name():
                    component1.add_destination(component2, 0)

    def get_V0 (self):
        return self.V0

    def print_info(self):
        print("visto desde los nodos conexion:")
        for node in self.graph_circuit.get_nodes():
            print(node.print_adjacent_nodes())
        print("visto desde el grafo:")
        self.graph_circuit.print_graph_nodes()

R1  = Resistor("R1", 100)
R2  = Resistor("R2", 200)
R3  = Resistor("R3", 300)
V1 = Voltage("Source", 5)

EC1 = ElectricCircuit()

EC1.create_voltage_link(V1, "C0")
EC1.create_resistor_link(R1, "C1")
EC1.create_resistor_link(R2, "C2")
EC1.create_resistor_link(R3, "C3")
EC1.connect_components(R1, R2)
EC1.connect_components(R1, R3)
EC1.connect_components(EC1.get_V0(), V1)
EC1.connect_components(V1, R1)
EC1.connect_components(R2, EC1.get_V0())
EC1.connect_components(R3, EC1.get_V0())
EC1.print_info()
  
""" nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")

nodeA.add_destination(nodeB,10)
nodeA.add_destination(nodeC,15)

nodeB.add_destination(nodeD,12)
nodeB.add_destination(nodeF,15)

nodeC.add_destination(nodeE,10)

nodeD.add_destination(nodeE,2)
nodeD.add_destination(nodeF,1)

nodeF.add_destination(nodeE,5)


print("method get_adjacent_nodes()")
print(nodeB.get_adjacent_nodes())
print(nodeB.get_distance())
print(nodeB.get_name()) 



nodeA.print_adjacent_nodes()


graph = Graph()

graph.addNode(nodeA)
graph.addNode(nodeB)
graph.addNode(nodeC)
graph.addNode(nodeD)
graph.addNode(nodeE)
graph.addNode(nodeF)

graph.add_edge(nodeA, nodeB, 10)
graph.add_edge(nodeA, nodeC, 15)

graph.add_edge(nodeB, nodeD, 12)
graph.add_edge(nodeB, nodeF, 15)

graph.add_edge(nodeC, nodeE, 10)

graph.add_edge(nodeD, nodeE, 2)
graph.add_edge(nodeD, nodeF, 1)

graph.add_edge(nodeF, nodeE, 5)

graph.print_edges()




#graph.print_graph_nodes()


print("done") """
        

        


