class AssocArray:
	def __init__(self, sz, stp):
		self.size = sz
		self.step = stp
		self.slots = [None] * self.size
		self.values = [None] * self.size

	def hash_fun(self, value):
		value = str(value)

		bytes_sum = 0

		for symbol in value:
			bytes_sum += ord(symbol)

		return bytes_sum % self.size

	def seek_slot(self, value):
		base_index = self.hash_fun(value)
		index = base_index
		first_round = True

		while self.slots[index] is not None:
			index += self.step

			if first_round:
				if index >= self.size:
					first_round = False
					index = 0
			else:
				if index >= base_index:
					return None

		return index
		
	def put(self, key, value):
		index = self.seek_slot(key)
		self.slots[index] = key
		self.values[index] = value

	def is_key(self, key):
		index = self.hash_fun(key)
		return self.slots[index] is not None

	def get(self, key):
		index = self.hash_fun(key)

		if self.slots[index] is not None:		
			return self.values[index]
		else:
			return None
