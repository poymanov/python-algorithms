class PowerSet:
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
		if self.find(value) is not None:
			raise Exception('Value already exists')

		index = self.seek_slot(value)
		self.slots[index] = value

	def find(self, value):
		base_index = self.hash_fun(value)
		return self.iterate_slots(base_index, 1, value)

	def remove(self, value):
		index = self.find(value)
		self.slots[index] = None

	def intersection(self, power_set):
		values = []

		for slot in self.slots:
			if slot is None: continue
			
			if power_set.find(slot) is not None:
				values.append(slot)

		return self.create_power_set_from_values(values)

	def difference(self, power_set):
		values = []

		for slot in self.slots:
			if slot is None: continue

			if power_set.find(slot) is None:
				values.append(slot)

		return self.create_power_set_from_values(values)		

	def issubset(self, power_set):
		for slot in power_set.slots:
			if slot is None: continue

			if self.find(slot) is None:
				return False

		return True

	def union(self, power_set):
		values = []

		for slot in self.slots:
			if slot is None or slot in values: continue

			values.append(slot)

		for slot in power_set.slots:
			if slot is None or slot in values: continue

			values.append(slot)			

		return self.create_power_set_from_values(values)
			
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

	def create_power_set_from_values(self, values):
		values_length = len(values)
				
		if values_length < 19:
			size = 19
		else:
			size = values_length * 2

		new_power_set = PowerSet(size, 3)	
				
		for value in values:			
			new_power_set.put(value)

		return new_power_set	
