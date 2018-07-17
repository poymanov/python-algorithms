class Node():
	def __init__(self, parent):
		self.parent = parent
		self.child = []
		self.value = None
		self.level = -1

		if not parent is None:
			parent.child.append(self)

	def __repr__(self):
		return 'Node {}'.format(self.value)			

