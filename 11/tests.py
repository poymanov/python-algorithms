import unittest
from PowerSet import PowerSet

class PowerSetCase(unittest.TestCase):
	def setUp(self):
		self.value = 'hello world'
		self.size = 19
		self.step = 3

	def test_failed_to_put_same_value(self):
		power_set = PowerSet(self.size, self.step)
		power_set.put(self.value)
		
		with self.assertRaises(Exception):
			power_set.put(self.value)

	def test_remove_value(self):		
		power_set = PowerSet(self.size, self.step)
		power_set.put(self.value)

		power_set.remove(self.value)
		self.assertIsNone(power_set.find(self.value))
		self.assertIsNone(power_set.remove('not_exist_value'))
			
	def	test_find_same_elements(self):
		power_set1 = PowerSet(self.size, self.step)
		power_set1.put('value1')
		power_set1.put('value2')
		power_set1.put('value4')
		power_set1.put('value5')

		power_set2 = PowerSet(self.size, self.step)
		power_set2.put('value1')
		power_set2.put('value2')
		power_set2.put('value6')
		power_set2.put('value7')

		power_set3 = power_set1.intersection(power_set2)

		self.assertIsNotNone(power_set3.find('value1'))
		self.assertIsNotNone(power_set3.find('value2'))
		self.assertIsNone(power_set3.find('value4'))
		self.assertIsNone(power_set3.find('value5'))
		self.assertIsNone(power_set3.find('value6'))
		self.assertIsNone(power_set3.find('value7'))

	def test_union_some_elements(self):
		power_set1 = PowerSet(self.size, self.step)
		power_set1.put('value1')
		power_set1.put('value2')
		power_set1.put('value4')
		power_set1.put('value5')

		power_set2 = PowerSet(self.size, self.step)
		power_set2.put('value1')
		power_set2.put('value2')
		power_set2.put('value6')
		power_set2.put('value7')

		power_set3 = power_set1.union(power_set2)

		self.assertIsNotNone(power_set3.find('value1'))
		self.assertIsNotNone(power_set3.find('value2'))
		self.assertIsNotNone(power_set3.find('value4'))
		self.assertIsNotNone(power_set3.find('value5'))
		self.assertIsNotNone(power_set3.find('value6'))
		self.assertIsNotNone(power_set3.find('value7'))

	def test_get_different_elements(self):
		power_set1 = PowerSet(self.size, self.step)
		power_set1.put('value1')
		power_set1.put('value2')
		power_set1.put('value4')
		power_set1.put('value5')

		power_set2 = PowerSet(self.size, self.step)
		power_set2.put('value1')
		power_set2.put('value2')
		power_set2.put('value6')
		power_set2.put('value7')

		power_set3 = power_set1.difference(power_set2)

		self.assertIsNone(power_set3.find('value1'))
		self.assertIsNone(power_set3.find('value2'))
		self.assertIsNone(power_set3.find('value6'))
		self.assertIsNone(power_set3.find('value7'))

		self.assertIsNotNone(power_set3.find('value4'))
		self.assertIsNotNone(power_set3.find('value5'))

	def test_check_subset(self):
		power_set1 = PowerSet(self.size, self.step)
		power_set1.put('value1')
		power_set1.put('value2')
		power_set1.put('value3')
		power_set1.put('value4')
		power_set1.put('value5')

		power_set2 = PowerSet(self.size, self.step)
		power_set2.put('value1')
		power_set2.put('value2')

		power_set3 = PowerSet(self.size, self.step)
		power_set3.put('value7')
		power_set3.put('value8')

		self.assertTrue(power_set1.issubset(power_set2))
		self.assertFalse(power_set1.issubset(power_set3))

if __name__ == '__main__':
	unittest.main(verbosity=2)		