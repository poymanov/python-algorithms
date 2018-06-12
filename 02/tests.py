import unittest
from LinkedList import Node, List

class NodeCase(unittest.TestCase):
	def test_node_can_have_previous_element(self):
		n1 = Node(1)	
		n2 = Node(2)

		n2.prev = n1

		self.assertIs(n2.prev, n1)

	def test_node_can_have_next_element(self):
		n1 = Node(1)	
		n2 = Node(2)

		n1.next = n2

		self.assertIs(n1.next, n2)
		
class ListCase(unittest.TestCase):
	def test_list_can_delete_one_node_by_value(self):
		n1 = Node(1)	
		n2 = Node(2)
		n3 = Node(3)
		n4 = Node(4)

		linked_list = List();
		linked_list.add_in_tail(n1)	
		linked_list.add_in_tail(n2)	
		linked_list.add_in_tail(n3)	
		linked_list.add_in_tail(n4)	

		linked_list.delete_first_by_value(3)

		self.assertIsNone(n3.prev)
		self.assertIsNone(n3.next)

		self.assertIsNone(n1.prev)
		self.assertIs(n1.next, n2)
		self.assertIs(n2.prev, n1)
		self.assertIs(n2.next, n4)
		self.assertIs(n4.prev, n2)
		self.assertIsNone(n4.next)

	def test_list_can_append_node_after_item(self):
		n1 = Node(1)	
		n2 = Node(2)
		n3 = Node(3)
		n4 = Node(4)

		linked_list = List();
		linked_list.add_in_tail(n1)	
		linked_list.add_in_tail(n2)	
		linked_list.add_in_tail(n4)	

		linked_list.append_after(node=n3, after=n2)
	
		self.assertIsNone(n1.prev)
		self.assertIs(n1.next, n2)
		self.assertIs(n2.prev, n1)
		self.assertIs(n2.next, n3)
		self.assertIs(n3.prev, n2)
		self.assertIs(n3.next, n4)	
		self.assertIs(n4.prev, n3)
		self.assertIsNone(n4.next)

	def test_list_can_append_node_in_head(self):
		n1 = Node(1)		
		n2 = Node(2)
		n3 = Node(3)
		n4 = Node(4)

		linked_list = List();
		linked_list.add_in_tail(n2)	
		linked_list.add_in_tail(n3)	
		linked_list.add_in_tail(n4)	

		linked_list.append_in_head(n1)

		self.assertIs(linked_list.head, n1)
		self.assertIsNone(n1.prev)
		self.assertIs(n1.next, n2)
		self.assertIs(n2.prev, n1)

if __name__ == '__main__':
	unittest.main(verbosity=2)		