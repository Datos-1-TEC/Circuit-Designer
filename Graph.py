from typing import List
import sys


class Node:
    def __init__(self,name):
        self.name = name 
        self.shortesPath = list()
        self.distance = sys.maxsize
        self.adjacentNodes = {}

    def add_destination(self,destination,distance):
        self.adjacentNodes[destination] = distance

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


class Graph:
    def __init__(self):
        self.nodes = set()

    def addNode(self,node):
        self.nodes.add(node)

    
    


nodeA = Node("A")
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

graph = Graph()

graph.addNode(nodeA)
graph.addNode(nodeB)
graph.addNode(nodeC)
graph.addNode(nodeD)
graph.addNode(nodeE)
graph.addNode(nodeF)

print("done")
        

        


