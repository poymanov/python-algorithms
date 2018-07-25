import unittest
from Tree import Tree

class TreeToArrayCase(unittest.TestCase):
	def setUp(self):
		tree = Tree(4, 50)
		tree.add_left(50, 25)
		tree.add_right(50, 75)

		tree.add_right(25, 37)
		tree.add_left(37, 31)
		tree.add_right(37, 43)

		tree.add_left(75, 62)
		tree.add_left(62, 55)

		tree.add_right(75, 84)
		tree.add_right(84, 92)

		self.tree = tree

		self.result_data = [50, 25, 75, None, 37, 62, 84, None, None, 31, 43, 55, None, None, 92]

	def test_init_tree(self):
		tree = Tree(4, 50)

		result_data = [None] * 15
		result_data[0] = 50

		self.assertEqual(result_data, tree.data)

	def test_get_left_index(self):
		tree = Tree(4, 50)
		self.assertEqual(1, tree.get_left_index(0))

	def test_get_right_index(self):
		tree = Tree(4, 50)
		self.assertEqual(2, tree.get_right_index(0))		

	def test_add_left_child_failed(self):	
		tree = Tree(4, 50)

		with self.assertRaises(Exception):
			tree.add_left(99, 10)

		tree = Tree(1, 50)			

		with self.assertRaises(Exception):
			tree.add_left(50, 10)

		tree = Tree(4, 50)

		with self.assertRaises(Exception):
			tree.add_left(50, 100)	

		tree = Tree(4, 50)
		tree.data[2] = 5

		with self.assertRaises(Exception):
			tree.add_left(50, 10)		

	def test_add_left_child_success(self):
		tree = Tree(4, 50)
		tree.add_left(50, 25)

		result_data = [None] * 15
		result_data[0] = 50
		result_data[1] = 25

		self.assertEqual(result_data, tree.data)

	def test_add_right_child_failed(self):
		tree = Tree(4, 50)

		with self.assertRaises(Exception):
			tree.add_right(99, 10)

		tree = Tree(1, 50)			

		with self.assertRaises(Exception):
			tree.add_right(50, 10)			

		tree = Tree(4, 50)

		with self.assertRaises(Exception):
			tree.add_right(50, 2)	

	def test_add_right_child_success(self):
		tree = Tree(4, 50)
		tree.add_left(50, 25)
		tree.add_right(50, 75)

		result_data = [None] * 15
		result_data[0] = 50
		result_data[1] = 25
		result_data[2] = 75

		self.assertEqual(result_data, tree.data)

	def test_create_tree(self):
		self.assertEqual(self.result_data, self.tree.data)

	def test_search_missing_key(self):
		self.assertIsNone(self.tree.search(100))

	def test_search_exists_key(self):
		self.assertEqual(6, self.tree.search(84))

	def test_search_missing_acceptable_key(self):
		self.assertEqual(3, self.tree.search(21))

	def test_add_child_failed(self):
		with self.assertRaises(Exception):
			self.tree.add(100)	

		with self.assertRaises(Exception):
			self.tree.add(84)				

	def test_add_child_success(self):
		self.assertTrue(self.tree.add(21))
		self.assertEqual(3, self.tree.data.index(21))		

	def test_create_tree_with_add(self):
		tree = Tree(4, 50)
		tree.add(25)
		tree.add(75)

		tree.add(37)
		tree.add(31)
		tree.add(43)

		tree.add(62)
		tree.add(55)

		tree.add(84)
		tree.add(92)

		self.assertEqual(self.result_data, tree.data)

if __name__ == '__main__':
	unittest.main(verbosity=2)		
