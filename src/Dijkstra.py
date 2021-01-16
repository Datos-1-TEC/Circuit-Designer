from Graph import Graph, Node
from LinkedList import LinkedList
import sys

class Dijkstra:
    def __init__(self):
        self.settledNodes = set()
        self.unsettledNodes = set()

    def calculateShortestPathFromSource(self,graph, source):
        source.set_weight(0)

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
            nodeDistance = node.get_weight()
            if nodeDistance < lowestDistance:
                lowestDistance = nodeDistance
                lowestDistanceNode = node

        return lowestDistanceNode

    def calculateMinimumDistance(self, evaluationNode, edgeWeight, sourceNode):
        sourceDistance = sourceNode.get_weight()
        #SUMAR VOLTAJES DE SOURCE MAS VOLTAJE ADYACENTE
        print("sourceDistance: ", sourceDistance)
        print("edge: ", edgeWeight)
        print("eval: ", evaluationNode.get_weight())
        if sourceDistance + edgeWeight < evaluationNode.get_weight():
            evaluationNode.set_weight(sourceDistance + edgeWeight)
            shortestPath = sourceNode.get_shortest_path()
            shortestPath.insert(sourceNode)
            evaluationNode.set_shortest_path(shortestPath)

nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")

nodeA.add_destination(nodeB, 10)
nodeA.add_destination(nodeC, 15)

nodeB.add_destination(nodeD, 12)
nodeB.add_destination(nodeF, 15)

nodeC.add_destination(nodeE, 10)

nodeD.add_destination(nodeE, 2)
nodeD.add_destination(nodeF, 1)

nodeF.add_destination(nodeE, 5)


graph = Graph()

graph.addNode(nodeA)
graph.addNode(nodeB)
graph.addNode(nodeC)
graph.addNode(nodeD)
graph.addNode(nodeE)
graph.addNode(nodeF)

myDijsktra = Dijkstra()
graphh = myDijsktra.calculateShortestPathFromSource(graph, nodeB)








    















                







