class Node():
	def __init__(self, v):
		self.value = v
		self.prev = None
		self.next = None

class List():
	def __init__(self):
		self.head = None
		self.tail = None

	def add_in_tail(self, item):
		if self.head is None:
			self.head = item
			item.prev = None
			item.next = None
		else:
			self.tail.next = item
			item.prev = self.tail
		self.tail = item					

	def delete_first_by_value(self, value):
		nodes = []

		node = self.head

		while node != None:								
			nodes.append(node)
			node = node.next		

		self.head = None
		self.tail = None

		for item in nodes:
			item.prev = None
			item.next = None

			if item.value == value: continue

			self.add_in_tail(item)

	def append_after(self, node, after):
		nodes = []

		item = self.head

		while item != None:								
			nodes.append(item)
			item = item.next		

		self.head = None
		self.tail = None

		for item in nodes:	
			item.prev = None
			item.next = None

			self.add_in_tail(item)

			if after is item:
				self.add_in_tail(node)

	def append_in_head(self, node):
		nodes = []

		item = self.head

		while item != None:								
			nodes.append(item)
			item = item.next		

		self.head = None
		self.tail = None

		self.add_in_tail(node)

		for item in nodes:	
			item.prev = None
			item.next = None

			self.add_in_tail(item)