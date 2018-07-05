import unittest
from HashTable import HashTable

class HashTableCase(unittest.TestCase):
	def setUp(self):
		self.hash_value = 'hello world'
		self.hash_size = 19
		self.hash_step = 3

	def test_hash_fun_create_correct_index(self):		
		hash_table = HashTable(self.hash_size, self.hash_step)
		self.assertEqual(14, hash_table.hash_fun(self.hash_value))

	def test_seek_slot_for_value(self):		
		hash_table = HashTable(self.hash_size, self.hash_step)
		self.assertIsNotNone(hash_table.seek_slot(self.hash_value))

	def test_put_value_to_slot(self):
		value = "hello world"
		hash_table = HashTable(self.hash_size, self.hash_step)
		hash_table.put(self.hash_value)
		self.assertEqual(self.hash_value, hash_table.slots[14])

	def test_find_value_in_hash_table(self):
		missing_value = 'goodbye world'

		hash_table = HashTable(self.hash_size, self.hash_step)
		hash_table.put(self.hash_value)

		#self.assertEqual(14, hash_table.find(self.hash_value))	
		self.assertIsNone(hash_table.find(missing_value))


if __name__ == '__main__':
	unittest.main(verbosity=2)		