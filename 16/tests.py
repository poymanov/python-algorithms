import unittest
from Tree2.Node import Node
from Tree2.Tree import Tree
from functions import *

class TreeToArrayCase(unittest.TestCase):
	def setUp(self):
		node1 = Node(None, 50)
		node2 = Node(None, 25)
		node3 = Node(None, 75)
		node4 = Node(None, 37)
		node5 = Node(None, 62)
		node6 = Node(None, 84)
		node7 = Node(None, 31)
		node8 = Node(None, 43)
		node9 = Node(None, 55)
		node10 = Node(None, 92)

		tree = Tree(4)
		tree.root = node1

		node1.add_left(node2)
		node1.add_right(node3)
	
		node2.add_right(node4)
		node4.add_left(node7)
		node4.add_right(node8)

		node3.add_left(node5)
		node5.add_left(node9)

		node3.add_right(node6)
		node6.add_right(node10)

		self.tree = tree
		self.array = create_array_from_tree(self.tree)

	def test_get_array_size(self):
		tree = Tree(2)		
		self.assertEqual(3, tree.get_array_size())

		tree = Tree(3)		
		self.assertEqual(7, tree.get_array_size())

		tree = Tree(4)		
		self.assertEqual(15, tree.get_array_size())

	def test_create_array_from_tree(self):		
		result_array = [50, 25, 75, None, 37, 62, 84, None, None, 31, 43, 55, None, None, 92]	
		self.assertEqual(result_array, self.array)

	def test_search_missing_key(self):
		self.assertIsNone(search(self.tree, self.array, 100))

	def test_search_exists_key(self):
		self.assertEqual(6, search(self.tree, self.array, 84))

	def test_search_missing_acceptable_key(self):
		self.assertEqual(-12, search(self.tree, self.array, 21))

if __name__ == '__main__':
	unittest.main(verbosity=2)		
