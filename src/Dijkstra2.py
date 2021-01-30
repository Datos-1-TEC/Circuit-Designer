import math

class Dijkstra2:

    def __init__(self,graph,source,target, shortestpath):
        self.unvisited_nodes = graph
        self.shortest_distance = {}
        self.route = []
        self.predecessor = {}
        self.shortestpath = shortestpath

        self.source = source
        self.target = target

    def get_path(self):
        
        # Iterating through all the unvisited nodes
        for nodes in self.unvisited_nodes:
            
        # Setting the shortest_distance of all the nodes as infinty
            self.shortest_distance[nodes]=math.inf
            
        # The distance of a point to itself is 0.
        self.shortest_distance[self.source]=0
        
        # Running the loop while all the nodes have been visited
        while(self.unvisited_nodes):
            
            # setting the value of min_node as None
            min_Node=None
            
            # iterating through all the unvisited node
            for current_node in self.unvisited_nodes: 
                
                if min_Node is None:
                    min_Node=current_node
                
                elif self.shortest_distance[min_Node] > self.shortest_distance[current_node]:
                    min_Node = current_node

            for child_node,value in self.unvisited_nodes[min_Node].items():
            
                if self.shortestpath:
                    if value + self.shortest_distance[min_Node] < self.shortest_distance[child_node]:  
                        
            
                        self.shortest_distance[child_node] = value + self.shortest_distance[min_Node]
                        
                
                        self.predecessor[child_node] = min_Node

                else:
                              
                    self.shortest_distance[child_node] = value + self.shortest_distance[min_Node]
                    
                    self.predecessor[child_node] = min_Node

            self.unvisited_nodes.pop(min_Node)
            
        # Till now the shortest distance between the source node and target node 
        # has been found. Set the current node as the target node 
        node = self.target
        
        # Starting from the goal node, we will go back to the source node and 
    # see what path we followed to get the smallest distance
        while node != self.source:
            
            # As it is not necessary that the target node can be reached from # the source node, we must enclose it in a try block
            try:
                self.route.insert(0,node)
                node = self.predecessor[node]
            except Exception:
                print('Path not reachable')
                break
        # Including the ssource in the path
        self.route.insert(0,self.source)
        
        # If the node has been visited,
        if self.shortest_distance[self.target] != math.inf:
            # print the shortest distance and the path taken
            print('Shortest distance is ' + str(self.shortest_distance[self.target]))
            print('And the path is ' + str(self.route))
        # Remove the below comment if you want to show the the shortest distance 
        #from source to every other node
        # print(shortest_distance)

    
    def get_route(self):
        return self.route
# graph = {'C1': {'C2': 1}, 'C7': {'C0': 10}, 'C5': {'C6': 4}, 'C2': {'C3': 5}, 'C4': {'C5': 1}, 'C0': {'C1': 4, 'C4': 4}, 'C3': {'C6': 4}, 'C6': {'C7': 0}}
# dj = Dijkstra2(graph, 'C0', 'C7', False)
# dj.get_path()


