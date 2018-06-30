import unittest
import functions
from stack import Stack1, Stack2

class Stack1Case(unittest.TestCase):
	def test_stack_get_last_element_with_pop(self):
		stack = Stack1()
		stack.push(1)
		stack.push("2")
		stack.push(3.14)

		self.assertEqual(3.14, stack.pop())
		self.assertEqual("2", stack.pop())
		self.assertEqual(1, stack.pop())
		self.assertIsNone(stack.pop())

class Stack2Case(unittest.TestCase):
	def test_stack_get_first_element_with_pop(self):
		stack = Stack2()
		stack.push(1)
		stack.push("2")
		stack.push(3.14)

		self.assertEqual(3.14, stack.pop())
		self.assertEqual("2", stack.pop())
		self.assertEqual(1, stack.pop())
		self.assertIsNone(stack.pop())

class FunctionsCase(unittest.TestCase):
	def test_is_balanced(self):
		string1 = '(()((())()))'
		string2 = '(()()(()'
		string3 = '()'
		string4 = '()(()()'

		self.assertTrue(functions.is_balanced(string1))
		self.assertFalse(functions.is_balanced(string2))
		self.assertTrue(functions.is_balanced(string3))
		self.assertFalse(functions.is_balanced(string4))

	def test_calc_postfix_variables(self):
		string1 = '1 2 + 3 * ='
		string2 = '8 2 + 5 * 9 + ='

		self.assertEqual(9, functions.calc_postfix_variable(string1))
		self.assertEqual(59, functions.calc_postfix_variable(string2))		
		
if __name__ == '__main__':
	unittest.main(verbosity=2)		