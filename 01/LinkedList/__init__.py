class Node():
	def __init__(self, v):
		self.value = v
		self.next = None

class List():
	def __init__(self):
		self.head = None		
		self.tail = None

	def add_in_tail(self, item):
		if self.head is None:
			self.head = item
		else:
			self.tail.next = item
		self.tail = item
		
	def print_all_nodes(self):
		node = self.head
		while node != None:
			print(node.value)		
			node = node.next

	def find(self, val):
		node = self.head
		while node is not None:
			if node.value == val:
				return node
			node = node.next
		return None
						
	def delete_first_by_value(self, val): # 1.1
		nodes = []
		finded = None

		node = self.head
		while node != None:			
			if finded == None and node.value == val:
				finded = node
			else:
				nodes.append(node)							
			node = node.next					

		self.head = None
		self.tail = None
		finded.next = None

		for node in nodes:
			node.next = None
			self.add_in_tail(node)

	def delete_by_value(self, val): # 1.2
		nodes = []
		to_delete_nodes = []

		node = self.head
		while node != None:			
			if node.value == val:
				to_delete_nodes.append(node)
			else:
				nodes.append(node)

			node = node.next

		self.head = None
		self.tail = None	

		for node in nodes:
			node.next = None
			self.add_in_tail(node)

		for node in to_delete_nodes:
			node.next = None			

	def flush_all(self): # 1.3
		nodes = []

		node = self.head
		while node != None:			
			nodes.append(node)		
			node = node.next

		self.head = None
		self.tail = None

		for node in nodes:
			node.next = None

	def find_all(self, val): # 1.4
		nodes = []
		
		node = self.head
		while node is not None:
			if node.value == val: nodes.append(node)				
			node = node.next

		return nodes	

	def length(self): # 1.5
		length = 0

		node = self.head
		while node is not None:
			length += 1
			node = node.next	

		return length

	def append_after(self, newNode, afterNode):	# 1.6		
		nodes = []

		node = self.head
		while node is not None:
			nodes.append(node)

			if node is afterNode: nodes.append(newNode)
			node = node.next

		self.flush_all()
			
		for node in nodes:
			node.next = None
			self.add_in_tail(node)			

def sum_lists(list1, list2):
	if list1.length() != list2.length(): return None

	list1_values = []
	list2_values = []
	list_result = []

	node = list1.head
	while node is not None:
		list1_values.append(node.value)
		node = node.next

	node = list2.head
	while node is not None:
		list2_values.append(node.value)
		node = node.next		

	for i in range(len(list1_values)):
		value1 = list1_values[i]
		value2 = list2_values[i]
		list_result.append(value1 + value2)		

	return list_result


