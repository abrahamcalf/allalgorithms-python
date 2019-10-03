import unittest

from allalgorithms.subarray import kadane

class TestSearches(unittest.TestCase):
	def test_returnArray(self):
		self.assertEqual( [11,[2,3,-1,7]], kadane.returnArray([2,3,-1,7]))
		self.assertEqual([5,[2,3]], kadane.returnArray([2,3,-2,4]))
		self.assertEqual([0, [0]], kadane.returnArray([-1,-1,-0,0]))
		self.assertEqual([-1, [-1]], kadane.returnArray([-1]))

	def test_maxsum_subarray(self):
		self.assertEqual(11,kadane.maxsum_subarray([2,3,-1,7]))
		self.assertEqual(5, kadane.maxsum_subarray([2,3,-2,4]))
		self.assertEqual(0, kadane.maxsum_subarray([-1,-1,-0,0]))
		self.assertEqual(-1, kadane.maxsum_subarray([-1]))

if __name__ == '__main__':
	unittest.main()
