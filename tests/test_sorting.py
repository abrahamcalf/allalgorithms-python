import unittest

from allalgorithms.sorting import (
    bubble_sort,
    insertion_sort,
    merge_sort,
    selection_sort,
    pigeonhole_sort,
    stooge_sort,
    cocktail_shaker_sort,
    tree_sort,
    shell_sort,
    comb_sort,
)


class TestSorting(unittest.TestCase):
    def test_merge_sort(self):
        self.assertEqual([-44, 1, 2, 3, 7, 19], merge_sort([7, 3, 2, 19, -44, 1]))

    def test_bubble_sort(self):
        self.assertEqual([-44, 1, 2, 3, 7, 19], bubble_sort([7, 3, 2, 19, -44, 1]))

    def test_insertion_sort(self):
        self.assertEqual([-44, 1, 2, 3, 7, 19], insertion_sort([7, 3, 2, 19, -44, 1]))

    def test_selection_sort(self):
        self.assertEqual([-44, 1, 2, 3, 7, 19], selection_sort([7, 3, 2, 19, -44, 1]))

    def test_pigeonhole_sort(self):
        self.assertEqual([-44, 1, 2, 3, 7, 19], pigeonhole_sort([7, 3, 2, 19, -44, 1]))

    def test_stooge_sort(self):
        self.assertEqual([-44, 1, 2, 3, 7, 19], stooge_sort([7, 3, 2, 19, -44, 1]))

    def test_cocktail_shaker_sort(self):
        self.assertEqual([-44, 1, 2, 3, 7, 19], cocktail_shaker_sort([7, 3, 2, 19, -44, 1]))
    
    def tree_sort(self):
        self.assertEqual([-44, 1, 2, 3, 7, 19], tree_sort([7, 3, 2, 19, -44, 1]))

    def test_shell_sort(self):
        self.assertEqual([-44, 1, 2, 3, 7, 19], shell_sort([7, 3, 2, 19, -44, 1]))

    def test_comb_sort(self):
        self.assertEqual([-44, 1, 2, 3, 7, 19], comb_sort([7, 3, 2, 19, -44, 1]))


if __name__ == "__main__":
    unittest.main()
