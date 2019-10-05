import unittest

from allalgorithms.math import (
    find_max,
    kth_divisor
)


class TestMath(unittest.TestCase):

    def test_find_max_value(self):
        test_list = [3, 1, 8, 7, 4]
        self.assertEqual(8, find_max(test_list))

    def test_find_kth_divisor_of_prime_number(self):
        self.assertEqual(1, kth_divisor(257, 1))
        self.assertEqual(257, kth_divisor(257, 2))
        with self.assertRaises(ValueError):
            kth_divisor(257, 3)

    def test_find_kth_divisor_of_even_number(self):
        self.assertEqual(7, kth_divisor(728, 4))
        self.assertEqual(91, kth_divisor(728, 12))
        self.assertEqual(364, kth_divisor(728, 15))
        with self.assertRaises(ValueError):
            kth_divisor(728, 17)

    def test_find_kth_divisor_of_odd_number(self):
        self.assertEqual(459, kth_divisor(162027, 9))
        self.assertEqual(18003, kth_divisor(162027, 14))
        self.assertEqual(162027, kth_divisor(162027, 16))
        with self.assertRaises(ValueError):
            kth_divisor(162027, 17)


if __name__ == "__main__":
    unittest.main()
