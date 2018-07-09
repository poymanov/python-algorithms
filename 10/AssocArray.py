class AssocArray:
	def __init__(self):		
		self.slots = []
		self.values = []

	def put(self, key, value):
		self.slots.append(key)
		self.values.append(value)

	def is_key(self, key):
		return key in self.slots

	def get(self, key):
		result = None

		if self.is_key(key): result = self.values[self.slots.index(key)]

		return result
