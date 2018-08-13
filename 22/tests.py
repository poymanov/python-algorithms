import unittest
from functions import *
import random

class InsertionSortCase(unittest.TestCase):
	def test_shell_sort_case_1(self):
		data = self.create_sort_data(5, 10)

		except_data = data[:]	
		except_data.sort()	

		self.assertEqual(except_data, shell_sort(data))

	def test_shell_sort_case_2(self):
		data = self.create_sort_data(10, 20)

		except_data = data[:]	
		except_data.sort()	

		self.assertEqual(except_data, shell_sort(data))

	def test_shell_sort_case_3(self):
		data = self.create_sort_data(20, 200)

		except_data = data[:]	
		except_data.sort()	

		self.assertEqual(except_data, shell_sort(data))

	def create_sort_data(self, value_min, value_max):
		length = random.randint(value_min, value_max)

		data = []

		for _ in range(length):
			data.append(random.randint(0, 100))		

		return data


if __name__ == '__main__':
	unittest.main(verbosity=2)