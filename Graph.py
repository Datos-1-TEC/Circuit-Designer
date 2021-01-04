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

    def print_edges(self):
        edges = self.edges
        for key, value in edges.items():
            print(key.get_name(), ' : ', value)

    def print_graph_nodes(self):
        printedSet = []
        for x in self.nodes:
            printedSet += [x.get_name()]
        print(printedSet)

class Resistor:
    def __init__(self, name, val): 
        self.name = name
        self.val = val
        self.prev_node = Node("PREV")
        self.next_node = Node("NEXT")
        self.unit = "Ohms"

    def get_name(self):
        return self.name

    def get_val(self):
        return self.val
    
    def set_name(self, name):
        self.name = name
    
    def set_val(self, val):
        self.val = val

    def get_prev_node(self):
        return self.prev_node
    
    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, connection):
        self.next_node = connection

    def set_prev_node(self, connection):
        self.prev_node = connection

    def print_resistor(self):
        print("Resistor name: %s value: %s", self.get_name(), self.get_val(), self.unit)

class Voltage:
    def __init__(self, name, val): 
        self.name = name
        self.val = val
        self.prev_node = Node("PREV")
        self.next_node = Node("NEXT")
        self.reference = 0
        self.unit = "V"

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

    def get_prev_node(self):
        return self.prev_node
    
    def get_next_node(self):
        return self.next_node

    def print_voltage(self):
        print("Source name: %s value: %s", self.get_name(), self.get_val(), self.unit)

class CircuitExample:
    def __init__(self):
        self.name = "Ejemplo de circuito"
        self.resistorsList = LinkedList()
        self.voltSources = LinkedList()
        self.create_components()
        
    
    def create_components(self):

        R1  = Resistor("R1", 100)
        R2  = Resistor("R2", 200)
        R3  = Resistor("R3", 300)
        V1 = Voltage("Source", 5)

        V1.get_prev_node().set_name("0")
        V1.get_next_node().set_name("1")

        R1.set_prev_node(V1.get_next_node())
        R1.get_next_node().set_name("2")

        R2.set_prev_node(R1.get_next_node())
        R2.set_next_node(V1.get_prev_node())

        R3.set_prev_node(R2.get_prev_node())
        R3.set_next_node(V1.get_prev_node())

        circuitGraph = Graph()
        circuitGraph.addNode(R1.get_prev_node())
        circuitGraph.addNode(R1.get_next_node())
        circuitGraph.addNode(R2.get_next_node())

        circuitGraph.add_edge(R1.get_prev_node(), R1.get_next_node(), R1.get_val())
        circuitGraph.add_edge(R2.get_prev_node(), R2.get_next_node(), R2.get_val())
        circuitGraph.add_edge(R3.get_prev_node(), R3.get_next_node(), R3.get_val())

        circuitGraph.print_edges()


C1 = CircuitExample()





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
        

        


