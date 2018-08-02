from .Queue import Queue

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
			raise Exception('Trying to find nearbies for unknown vertex')

		nearbies = []	
		vertex_index = self.vertex.index(vertex)
		m_adjacency_line = self.m_adjacency[vertex_index]

		for key, value in enumerate(m_adjacency_line):
			if value == 1:
				nearbies.append(self.vertex[key])

		return nearbies

	def unmark_vertexes(self):
		for vertex in self.vertex:
			vertex.hit = False

	def find_way(self, vertex1, vertex2):
		if vertex1 not in self.vertex or vertex2 not in self.vertex:
			raise Exception('Trying to find way with unknown vertexes')		

		predecessors = []
		queue = Queue()
		queue.enqueue(vertex1)

		while queue.size() > 0:
			current = queue.dequeue()
			current.hit = True

			if current == vertex2:
				break;

			nearbies = self.get_nearbies(current)

			for nearby_vertex in nearbies:
				if nearby_vertex.hit == True: continue
				predecessors.append(current)
				predecessors.append(nearby_vertex)

				queue.enqueue(nearby_vertex)

		self.unmark_vertexes()			

		if vertex2 not in predecessors:
			return None

		path = []
		current_element = vertex2	
			
		while True:
			path.insert(0, current_element)
			current_element_index = predecessors.index(current_element)

			if current_element_index == 0: break
			current_element = predecessors[current_element_index - 1]

		return path		