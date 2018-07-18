class Tree:
	def __init__(self):
		self.root = None

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

	def iterate_node(self, node=None):
		if node is None:
			node = self.root

		yield node

		if node.left_child:
			for k in self.iterate_node(node.left_child):
				yield k

		if node.right_child:		
			for k in self.iterate_node(node.right_child):
				yield k

	def iterate_left_childs(self, node):
		yield node

		if node.left_child:
			for k in self.iterate_node(node.left_child):
				yield k

	def get_min_max(self, node=None):
		min_value = None
		max_value = None

		for node in self.iterate_node(node):
			current_key = node.key
			if not min_value: min_value = current_key
			if not max_value: max_value = current_key

			if current_key < min_value: 
				min_value = current_key
			elif current_key > max_value:
				max_value = current_key

		return {'min': min_value, 'max': max_value}	

	def delete(self, node):
		if node.right_child.left_child:
			self.delete_left(node)
		else:
			self.delete_right(node)

		node.parent = None
		node.left_child = None
		node.right_child = None			

	def delete_left(self, node):
		new_node = None

		for item in self.iterate_left_childs(node.right_child):
			if item == node: continue

			if item.left_child or item.right_child: continue

			new_node = item		
			break			

		new_node.parent = node.parent
		
		if node.parent.left_child == node:
			node.parent.left_child = new_node
		elif node.parent.right_child == node:
			node.parent.right_child = new_node

		new_node.left_child = node.left_child
		new_node.right_child = node.right_child

		node.left_child.parent = new_node
		node.right_child.parent = new_node

	def delete_right(self, node):		
		new_node = node.right_child

		new_node.parent = node.parent

		if node.parent.left_child == node:
			node.parent.left_child = new_node
		elif node.parent.right_child == node:
			node.parent.right_child = new_node		

		new_node.left_child = node.left_child
		node.left_child.parent = new_node