import unittest
from DynArray import DynArray

class NodeCase(unittest.TestCase):
	def test_dyn_array_can_insert_element_at_specified_position(self):
		da = DynArray()
		da.append(0)
		da.append(1)
		da.append(3)
		da.append(4)

		da.insert(2, 2)

		self.assertEqual(2, da[2])
		self.assertEqual(3, da[3])

	def test_dyn_array_can_delete_element_from_specified_position(self):
		da = DynArray()
		da.append(0)
		da.append(1)
		da.append(2)
		da.append(3)

		da.delete(3)
		da.delete(2)
		da.delete(1)

		self.assertEqual(0, da[0])
		self.assertEqual(1, len(da))

if __name__ == '__main__':
	unittest.main(verbosity=2)		