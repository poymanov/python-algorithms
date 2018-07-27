import unittest
from Heap import Heap

class HeapCase(unittest.TestCase):
	def setUp(self):
		heap = Heap(3, 1)
		heap.add(2)
		heap.add(3)
		heap.add(4)
		heap.add(5)
		self.heap = heap

	def test_init_heap(self):
		heap = Heap(4, 50)

		result_data = [None] * 15
		result_data[0] = 50

		self.assertEqual(result_data, heap.data)

	def test_create_heap(self):
		result_data = [5, 4, 3, 2, 1, None, None]

		self.assertEqual(result_data, self.heap.data)

	def	test_delete_max_element(self):
		result_data = [4, 3, 2, 1, None, None, None]
		self.heap.delete_max()
		self.assertEqual(result_data, self.heap.data)

if __name__ == '__main__':
	unittest.main(verbosity=2)
