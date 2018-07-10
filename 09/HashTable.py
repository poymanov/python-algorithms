class HashTable:
	def __init__(self, sz, stp):
		self.size = sz
		self.step = stp
		self.slots = [None] * self.size

	def hash_fun(self, value):
		value = str(value)

		bytes_sum = 0

		for symbol in value:
			bytes_sum += ord(symbol)

		return bytes_sum % self.size

	def seek_slot(self, value):
		base_index = self.hash_fun(value)
		return self.iterate_slots(base_index, self.step, None)

	def put(self, value):
		index = self.seek_slot(value)

		if index is None:
			raise Exception('Slot finding is failed')

		self.slots[index] = value

	def find(self, value):
		base_index = self.hash_fun(value)
		return self.iterate_slots(base_index, 1, value)

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

