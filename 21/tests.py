import unittest
from functions import *

class InsertionSortCase(unittest.TestCase):
	def setUp(self):
		self.data = [2, 4, 5, 6, 3, 7, 8]

	def test_insertion_sort_step_1(self):
		data = [2, 4, 5, 6, 3, 7, 8]
		except_data = [2, 3, 4, 5, 6, 7, 8]
		self.assertEqual(except_data, insertion_sort(self.data))

	def test_insertion_sort_step_2(self):
		except_data = [2, 4, 3, 5, 6, 7, 8]
		step = 2
		self.assertEqual(except_data, insertion_sort(self.data, step))		

	def test_insertion_sort_step_3(self):
		except_data = [2, 4, 5, 3, 6, 7, 8]	
		step = 3
		self.assertEqual(except_data, insertion_sort(self.data, step))				

	def test_insertion_sort_incorrect_step(self):
		step = 8

		with self.assertRaises(ValueError):
			result = insertion_sort(self.data, step)

if __name__ == '__main__':
	unittest.main(verbosity=2)