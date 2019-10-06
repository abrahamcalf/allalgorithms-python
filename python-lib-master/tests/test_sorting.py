from allalgorithms.sorting import (
	merge_sort
)
import unittest

class TestSorting(unittest.TestCase):

	def test_merge_sort(self):
		self.assertEqual([-44, 1, 2, 3, 7, 19], merge_sort([7, 3, 2, 19, -44, 1]))

if __name__ == "__main__":
	unittest.main()
