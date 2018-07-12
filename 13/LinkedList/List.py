class List():
	def __init__(self):
		self.head = None
		self.tail = None
		self.current = None

	def __next__(self):
		current = self.current

		if current is None:
			self.first()
			raise StopIteration

		self.current = current.next		
		return current

	def first(self):
		self.current = self.head

	def add_in_tail(self, item):
		if self.head is None:
			self.head = item
			item.prev = None
			item.next = None
			self.current = item
		else:
			self.tail.next = item
			item.prev = self.tail
		self.tail = item