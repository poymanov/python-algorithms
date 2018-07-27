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

		prev_index = index - 1
		prev_value = self.data[prev_index]

		if value > self.data[prev_index]:
			self.data[index] = prev_value
			self.data[prev_index] = value
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

		if self.data[-1] == value: return None

		next_index = value_index + 1
		next_value = self.data[next_index]

		if next_value is None: return None

		if value < self.data[next_index]:
			self.data[value_index] = next_value
			self.data[next_index] = value
			return self.delete_max(value)
