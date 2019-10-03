import unittest

from allalgorithms.kadane import *

class TestSearches(unittest.TestCase):
	def test_returnArray(self):
		self.assertEqual( [11,[2,3,-1,7]], returnArray([2,3,-1,7]))
		self.assertEqual([5,[2,3]], returnArray([2,3,-2,4]))
		self.assertEqual([0, [0]], returnArray([-1,-1,-0,0]))
		self.assertEqual([-1, [-1]], returnArray([-1]))

	def test_maxsum_subarray(self):
		self.assertEqual(11,maxsum_subarray([2,3,-1,7]))
		self.assertEqual(5, maxsum_subarray([2,3,-2,4]))
		self.assertEqual(0, maxsum_subarray([-1,-1,-0,0]))
		self.assertEqual(-1, maxsum_subarray([-1]))

if __name__ == '__main__':
	unittest.main()
