from Graph import Graph, Node

class Dijkstra:
    def __init__(self):
        self.settledNodes = set()
        self.unsettledNodes = set()



    def calculateShortestPathFromSource(self,graph, source):
        source.set_distance(0)

        self.unsettledNodes.add(source)
        while(len(self.unsettledNodes)!=0):
            currentNode = getLowestDistanceNode(self.unsettledNodes)
            self.unsettledNodes.remove(currentNode)






