from Graph import *
import random

class ElectricCircuit:
    """A class used to represent an Electric Circuit
        Atributtes-------------------
        graph_circuit: graph 
            data structure where connections between components in the Electric Circuit are made
        
        Methods----------------------
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
        self.connections_for_netlist = {}      

    def create_resistor_link(self, resistor, connection_name):
        """ Adds a destination Node to the resistor which will be used to make connections in the circuit
            & inserts that node to the graph_circuit
            Parameters--------------
            resistor: Resistor
            connection_name: str

        """
        connection = Node(connection_name)
        resistor.add_destination(connection, resistor.get_val())
        connection.set_voltage(random.randint(1, 5))
        volt = connection.get_voltage()
        connection.set_current(1000.0*(volt/int(resistor.get_val())))
        self.graph_circuit.addNode(connection)
    
    def create_voltage_link(self, voltage, connection_name):
        """ Adds a destination node to the voltage source which will be used to make connections in the circuit
            & inserts that node to the graph_circuit
            Parameters--------------
            voltage: Voltage
            connection_name: str

        """
        connection = Node(connection_name)
        voltage.add_destination(connection, 0)
        connection.set_voltage(voltage.get_val())
        connection.set_current(random.randint(1, 10))
        self.graph_circuit.addNode(connection)

    def connect_components(self, component1, component2):
        """ Establishes the real connection between two components through its links
            Parameters--------------
            component1: Resistor/Voltage
            component2: Resistor/Voltage
        """
        graph_nodes = self.graph_circuit.get_nodes()  
        connection1 = self.search_connection(component1)
        connection2 = self.search_connection(component2)
        

        if isinstance(component2, Resistor):
            connection1.add_destination(connection2, component2.get_val())

            print('Se conectaron' + component1.get_name(), component2.get_name())
            self.connections_for_netlist[component1.get_name()] = component2.get_name(),component2.get_val(), component1.get_val()
            print(self.connections_for_netlist)
            
        else:
            if component2.get_name() == "V0":
                connection2.set_voltage(0)
            connection1.add_destination(connection2, 0)
            self.connections_for_netlist[component1.get_name()] = component2.get_name(),component2.get_val(),component1.get_val()
            print(self.connections_for_netlist)


    def search_connection(self, component):
        """ Searches for the component's link
            Parameters--------------
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

    def get_connections_for_netlist(self):
        return self.connections_for_netlist

    def get_graph_as_dict(self):
        dict_graph = {}
        for node in self.graph_circuit.get_nodes():
            
            adj_nodes = node.get_adjacent_nodes()
            print("Printing adj_nodes")
            print(adj_nodes.items())
            adj_nodes_dict = {}
            for key, value in adj_nodes.items():
                
                adj_nodes_dict[key.get_name()] = key.get_voltage()
            dict_graph[node.get_name()] = adj_nodes_dict
                
        print(dict_graph)
        return dict_graph
    
class Resistor(Node):
    """ A class used to represent a resistor component of the circuit
        Atributtes-------------------
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
        Atributtes-------------------
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

