import unittest
import functions

class TasksCase(unittest.TestCase):
	def test_check_palindrom_with_deque(self):		
		self.assertTrue(functions.check_palindrom('eye'))
		self.assertTrue(functions.check_palindrom('pop'))
		self.assertFalse(functions.check_palindrom('test'))
		self.assertFalse(functions.check_palindrom('python'))

if __name__ == '__main__':
	unittest.main(verbosity=2)		