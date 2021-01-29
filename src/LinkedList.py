
class Node(object):
	"""***********************************************************
	Esta clase se encarga de almacenar las referencias del nodo actual y siguiente.
	***********************************************************"""
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
	"""**********************************************************************
	Esta clase usa la clase Node para implementar las operaciones(append, insert, entre otros).
	Methods---------------------------------------------
	1. print_list(self)
		muestra en la terminal todos los elementos de la lista, en caso de estar vacia, envia mensaje
		que dice que la lista esta vacia.

	2. get_head(self)
		retorna el nodo cabeza de la lista.

	3. get_tail(self)
		retorna la el nodo cola de la lista.

	4. get_size(self)
		retorna el tamaño de la lista.

	5. insert(self, data)
		inserta un nodo al principio de la lista.

	6. append(self, new_data)
		inserta un nodo al final de la lista.

	7. index(self, i)
		Para buscar un elemento en el indice dado.
	
	8. clear(self)
		Elimina todos los elementos en la lista.

	9. delete(self, data)
		Elimina un elemento en especifico.

	**********************************************************************"""
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
		self.size += 1  
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
		
		while i != cont:
			cont += 1
			current = current.get_next()
		return current
				

	def clear(self):

		while (self.head != None):
			temp = self.head
			self.head = self.head.get_next()
			temp = None

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

