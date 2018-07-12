import unittest
from LinkedList.Node import Node
from LinkedList.List import List

class ListCase(unittest.TestCase):
	def setUp(self):
		n1, n2, n3 = Node(1), Node(2), Node(3)	

		linked_list = List();
		linked_list.add_in_tail(n1)	
		linked_list.add_in_tail(n2)	
		linked_list.add_in_tail(n3)

		self.n1, self.n2, self.n3, self.linked_list = n1, n2, n3, linked_list

	def test_list_iterable(self):		
		self.assertIs(self.n1, self.linked_list.current)

		current = next(self.linked_list)
		self.assertIs(self.n1, current)

		current = next(self.linked_list)
		self.assertIs(self.n2, current)

		current = next(self.linked_list)
		self.assertIs(self.n3, current)

	def test_list_reset_current_position(self):
		next(self.linked_list)
		next(self.linked_list)
		next(self.linked_list)

		self.linked_list.first()
		
		self.assertIs(self.n1, next(self.linked_list))

	def test_list_throw_iterable_exception(self):
		next(self.linked_list)
		next(self.linked_list)
		next(self.linked_list)

		with self.assertRaises(StopIteration):
			next(self.linked_list)
		
if __name__ == '__main__':
	unittest.main(verbosity=2)		