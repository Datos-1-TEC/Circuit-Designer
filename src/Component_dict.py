class Component_dict: 
    """
    Class that works as a container used in a dictionary, this class allows to have multiple keys that are the same, this is highly important for the netlist implementation

    Attributes------------------------
    name : str, name of electric component 

    Methods---------------------------
    1. get_name() 
        returns name of the electric component
    """

    def __init__(self, name):
        self.name = name 

    def get_name(self):
        return self.name 
    
