import unittest
from AssocArray import AssocArray

class AssocArrayCase(unittest.TestCase):
	def setUp(self):
		self.hash_size = 19
		self.hash_step = 3

	def test_add_new_value(self):
		assoc_array = AssocArray(self.hash_size, self.hash_step)
		assoc_array.put('key', 'value')

		self.assertIsNotNone(assoc_array.slots[6])
		self.assertEqual('key', assoc_array.slots[6])

		self.assertIsNotNone(assoc_array.values[6])
		self.assertEqual('value', assoc_array.values[6])

	def test_check_key_exists(self):
		assoc_array = AssocArray(self.hash_size, self.hash_step)
		assoc_array.put('key', 'value')

		self.assertTrue(assoc_array.is_key('key'))
		self.assertFalse(assoc_array.is_key('key2'))

	def test_get_value_by_key(self):
		assoc_array = AssocArray(self.hash_size, self.hash_step)
		assoc_array.put('key', 'value')

		self.assertEqual('value', assoc_array.get('key'))
		self.assertIsNone(assoc_array.get('key2'))

if __name__ == '__main__':
	unittest.main(verbosity=2)		