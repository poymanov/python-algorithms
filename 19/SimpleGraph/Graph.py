from .Stack import Stack

class Graph:
	def __init__(self, max_vertex):
		self.max_vertex = max_vertex
		self.m_adjacency = []
		self.vertex = []

		self.init_m_adjacency()

	def init_m_adjacency(self):
		for __ in range(self.max_vertex):
			self.m_adjacency.append([0] * self.max_vertex)

	def add_vertex(self, vertex):
		if len(self.vertex) == self.max_vertex:
			raise Exception('Trying to add excess_vertex')

		if vertex in self.vertex:
			raise Exception('Trying to add exists vertex')

		self.vertex.append(vertex)

	def get_vertex_index(self, vertex):
		if vertex not in self.vertex:
			raise Exception('Vertex is not in graph')

		return self.vertex.index(vertex)

	def add_edge(self, vertex1, vertex2):
		try:
			vertex1_index = self.get_vertex_index(vertex1)
			vertex2_index = self.get_vertex_index(vertex2)
		except:
			raise Exception('Trying to create edge between unknown vertexes')

		if self.m_adjacency[vertex1_index][vertex2_index] == 1 and \
			self.m_adjacency[vertex2_index][vertex1_index] == 1:
				raise Exception('Trying to create already exists edge')

		self.m_adjacency[vertex1_index][vertex2_index] = 1
		self.m_adjacency[vertex2_index][vertex1_index] = 1

	def remove_edge(self, vertex1, vertex2):
		try:
			vertex1_index = self.get_vertex_index(vertex1)
			vertex2_index = self.get_vertex_index(vertex2)
		except:
			raise Exception('Trying to remove edge between unknown vertexes')

		vertex1_index = self.get_vertex_index(vertex1)
		vertex2_index = self.get_vertex_index(vertex2)

		if self.m_adjacency[vertex1_index][vertex2_index] == 0 and \
			self.m_adjacency[vertex2_index][vertex1_index] == 0:
			raise Exception('Trying to remove not existed edge')

		self.m_adjacency[vertex1_index][vertex2_index] = 0
		self.m_adjacency[vertex2_index][vertex1_index] = 0

	def delete_vertex(self, vertex):
		if vertex not in self.vertex:
			raise Exception('Trying to delete unknown vertex')

		vertex_index = self.get_vertex_index(vertex)

		edges = []

		for key, value in enumerate(self.m_adjacency[vertex_index]):
			if value == 1:
				edges.append(key)
				self.m_adjacency[vertex_index][key] = 0

		for key, data in enumerate(self.m_adjacency):
			if key in edges:
				self.m_adjacency[key][vertex_index] = 0

		self.vertex.remove(vertex)

	def get_nearbies(self, vertex):
		if vertex not in self.vertex:
			raise Exception('Trying to find nerbies for unknown vertex')

		nearbies = []	
		vertex_index = self.vertex.index(vertex)
		m_adjacency_line = self.m_adjacency[vertex_index]

		for key, value in enumerate(m_adjacency_line):
			if value == 1:
				nearbies.append(self.vertex[key])

		return nearbies

	def find_way(self, vertex1, vertex2):
		if vertex1 not in self.vertex or vertex2 not in self.vertex:
			raise Exception('Trying to find way with unknown vertexes')

		stack = Stack()	

		vertex1.hit = True

		stack.push(vertex1)

		nearbies = self.get_nearbies(vertex1)

		for item in nearbies:
			if item == vertex1 or item.hit == True: continue
			if item == vertex2:
				item.hit = True
				stack.push(item)
								
		if vertex2 in stack.stack:
			for item in stack.stack:
				item.hit = False		
		else:
			for item in nearbies:
				if item == vertex1 or item.hit == True: continue
				stack2 = self.find_way(item, vertex2)	
				stack.stack += stack2.stack

			if vertex2 in stack.stack:
				for item in stack.stack:
					item.hit = False	
				return stack	
			else:
				stack.pop()

				if stack.size() == 0:
					return stack

				vertex1 = stack.peak()

				stack3 = self.find_way(vertex1, vertex2)	

				if vertex2 in stack.stack:
					for item in stack.stack:
						item.hit = False	

		return stack
