import math

class Dijkstra2:

    def __init__(self,graph,source,target):
        self.unvisited_nodes = graph
        self.shortest_distance = {}
        self.route = []
        self.predecessor = {}

        self.source = source
        self.target = target

    def get_shortest_path(self):
        
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
                
            # For the very first time that loop runs this will be called
                if min_Node is None:
                
                # Setting the value of min_Node as the current node
                    min_Node=current_node
                    
                elif self.shortest_distance[min_Node] > self.shortest_distance[current_node]:
                    
                # I the value of min_Node is less than that of current_node, set 
                #min_Node as current_node

                    min_Node=current_node
                    
            # Iterating through the connected nodes of current_node (for # 
            #example, a is connected with b and c having values 10 and 3 
            # respectively) and the weight of the edges

            for child_node,value in self.unvisited_nodes[min_Node].items():

                # checking if the value of the current_node + value of the edge 
                # that connects this neighbor node with current_node
                # is lesser than the value that distance between current nodes 
                # and its connections
                if value + self.shortest_distance[min_Node] < self.shortest_distance[child_node]:  
                    
        # If true  set the new value as the minimum distance of that connection
                    self.shortest_distance[child_node] = value + self.shortest_distance[min_Node]
                    
            # Adding the current node as the predecessor of the child node
                    self.predecessor[child_node] = min_Node
            
            # After the node has been visited (also known as relaxed) remove it from unvisited node
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




