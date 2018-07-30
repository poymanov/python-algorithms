import unittest
from SimpleGraph.Graph import Graph
from SimpleGraph.Vertex import Vertex

class SimpleGraphCase(unittest.TestCase):
	def setUp(self):
		vertex1 = Vertex()
		vertex2 = Vertex()
		vertex3 = Vertex()	

		simple_graph = Graph(3)		
		simple_graph.add_vertex(vertex1)	
		simple_graph.add_vertex(vertex2)
		simple_graph.add_vertex(vertex3)

		edge_1_3_vertex = [
			[0, 0, 1],
			[0, 0, 0],
			[1, 0, 0]
		]

		empty_m_adjacency = []

		for __ in range(3):
			empty_m_adjacency.append([0, 0, 0])

		self.vertex1, self.vertex2, self.vertex3 = vertex1,	vertex2, vertex3
		self.simple_graph, self.edge_1_3_vertex = simple_graph, edge_1_3_vertex
		self.empty_m_adjacency = empty_m_adjacency	

	def	test_init_simple_graph(self):
		simple_graph = Graph(3)

		self.assertEqual(self.empty_m_adjacency, simple_graph.m_adjacency)	

	def test_get_vertex_index(self):
		vertex4 = Vertex()

		self.assertEqual(0, self.simple_graph.get_vertex_index(self.vertex1))
		self.assertEqual(1, self.simple_graph.get_vertex_index(self.vertex2))
		self.assertEqual(2, self.simple_graph.get_vertex_index(self.vertex3))

		with self.assertRaises(Exception):
			self.simple_graph.add_vertex(vertex4)
		
	def test_add_excess_vertex(self):	
		vertex4 = Vertex()		

		with self.assertRaises(Exception):
			self.simple_graph.add_vertex(vertex4)

		self.assertNotIn(vertex4, self.simple_graph.vertex)

	def test_add_exists_vertex(self):
		vertex_list = [self.vertex1, self.vertex2, self.vertex3]	

		with self.assertRaises(Exception):
			self.simple_graph.add_vertex(self.vertex2)

		self.assertEqual(3, len(self.simple_graph.vertex))
		self.assertEqual(vertex_list, self.simple_graph.vertex)

	def test_add_vertex(self):
		vertex_list = [self.vertex1, self.vertex2, self.vertex3]		
		self.assertEqual(vertex_list, self.simple_graph.vertex)

	def test_add_edge_unknown_vertexes(self):
		vertex4 = Vertex()
		vertex5 = Vertex()

		with self.assertRaises(Exception):
			self.simple_graph.add_edge(self.vertex1, vertex4)

		with self.assertRaises(Exception):
			self.simple_graph.add_edge(vertex4, vertex5)			

	def test_add_exists_edge(self):
		self.simple_graph.m_adjacency[0][2] = 1
		self.simple_graph.m_adjacency[2][0] = 1

		with self.assertRaises(Exception):
			self.simple_graph.add_edge(self.vertex1, self.vertex3)		
			
	def test_add_edge_beetween_vertex(self):
		result_m_adjacency = self.edge_1_3_vertex

		self.simple_graph.add_edge(self.vertex1, self.vertex3)

		self.assertEqual(result_m_adjacency, self.simple_graph.m_adjacency)

	def test_remove_edge_unknown_vertexes(self):
		vertex4 = Vertex()
		vertex5 = Vertex()

		with self.assertRaises(Exception):
			self.simple_graph.remove_edge(self.vertex1, vertex4)

		with self.assertRaises(Exception):
			self.simple_graph.remove_edge(vertex4, vertex5)	

	def test_remove_not_existed_edge(self):
		with self.assertRaises(Exception):
			self.simple_graph.remove_edge(self.vertex1, self.vertex3)

	def test_remove_edge(self):
		self.simple_graph.m_adjacency = self.edge_1_3_vertex

		self.simple_graph.remove_edge(self.vertex1, self.vertex3)
		self.assertEqual(self.empty_m_adjacency, self.simple_graph.m_adjacency)

	def test_delete_unknown_vertex(self):
		vertex4 = Vertex()

		with self.assertRaises(Exception):
			self.simple_graph.delete_vertex(vertex4)

	def test_delete_vertex(self):
		self.simple_graph.m_adjacency = self.edge_1_3_vertex

		result_vertex = [self.vertex2, self.vertex3]

		self.simple_graph.delete_vertex(self.vertex1)	

		self.assertEqual(self.empty_m_adjacency, self.simple_graph.m_adjacency)		
		self.assertEqual(result_vertex, self.simple_graph.vertex)

if __name__ == '__main__':
	unittest.main(verbosity=2)
