from Graph import Graph, Node
from LinkedList import LinkedList
import sys

class Dijkstra:
    def __init__(self):
        self.settledNodes = set()
        self.unsettledNodes = set()

    def calculateShortestPathFromSource(self,graph, source):
        source.set_distance(0)

        self.unsettledNodes.add(source)
        while(len(self.unsettledNodes)!=0):
            adjacencyPair = {} #EN LUGAR DE METER NODO:PESO >>>> NODO: VOLTAJE
            #currentNode = Node("")
            currentNode = self.getLowestDistanceNode(self.unsettledNodes)
            self.unsettledNodes.remove(currentNode)
            for n,i in currentNode.get_adjacent_nodes().items():
                adjacencyPair[n] = i
                adjacentNode = adjacencyPair.get(n)
                edgeWeight = adjacencyPair.get(i)
                if not self.settledNodes.__contains__(adjacentNode):
                    self.calculateMinimumDistance(adjacentNode,edgeWeight,currentNode)
                    self.unsettledNodes.add(adjacentNode)

            self.settledNodes.add(currentNode)

        return graph

    def getLowestDistanceNode(self, unsettledNodes):
        lowestDistanceNode = None
        lowestDistance = sys.maxsize
        for node in unsettledNodes:
            nodeDistance = node.get_distance()
            if nodeDistance < lowestDistance:
                lowestDistance = nodeDistance
                lowestDistanceNode = node

        return lowestDistanceNode

    def calculateMinimumDistance(self, evaluationNode, edgeWeight, sourceNode):
        sourceDistance = sourceNode.get_distance()
        #SUMAR VOLTAJES DE SOURCE MAS VOLTAJE ADYACENTE
        if sourceDistance + edgeWeight < evaluationNode.get_distance():
            evaluationNode.set_distance(sourceNode + edgeWeight)
            shortestPath = sourceNode.get_shortest_path()
            shortestPath.insert(sourceNode)
            evaluationNode.set_shortest_path(shortestPath)









    















                







