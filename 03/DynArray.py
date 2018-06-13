import ctypes

class DynArray():
	BASE_CAPACITY = 16

	def __init__(self):
		self.count = 0
		self.capacity = self.BASE_CAPACITY
		self.array = self.make_array(self.capacity)

	def __len__(self):
		return self.count;	

	def make_array(self, new_capacity):
		return (new_capacity * ctypes.py_object)()

	def __getitem__(self, i):
		if i < 0 or i >= self.count:
			raise IndexError('Index is out of bounds')
		return self.array[i]	

	def resize(self, new_capacity):
		new_array = self.make_array(new_capacity)
		for i in range(self.count):
			new_array[i] = self.array[i]
		self.array = new_array
		self.capacity = new_capacity

	def append(self, itm):
		if self.count == self.capacity:
			self.resize(2 * self.capacity)		
		self.array[self.count] = itm
		self.count += 1

	def insert(self, i, itm):
		values = []

		for k in range(self.count):			
			if k == i: values.append(itm)				
			values.append(self.array[k])

		self.count = 0	
		self.array = self.make_array(self.capacity)
	
		for value in values:
			self.append(value)

	def delete(self, i):
		values = []

		for k in range(self.count):			
			if k == i: continue				
			values.append(self.array[k])

		self.count = 0	
		self.array = self.make_array(self.capacity)
	
		for value in values:
			self.append(value)






