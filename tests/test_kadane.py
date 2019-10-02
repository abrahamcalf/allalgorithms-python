import unittest

from allalgorithms.subarray import kadane

class TestSearches(unittest.TestCase):

	def test_returnArray(self):
		self.assertEqual( [11,[2,3,-1,7]], binary_search([2,3,-1,7]))
		self.assertEqual([5,[2,3]], binary_search([2,3,-2,4]))
		self.assertEqual([0, [0]], binary_search([-1,-1,-0,0]))
		self.assertEqual([-1, [-1]], binary_search([-1]))

	def test_maxsum_subarray(self):
  	self.assertEqual( 11,, binary_search([2,3,-1,7]))
		self.assertEqual(5, binary_search([2,3,-2,4]))
		self.assertEqual(0, binary_search([-1,-1,-0,0]))
		self.assertEqual(-1, binary_search([-1]))

if __name__ == '__main__':
	unittest.main()
