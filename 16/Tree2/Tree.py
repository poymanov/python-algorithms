class Tree:
	def __init__(self, depth):
		self.root = None
		self.depth = depth
		
	def search(self, value, node=None):
		if node == None:
			node = self.root

		if node.key == value:
			return [node, True]
		else:
			if value < node.key:
				if node.left_child:					
					return self.search(value, node.left_child)
				else:
					return [node, False, 'left']
			else:
				if node.right_child:
					return self.search(value, node.right_child)
				else:
					return [node, False, 'right']	
		
	def get_array_size(self):		
		childs = None
		array_size = 0

		for i in range(self.depth):				
			if childs == None:
				childs = 1
			else:
				childs *=2

			array_size += childs

		return array_size

	def iterate_node(self, node=None):
		if node is None:
			node = self.root
			yield node
		
		if node.left_child:					
			yield node.left_child

		if node.right_child:						
			yield node.right_child

		if node.left_child:
			for k in self.iterate_node(node.left_child):
				yield k	

		if node.right_child:
			for k in self.iterate_node(node.right_child):
				yield k