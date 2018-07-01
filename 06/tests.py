import unittest
import functions
from queue import Queue

class TasksCase(unittest.TestCase):
	def test_rotate_quenue_by_n_elements(self):
		qu = Queue()
		qu.enqueue(1)
		qu.enqueue(2)
		qu.enqueue(3)
		qu.enqueue(4)
		qu.enqueue(5)

		self.assertEqual([5, 4, 3, 2, 1], qu.items)

		functions.rotate_queue(qu, 4)

		self.assertEqual([4, 3, 2, 1, 5], qu.items)

if __name__ == '__main__':
	unittest.main(verbosity=2)		