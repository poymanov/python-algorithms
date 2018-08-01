class Vertex:
	hit = False

	def __init__(self, key = None):
		self.key = key

	def __repr__(self):
		return 'Vertex {}'.format(self.key)