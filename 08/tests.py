import unittest
from OrderedList.Node import Node
from OrderedList.List import List
from OrderedList.ListStrings import ListStrings

class ListCase(unittest.TestCase):
	def test_add_integer_values_in_list_sorted_by_asc(self):
		n1 = Node(1)	
		n4 = Node(4)
		n3 = Node(3)
		n2 = Node(2)

		ordered_list = List();
		ordered_list.add(n1)	
		ordered_list.add(n4)	
		ordered_list.add(n3)	
		ordered_list.add(n2)

		self.assertIsNone(n1.prev)
		self.assertIs(n1.next.value, n2.value)
		self.assertIs(n2.prev.value, n1.value)
		self.assertIs(n2.next.value, n3.value)
		self.assertIs(n3.prev.value, n2.value)
		self.assertIs(n3.next.value, n4.value)
		self.assertIs(n3.prev.value, n2.value)
		self.assertIsNone(n4.next)

	def test_add_integer_values_in_list_sorted_by_desc(self):
		n1 = Node(1)	
		n4 = Node(4)
		n3 = Node(3)
		n2 = Node(2)

		ordered_list = List(List.SORT_DESC);
		ordered_list.add(n1)	
		ordered_list.add(n4)	
		ordered_list.add(n3)	
		ordered_list.add(n2)

		self.assertIsNone(n4.prev)
		self.assertIs(n4.next.value, n3.value)
		self.assertIs(n3.prev.value, n4.value)
		self.assertIs(n3.next.value, n2.value)
		self.assertIs(n2.prev.value, n3.value)
		self.assertIs(n2.next.value, n1.value)		
		self.assertIs(n1.prev.value, n2.value)
		self.assertIsNone(n1.next)

	def test_add_string_values_in_list_sorted_by_asc(self):
		n1 = Node('a')	
		n4 = Node('d')
		n3 = Node('c')
		n2 = Node('b')

		ordered_list = ListStrings();
		ordered_list.add(n1)	
		ordered_list.add(n4)	
		ordered_list.add(n3)	
		ordered_list.add(n2)

		self.assertIsNone(n1.prev)
		self.assertIs(n1.next.value, n2.value)
		self.assertIs(n2.prev.value, n1.value)
		self.assertIs(n2.next.value, n3.value)
		self.assertIs(n3.prev.value, n2.value)
		self.assertIs(n3.next.value, n4.value)
		self.assertIs(n3.prev.value, n2.value)
		self.assertIsNone(n4.next)	

	def test_add_string_values_in_list_sorted_by_desc(self):
		n1 = Node('a')	
		n4 = Node('d')
		n3 = Node('c')
		n2 = Node('b')

		ordered_list = ListStrings(List.SORT_DESC);
		ordered_list.add(n1)	
		ordered_list.add(n4)	
		ordered_list.add(n3)	
		ordered_list.add(n2)

		self.assertIsNone(n4.prev)
		self.assertIs(n4.next.value, n3.value)
		self.assertIs(n3.prev.value, n4.value)
		self.assertIs(n3.next.value, n2.value)
		self.assertIs(n2.prev.value, n3.value)
		self.assertIs(n2.next.value, n1.value)		
		self.assertIs(n1.prev.value, n2.value)
		self.assertIsNone(n1.next)		

	def test_find_value_in_list(self):
		n1 = Node(1)	
		n4 = Node(4)
		n3 = Node(3)
		n2 = Node(2)

		ordered_list = List();
		ordered_list.add(n1)	
		ordered_list.add(n4)	
		ordered_list.add(n3)	
		ordered_list.add(n2)

		self.assertIs(n2, ordered_list.find(n2.value))

	def test_return_none_when_find_in_list_sort_by_asc(self):
		n2 = Node(2)
		n3 = Node(3)
		n4 = Node(4)

		ordered_list = List();	
		ordered_list.add(n4)	
		ordered_list.add(n2)		
		ordered_list.add(n3)	

		self.assertIsNone(ordered_list.find(1))	
		self.assertIsNone(ordered_list.find(5))	

	def test_return_none_when_find_in_list_sort_by_desc(self):
		n2 = Node(2)
		n3 = Node(3)
		n4 = Node(4)

		ordered_list = List();	
		ordered_list.add(n2)
		ordered_list.add(n4)	
		ordered_list.add(n3)	

		self.assertIsNone(ordered_list.find(5))			
		self.assertIsNone(ordered_list.find(1))	

if __name__ == '__main__':
	unittest.main(verbosity=2)		