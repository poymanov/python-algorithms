class Tree:
	def __init__(self, depth, root):
		size = self.get_array_size(depth)
		self.data = [None] * size
		self.data[0] = root

	def get_left_index(self, parent_index):
		return 2 * parent_index + 1

	def get_right_index(self, parent_index):
		return 2 * parent_index + 2

	def get_array_size(self, depth):		
		childs = None
		array_size = 0

		for i in range(depth):				
			if childs == None:
				childs = 1
			else:
				childs *=2

			array_size += childs

		return array_size	

	def add_left(self, parent, child):
		if not parent in self.data:
			raise 'Unknown parent'			

		parent_index = self.data.index(parent)	

		left_index = self.get_left_index(parent_index)
		right_index = self.get_right_index(parent_index)

		try:
			left_value = self.data[left_index]	
		except:
			raise 'Failed to found slot for child'

		if parent < child:
			raise ValueError('Parent value less then child value')		

		right_value = self.data[right_index]	

		if right_value and child > right_value:
			raise ValueError('Right child key less then node key')		

		self.data[left_index] = child			

	def add_right(self, parent, child):
		if not parent in self.data:
			raise 'Unknown parent'			

		parent_index = self.data.index(parent)
		right_index = self.get_right_index(parent_index)

		try:
			right_value = self.data[right_index]	
		except:
			raise 'Failed to found slot for child'

		if parent > child:
			raise ValueError('Parent value biggest then child value')				

		self.data[right_index] = child

	def add(self, value):
		value_index = self.search(value)

		if value_index is None:
			raise 'Failed to found slot for child'

		if self.data[value_index] is not None:
			raise 'Element already in tree'	

		self.data[value_index] = value

		return True		
		
	def search(self, value, parent = None):
		if parent == None:
			parent = self.data[0]

		parent_index = self.data.index(parent)

		if parent == value:
			return parent_index		
		else:
			if value < parent:			
		 		index = self.get_left_index(parent_index)
			else:
				index = self.get_right_index(parent_index)	 

			try:
				next_value = self.data[index]

				if next_value == None:
					return index
				else:		
					return self.search(value, self.data[index])
			except:
				return None	