class Cache:
	def __init__(self, sz, stp):
		self.size = sz
		self.step = stp
		self.slots = [None] * self.size
		self.values = [None] * self.size
		self.hits = [0] * self.size

	def hash_fun(self, value):
		value = str(value)

		bytes_sum = 0

		for symbol in value:
			bytes_sum += ord(symbol)

		return bytes_sum % self.size

	def seek_slot(self, value):
		base_index = self.hash_fun(value)

		index = self.iterate_slots(base_index, self.step, None)

		if index is None:
			self.remove_least_popular_slot()
			return self.seek_slot(value)
		else:
			return index
		
	def put(self, key, value):
		index = self.seek_slot(key)
		self.slots[index] = key
		self.values[index] = value

	def is_key(self, key):
		index = self.hash_fun(key)
		return self.slots[index] is not None and self.slots[index] == key

	def get(self, key):
		base_index = self.hash_fun(key)
		index = self.iterate_slots(base_index, 1, key)

		if index is not None:			
			self.put_hits(index)				
			return self.values[index]
		else:
			return None

	def iterate_slots(self, base_index, step, value):
		index = base_index
		first_round = True

		while self.slots[index] != value:
			index += step

			if first_round:
				if index >= self.size:
					first_round = False
					index = 0
			else:
				if index >= base_index:
					return None

		return index	

	def put_hits(self, index):
		self.hits[index] += 1

	def remove_least_popular_slot(self):
		min_value = min(self.hits)
		min_index = self.hits.index(min_value)

		self.slots[min_index] = None
		self.values[min_index] = None
		self.hits[min_index] = 0