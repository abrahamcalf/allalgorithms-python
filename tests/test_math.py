import unittest

from allalgorithms.math import (
    find_max
)

class TestMax(unittest.TestCase):

    def test_find_max_value(self):
        test_list = [3, 1, 8, 7, 4]
        self.assertEqual(8, find_max(test_list))

if __name__ == "__main__":
    unittest.main()
