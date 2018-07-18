import unittest
from Tree2.Node import Node
from Tree2.Tree import Tree

class NodeCase(unittest.TestCase):
	def test_failed_to_add_left_child(self):
		node1 = Node(None, 10)
		node2 = Node(None, None)
		node3 = Node(None, 2)

		with self.assertRaises(ValueError):
			node1.add_left(node2)

		node2.key = 20

		with self.assertRaises(ValueError):
			node1.add_left(node2)

		node2.key = 5
		node1.right_child = node3	

		with self.assertRaises(ValueError):
			node1.add_left(node2)

	def test_successfully_add_to_left_child(self):
		node1 = Node(None, 10)
		node2 = Node(None, 2)

		node1.add_left(node2)

		self.assertIs(node1.left_child, node2)
		self.assertIs(node2.parent, node1)

	def test_failed_to_add_right_child(self):
		node1 = Node(None, 10)
		node2 = Node(None, None)
		node3 = Node(None, 5)

		with self.assertRaises(ValueError):
			node1.add_right(node2)

		node2.key = 2

		with self.assertRaises(ValueError):
			node1.add_right(node2)

		node1.right_child = node3	

		with self.assertRaises(ValueError):
			node1.add_right(node2)	

	def test_successfully_add_to_right_child(self):
		node1 = Node(None, 10)
		node2 = Node(None, 20)

		node1.add_right(node2)

		self.assertIs(node1.right_child, node2)
		self.assertIs(node2.parent, node1)
			
class TreeCase(unittest.TestCase):
	def test_search_node_by_equal_key(self):
		node1 = Node(None, 10)
		node2 = Node(None, 7)
		node3 = Node(None, 12)
		node4 = Node(None, 4)

		tree = Tree()
		tree.root = node1

		node1.add_left(node2)
		node1.add_right(node3)

		node2.add_left(node4)

		self.assertEqual([node4, True], tree.search(4))
		self.assertEqual([node3, True], tree.search(12))

	def test_search_node_by_not_equal_key(self):
		node1 = Node(None, 10)
		node2 = Node(None, 7)
		node3 = Node(None, 12)
		node4 = Node(None, 4)

		tree = Tree()
		tree.root = node1

		node1.add_left(node2)
		node1.add_right(node3)

		node2.add_left(node4)

		self.assertEqual([node4, False, 'left'], tree.search(3))
		self.assertEqual([node3, False, 'right'], tree.search(15))

	def test_get_min_max_keys(self):
		node1 = Node(None, 10)
		node2 = Node(None, 7)
		node3 = Node(None, 12)
		node4 = Node(None, 4)

		tree = Tree()
		tree.root = node1

		node1.add_left(node2)
		node1.add_right(node3)
		node2.add_left(node4)
	
		self.assertEqual({'min': 4, 'max': 12}, tree.get_min_max())
		self.assertEqual({'min': 4, 'max': 7}, tree.get_min_max(node2))
				
	def test_delete_node_left_descendant(self):
		node1 = Node(None, 8)
		node2 = Node(None, 4)
		node3 = Node(None, 12)
		node4 = Node(None, 10)
		node5 = Node(None, 14)
		node6 = Node(None, 13)
		node7 = Node(None, 15)

		tree = Tree()
		tree.root = node1

		node1.add_left(node2)
		node1.add_right(node3)
		node3.add_left(node4)
		node3.add_right(node5)
		node5.add_left(node6)
		node5.add_right(node7)

		tree.delete(node3)

		self.assertIs(node6, node1.right_child)
		self.assertIs(node6.parent, node1)

		self.assertIs(node6.left_child, node4)
		self.assertIs(node6.right_child, node5)

		self.assertIs(node4.parent, node6)
		self.assertIs(node5.parent, node6)

		self.assertIsNone(node3.parent)
		self.assertIsNone(node3.left_child)
		self.assertIsNone(node3.right_child)

	def test_delete_node_right_descendant(self):	
		node1 = Node(None, 8)
		node2 = Node(None, 4)
		node3 = Node(None, 12)
		node4 = Node(None, 10)
		node5 = Node(None, 14)
		node6 = Node(None, 15)

		node1.add_left(node2)
		node1.add_right(node3)
		node3.add_left(node4)
		node3.add_right(node5)
		node5.add_right(node6)

		tree = Tree()
		tree.root = node1

		tree.delete(node3)

		self.assertIs(node5, node1.right_child)
		self.assertIs(node5.parent, node1)

		self.assertIs(node5.left_child, node4)
		self.assertIs(node4.parent, node5)

		self.assertIsNone(node3.parent)
		self.assertIsNone(node3.left_child)
		self.assertIsNone(node3.right_child)

if __name__ == '__main__':
	unittest.main(verbosity=2)		