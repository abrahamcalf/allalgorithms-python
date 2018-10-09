from allalgorithms.searches import (
	binary_search
)

import unittest

class TestSearches(unittest.TestCase):

	def test_binary_search(self):
		arr = [1, 2, 3, 7, 10, 19, 27, 77]
		self.assertEqual(3, binary_search(arr, 7))
		self.assertEqual(7, binary_search(arr, 77))
		self.assertEqual(None, binary_search(arr, 8))
		self.assertEqual(None, binary_search(arr, -1))

if __name__ == '__main__':
	unittest.main()
