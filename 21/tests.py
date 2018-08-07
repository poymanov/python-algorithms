import unittest
from functions import *

class InsertionSortCase(unittest.TestCase):
	def setUp(self):
		self.data = [4, 1, 2, 3]

	def test_insertion_sort_step_1(self):
		except_data = [1, 2, 3, 4]

		self.assertEqual(except_data, insertion_sort(self.data))

	def test_insertion_sort_step_2(self):
		except_data = [2, 1, 4, 3]
		step = 2
		self.assertEqual(except_data, insertion_sort(self.data, step))		

	def test_insertion_sort_step_3(self):
		except_data = [3, 1, 2, 4]
		step = 3
		self.assertEqual(except_data, insertion_sort(self.data, step))				

	def test_insertion_sort_incorrect_step(self):
		step = 4

		with self.assertRaises(ValueError):
			result = insertion_sort(self.data, step)

if __name__ == '__main__':
	unittest.main(verbosity=2)