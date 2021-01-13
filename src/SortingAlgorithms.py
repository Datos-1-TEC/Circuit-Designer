from LinkedList import LinkedList

class SortingAlgorithms:
    def __init__(self, list):
        self.list = list
        self.sorted = None

    def get_list(self):
        return self.list
    #Orden descendente
    def insertion_Sort(self):

        current = self.list.get_head()
    
        while(current != None):
            next = current.get_next()
            self.sorted_element(current)
            current = next
        self.list.head = self.sorted

    def sorted_element(self, node):

        if self.sorted == None or self.sorted.get_data() <= node.get_data():
            node.set_next(self.sorted)
            self.sorted = node
        else:
            current = self.sorted
            while current.get_next() != None and current.get_next().get_data() > node.get_data():
                current = current.get_next()
            node.set_next(current.get_next())
            current.set_next(node)
    #Quick sort ascendente
    def partition(self, start, end):
        if (start == end or start == None or end == None):
            return start

        pivot_prev = start
        current = start
        pivot = end.get_data()

        while(start != end):

            if (start.get_data() < pivot ):
                pivot_prev = current
                tmp = current.get_data()
                current.set_data(start.get_data())
                start.set_data(tmp)
                current = current.get_next()
            start = start.get_next()
        tmp = current.get_data()
        current.set_data(pivot)
        end.set_data(tmp)
        return pivot_prev

    def quick_sort(self, start, end):

        if start == end:
            return
        pivot_prev = self.partition(start, end)
        self.quick_sort(start, pivot_prev)

        if pivot_prev != None and pivot_prev == start:
            self.quick_sort(pivot_prev.get_next(), end)


        
shortestPath = LinkedList()
shortestPath.append("R4")
shortestPath.append("R5")
shortestPath.append("R7")
shortestPath.append("R1")
shortestPath.append("R6")
shortestPath.append("R3")

print("\nBefore sorting")
shortestPath.print_list()

Sort = SortingAlgorithms(shortestPath)
print("After insertion sort")
Sort.insertion_Sort()
Sort.get_list().print_list()
print("After quick sort")
start = shortestPath.get_head()
end = shortestPath.get_tail()
Sort.quick_sort(start, end)
Sort.get_list().print_list()


        
    
