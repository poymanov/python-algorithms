import unittest
from SimpleGraph.Graph import Graph
from SimpleGraph.Vertex import Vertex

class SimpleGraphCase(unittest.TestCase):
	def setUp(self):
		vertex1 = Vertex(1)
		vertex2 = Vertex(2)
		vertex3 = Vertex(3)	

		simple_graph = Graph(3)		
		simple_graph.add_vertex(vertex1)	
		simple_graph.add_vertex(vertex2)
		simple_graph.add_vertex(vertex3)

		self.vertex1, self.vertex2, self.vertex3 = vertex1,	vertex2, vertex3
		self.simple_graph = simple_graph

	def test_find_way_unknown_vertex(self):
		vertex4 = Vertex()	
		vertex5 = Vertex()	

		with self.assertRaises(Exception):
			self.simple_graph.find_way(self.vertex1, vertex4)

		with self.assertRaises(Exception):
			self.simple_graph.find_way(vertex4, vertex5)			

	def test_clear_hits_data_after_find_way(self):
		self.simple_graph.add_edge(self.vertex1, self.vertex2)		
		self.simple_graph.find_way(self.vertex1, self.vertex2)

		self.assertFalse(self.vertex1.hit)
		self.assertFalse(self.vertex2.hit)

	def test_find_way_case_01(self):
		result_way = [self.vertex1, self.vertex2]

		self.simple_graph.add_edge(self.vertex1, self.vertex2)
		self.assertEqual(result_way, self.simple_graph.find_way(self.vertex1, self.vertex2))

	def test_find_way_case_02(self):
		vertex1 = Vertex(1)
		vertex2 = Vertex(2)
		vertex3 = Vertex(3)	
		vertex4 = Vertex(4)
		vertex5 = Vertex(5)
		vertex6 = Vertex(6)

		simple_graph = Graph(6)		
		simple_graph.add_vertex(vertex1)	
		simple_graph.add_vertex(vertex2)
		simple_graph.add_vertex(vertex3)
		simple_graph.add_vertex(vertex4)	
		simple_graph.add_vertex(vertex5)	
		simple_graph.add_vertex(vertex6)	

		result_way = [vertex1, vertex3, vertex4, vertex6]

		simple_graph.add_edge(vertex1, vertex2)
		simple_graph.add_edge(vertex1, vertex3)
		simple_graph.add_edge(vertex3, vertex4)
		simple_graph.add_edge(vertex3, vertex5)
		simple_graph.add_edge(vertex4, vertex6)
			
		self.assertEqual(result_way, simple_graph.find_way(vertex1, vertex6))	

	def test_find_way_case_03(self):
		self.simple_graph.add_edge(self.vertex1, self.vertex2)
		self.assertIsNone(self.simple_graph.find_way(self.vertex1, self.vertex3))	

if __name__ == '__main__':
	unittest.main(verbosity=2)
