class Node:
	def __init__(self, parent, key):
		self.parent = parent
		self.left_child = None
		self.right_child = None
		self.key = key

	def __repr__(self):
		return 'Node {}'.format(self.key)

	def add_left(self, node):
		if not node.key:
			raise ValueError('Node have empty key')

		if self.key < node.key:
			raise ValueError('Parent key less then node key')			

		if self.right_child and node.key > self.right_child.key:
			raise ValueError('Right child key less then node key')		

		self.left_child = node
		node.parent = self		

	def add_right(self, node):
		if not node.key:
			raise ValueError('Node have empty key')

		if self.key > node.key:
			raise ValueError('Parent key biggest then node key')			

		if self.left_child and node.key < self.left_child.key:
			raise ValueError('Left child key less then node key')	

		self.right_child = node
		node.parent = self	