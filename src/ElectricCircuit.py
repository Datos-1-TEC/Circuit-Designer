from Graph import *

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
            print('Se conectaron' + component1.get_name(), component2.get_name())
            
        else:
            connection1.add_destination(connection2, 0)

    def search_connection(self, component):
        nodes_dict = component.get_adjacent_nodes()
        for node, weight in nodes_dict.items():
            return node

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
        