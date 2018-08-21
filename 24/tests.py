import unittest
from quicksort import quicksort
import random

class QuicksortCase(unittest.TestCase):
	def test_quicksort_case_1(self):
		data = self.create_sort_data(5, 10)
		except_data = self.create_excepted_data(data)
		self.assertEqual(except_data, quicksort(data))

	def test_quicksort_case_2(self):
		data = self.create_sort_data(10, 20)
		except_data = self.create_excepted_data(data)
		self.assertEqual(except_data, quicksort(data))		

	def test_quicksort_case_3(self):
		data = self.create_sort_data(20, 200)
		except_data = self.create_excepted_data(data)
		self.assertEqual(except_data, quicksort(data))				
		
	def create_sort_data(self, value_min, value_max):
		length = random.randint(value_min, value_max)

		data = []

		for _ in range(length):
			data.append(random.randint(0, 100))		

		return data

	def create_excepted_data(self, data):
		except_data = data[:]	
		except_data.sort()	

		return except_data
		
if __name__ == '__main__':
	unittest.main(verbosity=2)