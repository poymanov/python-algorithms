class Node():
	def __init__(self, v):
		self.value = v
		self.prev = None
		self.next = None

	def __repr__(self):
		return 'Node ({})'.format(self.value)