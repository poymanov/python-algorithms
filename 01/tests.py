import unittest
from LinkedList.Node import Node
from LinkedList.List import List

class NodeCase(unittest.TestCase):
	def test_new_node_have_not_next_element(self):
		n1 = Node(12)
		self.assertIsNone(n1.next)	

	def test_node_have_value(self):
		n1 = Node(12)
		self.assertEqual(n1.value, 12)

	def test_node_have_next_element(self):
		n1 = Node(12)
		n2 = Node(55)
		n1.next = n2
		self.assertTrue(n1.next)
		
class ListCase(unittest.TestCase):
	def test_new_list_have_not_head_and_tail_nodes(self):
		linked_list = List()
		self.assertIsNone(linked_list.head)
		self.assertIsNone(linked_list.tail)

	def test_list_have_head_node(self):
		n1 = Node(12)
		linked_list = List()
		linked_list.add_in_tail(n1)		
		self.assertIs(linked_list.head, n1)

	def test_list_have_tail_node(self):
		n1 = Node(12)
		n2 = Node(55)
		linked_list = List()
		linked_list.add_in_tail(n1)
		linked_list.add_in_tail(n2)
		self.assertIs(linked_list.tail, n2)
		self.assertIsNone(n2.next)

	def test_list_can_find_node_by_value(self):
		n1 = Node(12)
		n2 = Node(55)
		n3 = Node(128)

		linked_list = List()
		linked_list.add_in_tail(n1)
		linked_list.add_in_tail(n2)
		linked_list.add_in_tail(n3)

		result = linked_list.find(55)
		self.assertIs(result, n2)	

	def test_list_can_delete_one_node_by_value(self): # 1.1
		n1 = Node(12)
		n2 = Node(55)
		n3 = Node(128)

		linked_list = List()
		linked_list.add_in_tail(n1)
		linked_list.add_in_tail(n2)
		linked_list.add_in_tail(n3)

		linked_list.delete_first_by_value(55)

		self.assertIsNone(linked_list.find(55))
		self.assertTrue(linked_list.find(12))
		self.assertTrue(linked_list.find(128))

		self.assertIs(linked_list.head, n1)
		self.assertIs(linked_list.tail, n3)

		self.assertIsNone(n2.next) 
		self.assertIs(n1.next, n3)
		self.assertIsNone(n3.next)

	def test_list_can_delete_all_nodes_by_value(self): # 1.2
		n1 = Node(55)
		n2 = Node(12)
		n3 = Node(55)
		n4 = Node(128)
		n5 = Node(55)

		linked_list = List()
		linked_list.add_in_tail(n1)
		linked_list.add_in_tail(n2)
		linked_list.add_in_tail(n3)
		linked_list.add_in_tail(n4)
		linked_list.add_in_tail(n5)

		linked_list.delete_by_value(55)
		self.assertIsNone(linked_list.find(55))

	def test_list_can_delete_all_nodes(self): # 1.3
		n1 = Node(12)
		n2 = Node(55)
		n3 = Node(128)

		linked_list = List()
		linked_list.add_in_tail(n1)
		linked_list.add_in_tail(n2)
		linked_list.add_in_tail(n3)

		linked_list.flush_all()

		self.assertIsNone(linked_list.head)
		self.assertIsNone(linked_list.tail)

		self.assertIsNone(linked_list.find(12))
		self.assertIsNone(linked_list.find(55))
		self.assertIsNone(linked_list.find(128))

	def test_list_can_find_all_nodes_by_value(self): # 1.4
		n1 = Node(55)
		n2 = Node(12)
		n3 = Node(55)
		n4 = Node(128)	
		n5 = Node(55)

		linked_list = List()
		linked_list.add_in_tail(n1)
		linked_list.add_in_tail(n2)
		linked_list.add_in_tail(n3)
		linked_list.add_in_tail(n4)
		linked_list.add_in_tail(n5)

		result = linked_list.find_all(55)		

		self.assertEqual(len(result), 3)

		self.assertIn(n1, result)
		self.assertIn(n3, result)
		self.assertIn(n5, result)

		self.assertNotIn(n2, result)
		self.assertNotIn(n4, result)

	def test_list_can_count_itself_length(self): # 1.5
		n1 = Node(55)
		n2 = Node(12)
		n3 = Node(55)
		n4 = Node(128)	
		n5 = Node(55)

		linked_list = List()
		linked_list.add_in_tail(n1)
		linked_list.add_in_tail(n2)
		linked_list.add_in_tail(n3)
		linked_list.add_in_tail(n4)
		linked_list.add_in_tail(n5)

		list_length = linked_list.length()

		self.assertEqual(list_length, 5)

	def test_list_can_append_node_after_specified_node(self): # 1.6
		n1 = Node(55)
		n2 = Node(12)
		n3 = Node(55)
		n4 = Node(128)	
		n5 = Node(55)

		new = Node(99)	

		linked_list = List()
		linked_list.add_in_tail(n1)
		linked_list.add_in_tail(n2)
		linked_list.add_in_tail(n3)
		linked_list.add_in_tail(n4)
		linked_list.add_in_tail(n5)

		linked_list.append_after(newNode=new, afterNode=n2)

		self.assertTrue(linked_list.find(99))
		self.assertEqual(linked_list.length(), 6)
		self.assertIs(n2.next, new)
		self.assertIs(new.next, n3)

class AnotherCase(unittest.TestCase):
	def test_sum_equal_lists(self):
		n1 = Node(12)
		n2 = Node(55)
		n3 = Node(128)

		linked_list1 = List()
		linked_list1.add_in_tail(n1)
		linked_list1.add_in_tail(n2)
		linked_list1.add_in_tail(n3)

		n4 = Node(12)
		n5 = Node(55)
		n6 = Node(128)

		linked_list2 = List()
		linked_list2.add_in_tail(n4)
		linked_list2.add_in_tail(n5)
		linked_list2.add_in_tail(n6)

		result = List.sum_lists(linked_list1, linked_list2)

		self.assertEqual(result, [24, 110, 256])

	def test_sum_not_equal_lists(self):
		n1 = Node(12)
		n2 = Node(55)
		n3 = Node(128)

		linked_list1 = List()
		linked_list1.add_in_tail(n1)
		linked_list1.add_in_tail(n2)
		linked_list1.add_in_tail(n3)

		n4 = Node(12)
		n5 = Node(55)
		n6 = Node(128)
		n7 = Node(200)

		linked_list2 = List()
		linked_list2.add_in_tail(n4)
		linked_list2.add_in_tail(n5)
		linked_list2.add_in_tail(n6)
		linked_list2.add_in_tail(n7)

		result = List.sum_lists(linked_list1, linked_list2)

		self.assertIsNone(result)

if __name__ == '__main__':
	unittest.main(verbosity=2)		