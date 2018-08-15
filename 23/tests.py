import unittest
from functions import *

class PartitioningCase(unittest.TestCase):
	def test_partitioning_case_1(self):
		data = [15, 18, 2, 36, 12, 78, 5, 6, 9];
		result = partitioning(data, 15)
		self.check_result(data, result)

	def test_partitioning_case_2(self):
		data = [2, 2, 2, 2, 2, 2];
		result = partitioning(data, 2)

		i1 = result['i1']
		i2 = result['i2']

		self.assertEqual(i1, 0)
		self.assertEqual(i2, 5)

	def test_partitioning_case_3(self):
		data = [2, 2, 2, 2, 2, 2];
		result = partitioning(data, 3)
		self.check_result(data, result)

	def test_partitioning_case_4(self):
		data = [2, 5, 8, 11, 20, 3];
		result = partitioning(data, 1)
		self.check_result(data, result)

	def test_partitioning_case_5(self):
		data = [2, 5, 8, 11, 20, 3];
		result = partitioning(data, 25)
		self.check_result(data, result)

	def check_result(self, data, result):
		i1 = result['i1']
		i2 = result['i2']

		self.assertEqual(i1, i2 - 1)
		self.assertIn(data[i1], data)
		self.assertIn(data[i2], data)
		

if __name__ == '__main__':
	unittest.main(verbosity=2)