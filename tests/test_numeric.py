import unittest

from allalgorithms.numeric import (
    find_max,
    prime_lower
)

class TestMax(unittest.TestCase):

    def test_find_max_value(self):
        test_list = [3, 1, 8, 7, 4]
        self.assertEqual(8, find_max(test_list))

class TestPrimeLower(unittest.TestCase):

    def test_prime_lower_value(self):
        test_list =[2, 3, 5, 7, 11, 13, 17]
        self.assertEqual(prime_lower(18), test_list)


if __name__ == "__main__":
    unittest.main()
