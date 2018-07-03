class Node():
	def __init__(self, v):
		self.value = v
		self.prev = None
		self.next = None

	def __repr__(self):
		return 'Node ({})'.format(self.value)	

class List():
	SORT_ASC = 'ASC'
	SORT_DESC = 'DESC'

	def __init__(self, sort = SORT_ASC):
		self.head = None
		self.tail = None
		self.sort = sort

	def add(self, item):
		nodes = []
		nodes.append(item)

		element = self.head

		while element != None:
			nodes.append(element)
			element = element.next	

		nodes = self.sort_nodes(nodes)
		
		self.head = None
		self.tail = None

		for node in nodes:
			node.next  = None
			node.prev = None
			self.add_in_tail(node)
						
	def sort_nodes(self, nodes):
		n = 1

		while n < len(nodes):
			for i in range(len(nodes)-n):
				if (self.sort == self.SORT_ASC and nodes[i].value > nodes[i+1].value) or (
					self.sort == self.SORT_DESC and nodes[i].value < nodes[i+1].value):
					nodes[i], nodes[i+1] = nodes[i+1], nodes[i]
			n += 1

		return nodes

	def add_in_tail(self, item):
		if self.head is None:
			self.head = item
			item.prev = None
			item.next = None
		else:
			self.tail.next = item
			item.prev = self.tail
		self.tail = item		

	def find(self, val):
		if self.sort == self.SORT_ASC:
			if self.head.value > val or self.tail.value < val: return None
		elif self.sort == self.SORT_DESC:
			if self.head.value < val or self.tail.value > val: return None

		node = self.head

		while node is not None:
			if node.value == val:
				return node
			node = node.next
		return None		

class ListStrings(List):
	def sort_nodes(self, nodes):
		n = 1

		while n < len(nodes):
			for i in range(len(nodes)-n):
				if (self.sort == self.SORT_ASC and nodes[i].value.strip() > nodes[i+1].value.strip()) or (
					self.sort == self.SORT_DESC and nodes[i].value.strip() < nodes[i+1].value.strip()):
					nodes[i], nodes[i+1] = nodes[i+1], nodes[i]
			n += 1

		return nodes