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

	def test_get_nearbies_for_unknown_vertex(self):
		simple_graph = Graph(3)		
		vertex1 = Vertex()
		
		with self.assertRaises(Exception):
			simple_graph.get_nearbies(vertex)

	def test_get_empty_nearbies_list(self):
		self.assertEqual([], self.simple_graph.get_nearbies(self.vertex1))
		self.assertEqual([], self.simple_graph.get_nearbies(self.vertex2))
		self.assertEqual([], self.simple_graph.get_nearbies(self.vertex3))

	def	test_get_nearbies_list(self):
		self.simple_graph.add_edge(self.vertex1, self.vertex2)
		self.simple_graph.add_edge(self.vertex1, self.vertex3)

		vertex1_nearbies = [self.vertex2, self.vertex3]
		vertex2_nearbies = [self.vertex1]
		vertex3_nearbies = [self.vertex1]

		self.assertEqual(vertex1_nearbies, self.simple_graph.get_nearbies(self.vertex1))
		self.assertEqual(vertex2_nearbies, self.simple_graph.get_nearbies(self.vertex2))
		self.assertEqual(vertex3_nearbies, self.simple_graph.get_nearbies(self.vertex3))

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
		self.assertEqual(result_way, self.simple_graph.find_way(self.vertex1, self.vertex2).stack)

	def test_find_way_case_02(self):
		result_way = [self.vertex1, self.vertex2, self.vertex3]

		self.simple_graph.add_edge(self.vertex1, self.vertex2)
		self.simple_graph.add_edge(self.vertex2, self.vertex3)
			
		self.assertEqual(result_way, self.simple_graph.find_way(self.vertex1, self.vertex3).stack)	

	def test_find_way_case_03(self):
		self.simple_graph.add_edge(self.vertex1, self.vertex2)

		self.assertFalse(self.simple_graph.find_way(self.vertex1, self.vertex3).size())	


if __name__ == '__main__':
	unittest.main(verbosity=2)
