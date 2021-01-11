from Graph import *

class ElectricCircuit:
    """A class used to represent an Electric Circuit
        ----------------Atributtes-------------------
        graph_circuit: graph 
            data structure where connections between components in the Electric Circuit are made
        
        ----------------Methods----------------------
        1. create_resistor_link(resistor, connection_name):
            Adds a destination Node to the resistor which will be used to make connections in the circuit
            & inserts that node to the graph_circuit
        2. create_voltage_link(voltage, connection_name):
            Adds a destination node to the voltage source which will be used to make connections in the circuit
            & inserts that node to the graph_circuit
        3. connect_components(component1, component2):
            Establishes the real connection between two components through its links
        4. search_connection(component):
            Searches for the component's link 
        """
    def __init__(self):
        self.graph_circuit = Graph()     

    def create_resistor_link(self, resistor, connection_name):
        """ Adds a destination Node to the resistor which will be used to make connections in the circuit
            & inserts that node to the graph_circuit
            ----------------Parameters--------------
            resistor: Resistor
            connection_name: str

        """
        connection = Node(connection_name)
        resistor.add_destination(connection, resistor.get_val())
        self.graph_circuit.addNode(connection)
    
    def create_voltage_link(self, voltage, connection_name):
        """ Adds a destination node to the voltage source which will be used to make connections in the circuit
            & inserts that node to the graph_circuit
            ----------------Parameters--------------
            voltage: Voltage
            connection_name: str

        """
        connection = Node(connection_name)
        voltage.add_destination(connection, 0)
        self.graph_circuit.addNode(connection)

    def connect_components(self, component1, component2):
        """ Establishes the real connection between two components through its links
            ----------------Parameters--------------
            component1: Resistor/Voltage
            component2: Resistor/Voltage
        """
        graph_nodes = self.graph_circuit.get_nodes()  
        connection1 = self.search_connection(component1)
        connection2 = self.search_connection(component2)
        

        if isinstance(component2, Resistor):
            connection1.add_destination(connection2, component2.get_val())
            print('Se conectaron' + component1.get_name(), component2.get_name())
            
        else:
            connection1.add_destination(connection2, 0)

    def search_connection(self, component):
        """ Searches for the component's link
            ----------------Parameters--------------
            component1: Resistor/Voltage
            return: node, is the link we are looking for 
        """
        nodes_dict = component.get_adjacent_nodes()
        for node, weight in nodes_dict.items():
            return node

    def print_info(self):
        print("visto desde el grafo:")
        self.graph_circuit.print_graph_nodes()
        
    def get_graph(self):
        return self.graph_circuit
    
    def print_graph(self):
        self.graph_circuit.print_graph_nodes()
    
class Resistor(Node):
    """ A class used to represent a resistor component of the circuit
        ----------------Atributtes-------------------
        name: str, resistor name
        val: int, resistor value in ohms
        unit: str, SI unit for resistance

    """
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
    """ A class used to represent a resistor component of the circuit, inheritates from Node object
        ----------------Atributtes-------------------
        name: str, voltage source name
        val: int, voltage source value in Volts
        unit: str, SI unit for voltage
    """        

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

EC = ElectricCircuit()

print(EC.connect_components.__doc__)