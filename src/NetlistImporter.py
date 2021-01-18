
class NetlistImporter:
    def __init__(self,file):
        self.file = file
        self.splited_list = self.file.split("/")
        self.file_name = self.splited_list[len(self.splited_list)-1]
        self.electric_components_list = []

    def get_electric_components_from_file(self):
        self.file = open(self.file_name, "r")
        self.lines = self.file.readlines()

        for line in self.lines:
            self.electric_components_list += [line]
            print(line)

        print("Returned list")
        print(self.electric_components_list)
        
        