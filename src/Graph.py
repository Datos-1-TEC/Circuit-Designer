from LinkedList import LinkedList
import sys
import random


class Node:
    def __init__(self,name):
        self.name = name 
        self.shortesPath = LinkedList()
        self.current = random.randint(1, 5)
        self.voltage = random.randint(1, 2)
        self.weight = sys.maxsize
        self.adjacentNodes = {}

    def add_destination(self,destination,weight):
        self.weight = weight
        self.adjacentNodes[destination] = self.weight
        if self.weight != 0:
            destination.set_voltage(destination.get_current()*self.weight)

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

    def get_weight(self):
        return self.weight

    def set_weight(self,weight):
        self.weight = weight
    
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




class Graph:
    def __init__(self):

        self.nodes = set()
        self.edges  = {}

    def addNode(self,node):
        self.nodes.add(node)

    def add_edge(self, start, end, weight):   
        if start not in self.edges:
            self.edges[start] = {}

        self.edges[start][end] = weight

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
             

      


