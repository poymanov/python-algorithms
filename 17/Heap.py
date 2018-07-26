class Heap:
	def __init__(self, depth, root):
		size = self.get_array_size(depth)
		self.data = [None] * size
		self.data[0] = root

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

	def add(self, value):
		if not value in self.data:
			index = self.data.index(None)
		else:
			index = self.data.index(value)

		if index == 0: return None

		self.data[index] = value

		parent_index = (index - 1) // 2

		parent_value = self.data[parent_index]

		if value > parent_value:
			self.data[parent_index] = value
			self.data[index] = parent_value
			return self.add(value)

	def delete_max(self, value = None):
		if value == None:
			data_without_none = list(filter(lambda v: v is not None, self.data))
			last_element = data_without_none[-1]
			last_element_index = self.data.index(last_element)
			self.data[0] = last_element
			self.data[last_element_index] = None
			value = last_element

		value_index = self.data.index(value)

		left_child_index = 2 * value_index + 1
		right_child_index = 2 * value_index + 2

		left_child_value = self.data[left_child_index]
		right_child_value = self.data[right_child_index]

		if left_child_value is not None and value < left_child_value:
			self.data[left_child_index] = value
			self.data[value_index] = left_child_value
			return self.delete_max(value)
		elif right_child_value is not None and value < right_child_value:
			self.data[right_child_index] = value
			self.data[value_index] = right_child_value
			return self.delete_max(value)
