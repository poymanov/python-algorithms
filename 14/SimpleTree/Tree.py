class Tree():
	def __init__(self, root):
		self.root = root

	def add_node(self, current, target):
		if self.root == target:
			raise Exception('Trying to remove root node')

		current.child.append(target)
		target.parent = current

	def delete_node(self, node):
		if self.root == node:
			raise Exception('Trying to delete root node')

		if node.parent is None:
			raise Exception('Node have not parent node')

		parent = node.parent
		parent.child += node.child

		for child in node.child:
			child.parent = parent

		parent.child.remove(node)

		node.parent = None
		node.child = []

	def iterate_node(self, node=None):
		if node is None:
			node = self.root

		yield node

		for item in node.child:						
			for k in self.iterate_node(item):
				yield k
		
		
	def iterate(self, node=None):		
		nodes = []		
		for node in self.iterate_node():
			nodes.append(node)

		return nodes

	def find_by_value(self, value):
		nodes = []		
		for node in self.iterate_node():
			if node.value == value:
				nodes.append(node)

		return nodes

	def info(self):
		nodes = 0
		leaves = 0

		for node in self.iterate_node():
			if node.child:
				nodes += 1
			else:
				leaves += 1

		return {'nodes': nodes, 'leaves': leaves}

	def set_levels(self):
		for node in self.iterate_node():
			if node == self.root:
				node.level = 0
			else:
				node.level = node.parent.level + 1