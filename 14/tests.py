import unittest
from SimpleTree.Node import Node
from SimpleTree.Tree import Tree

class NodeCase(unittest.TestCase):
	def test_create_node_with_parent(self):
		node1 = Node(None)
		node2 = Node(node1)

		self.assertTrue(node2 in node1.child)
		self.assertEqual(node1, node2.parent)
		

class TreeCase(unittest.TestCase):
	def test_add_child_to_node(self):
		node1 = Node(None)
		node2 = Node(None)

		tree = Tree(node1)

		tree.add_node(current=node1, target=node2)

		self.assertTrue(node2 in node1.child)
		self.assertEqual(node1, node2.parent)

		with self.assertRaises(Exception):
			tree.add_node(current=node2, target=node1)

	def test_delete_node(self):
		node1 = Node(None)
		node2 = Node(node1)
		node3 = Node(node2)

		tree = Tree(node1)

		with self.assertRaises(Exception):
			tree.delete_node(node1)

		tree.delete_node(node2)	

		self.assertTrue(node2 not in node1.child)
		self.assertTrue(node3 in node1.child)
		self.assertEqual(node1, node3.parent)
		self.assertFalse(node2.child)

	def test_iterate_tree(self):
		node1 = Node(None)
		node2 = Node(node1)
		node3 = Node(node2)

		tree = Tree(node1)

		self.assertEqual([node1, node2, node3], tree.iterate())

	def test_find_nodes_by_value(self):
		node1 = Node(None)
		node1.value = 'Node 1'
		node2 = Node(node1)
		node2.value = 'Node 2'
		node3 = Node(node2)
		node3.value = 'Node'		
		node4 = Node(node3)
		node4.value = 'Node'		

		tree = Tree(node1)

		self.assertEqual([node3, node4], tree.find_by_value('Node'))
		self.assertFalse(tree.find_by_value('Unknown Node'))

	def test_tree_info(self):
		node1 = Node(None)
		node2 = Node(node1)
		node3 = Node(node2)

		tree = Tree(node1)

		tree_info = tree.info()
		self.assertEqual(2, tree_info['nodes'])
		self.assertEqual(1, tree_info['leaves'])

	def test_set_node_levels(self):
		node1 = Node(None)
		node2 = Node(node1)
		node3 = Node(node2)
		node4 = Node(node2)
		node5 = Node(node1)

		tree = Tree(node1)

		tree.set_levels()

		self.assertEqual(0, node1.level)
		self.assertEqual(1, node2.level)
		self.assertEqual(2, node3.level)
		self.assertEqual(2, node4.level)
		self.assertEqual(1, node5.level)
				
if __name__ == '__main__':
	unittest.main(verbosity=2)		