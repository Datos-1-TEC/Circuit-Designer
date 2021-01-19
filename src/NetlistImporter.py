
class NetlistImporter:
    def __init__(self,file):
        self.file = file
        self.splited_list = self.file.split("/")
        self.file_name = self.splited_list[len(self.splited_list)-1]
        self.electric_components_list = []
        

    def enlist_electric_components(self):
        self.file = open(self.file_name, "r")
        self.lines = self.file.readlines()

        for line in self.lines:
            self.electric_components_list += [line]

        print("Returned list")
        self.electric_components_list.pop(0)
        print(self.electric_components_list)
        return self.electric_components_list

    def get_electric_components_to_create(self):
        self.electric_elements_to_create = []
        self.components_list = self.enlist_electric_components()

        for component in self.components_list: 
            #print("Show name from netlist")
            #print(str(component).split(" ")[0])
            component_name = str(component).split(" ")[0]
            #print(str(component).split(";")[1])
            electric_component = str(component).split(";")[1]
            #print(electric_component.split(" "))
            electric_component = electric_component.split(" ")
            #print(electric_component[1],electric_component[3].replace("\n",""))
            self.electric_elements_to_create.append((electric_component[1],electric_component[3].replace("\n",""),component_name))

        print(self.electric_elements_to_create)
        return self.electric_elements_to_create




            




    
        