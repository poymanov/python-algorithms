import unittest
from functions import *

class BinarySearchCase(unittest.TestCase):
    def test_binary_search_case_1(self):
        search_item = 2
        search_list = [1, 2, 3, 4]
        search_result = binary_search(search_item, search_list)
        self.assertEqual(1, search_result)

    def test_binary_search_case_2(self):
        search_item = 200
        search_list = [23, 64, 100, 150, 200, 450, 500, 1000]
        search_result = binary_search(search_item, search_list)
        self.assertEqual(4, search_result)

    def test_binary_search_case_3(self):
        search_item = 99
        search_list = [1, 2, 3, 4]
        search_result = binary_search(search_item, search_list)
        self.assertIsNone(search_result)

if __name__ == '__main__':
	unittest.main(verbosity=2)
