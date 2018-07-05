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
		index = self.hash_fun(value)

		while self.slots[index] is not None:
			index += self.step
			if index > self.size: return None

		return index

	def put(self, value):
		index = self.seek_slot(value)

		if index is None:
			raise Exception('Slot finding is failed')

		self.slots[index] = value

	def find(self, value):
		index = self.hash_fun(value)

		if self.slots[index] == value:
			return index
		else:
			return None

