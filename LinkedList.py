
class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList(object):
	def __init__(self, head=None):
		self.head = head

	#ubicación del nodo
	def search(self, head, data, index):
		if head.data == data:
			print (index)
		else:
			
			if head.next:
				return self.search(head.next, data, index+1)
			else:
				return "Nodo no está en lista"

	
	def print_list(self):
		if self.head == None:
			return "Lista vacía"

		current = self.head 
		while(current):
			print (current.data, end="  ")
			current = current.next
		print ('\n')


	def size(self):
		if self.head == None:
			return 0

		size = 0
		current = self.head
		while(current):
			size += 1
			current = current.next

		return size


	def insert(self, data):
		node = Node(data)
		if not self.head:
			self.head = node
		else:
			node.next = self.head
			self.head = node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = new_node;

	def delete(self, data):
		if not self.head:
			return
		
		temp = self.head
		
		if self.head.data == data:
			head = temp.next
			print ("Se borró " + str(head.data))
			return

		while(temp.next):
			if (temp.next.data == data):
				print ("Borrado" + str(temp.next.data))
				temp.next = temp.next.next
				return
			temp = temp.next
		print ("No se encontró nodo")
		return


shortestPath = LinkedList()
shortestPath.insert("a")
shortestPath.insert("b")
shortestPath.insert("c")
shortestPath.insert("d")
shortestPath.insert("e")
shortestPath.insert("f")
shortestPath.print_list()