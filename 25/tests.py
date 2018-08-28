import unittest
from ksort import ksort
import random

class ksortCase(unittest.TestCase):
    def test_ksort_case_1(self):
        data = ['g99', 'a01', 'b64']

        sorted_data = self.get_sorted_data(data)

        ksort_session = ksort(data)
        self.assertEqual(sorted_data, ksort_session.sort())

    def test_ksort_case_2(self):
        data = ['a11', 'e79', 'c64']

        sorted_data = self.get_sorted_data(data)

        ksort_session = ksort(data)
        self.assertEqual(sorted_data, ksort_session.sort())

    def test_ksort_case_3(self):
        data = ['c11', 'e65', 'd30']

        sorted_data = self.get_sorted_data(data)

        ksort_session = ksort(data)
        self.assertEqual(sorted_data, ksort_session.sort())

    def get_sorted_data(self, data):
        sorted_data = data[:]
        sorted_data.sort()
        return sorted_data

if __name__ == '__main__':
	unittest.main(verbosity=2)
