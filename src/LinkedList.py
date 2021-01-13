
class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None
	
	def get_data(self):
		return self.data

	def set_data(self, data):
		self.data = data
	
	def get_next(self):
		return self.next
	def set_next(self, next):
		self.next = next

class LinkedList(object):
	def __init__(self, head=None):
		self.head = head
		self.tail = None
		self.size = 0
		
	def print_list(self):
		if self.head == None:
			return "Lista vacía"

		current = self.head 
		while(current):
			print (current.data, end="  ")
			current = current.next
		print ('\n')

	def get_head(self):
		return self.head

	def get_tail(self):
		ref = self.head
		while ref.get_next() != None:
			ref = ref.get_next()
		self.tail = ref
		return self.tail

	def get_size(self):
		if self.head == None:
			return 0
		current = self.head
		while(current != None):
			self.size += 1
			current = current.next
		return self.size


	def insert(self, data):
		node = Node(data)
		if not self.head:
			self.head = node
		else:
			node.next = self.head
			self.head = node

	def append(self, new_data): 
		new_node = Node(new_data) 
		if self.head is None: 
			self.head = new_node 
			return
	
		last = self.head 
		while (last.next): 
			last = last.next
		last.next =  new_node
		
	def index(self, i):
		current = self.head
		cont = 0
		while current.next != None:
			if i == cont:
				return current
			else:
				current = current.next
				cont += 1


	def delete(self, data):
		if not self.head:
			return
		
		temp = self.head
		
		if self.head.data == data:
			head = temp.next
			print ("Se borró: " , head.data)
			return

		while(temp.next):
			if (temp.next.data == data):
				print ("Borrado: ", temp.next.data)
				temp.next = temp.next.next
				return 
			temp = temp.next
		print ("No se encontró nodo")
		return