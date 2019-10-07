import unittest

from allalgorithms.numeric import find_max
from allalgorithms.fibonacci import fibonacci, fibonacci_memo


class TestMax(unittest.TestCase):

    def test_find_max_value(self):
        test_list = [3, 1, 8, 7, 4]
        self.assertEqual(8, find_max(test_list))


class TestFibonacci(unittest.TestCase):

    def test_recursive_fibonacci(self):
        self.assertEqual(8, fibonacci(7))

    def test_memoize_fibonacci(self):
        self.assertEqual(8, fibonacci(7))


if __name__ == "__main__":
    unittest.main()
