import unittest

from allalgorithms.searches import (
    binary_search,
    fibonacci_search,
    dfs
)
from allalgorithms.structures import Graph


class TestSearches(unittest.TestCase):

    def test_binary_search(self):
        arr = [1, 2, 3, 7, 10, 19, 27, 77]
        self.assertEqual(3, binary_search(arr, 7))
        self.assertEqual(7, binary_search(arr, 77))
        self.assertEqual(None, binary_search(arr, 8))
        self.assertEqual(None, binary_search(arr, -1))

    def test_fibonacci_search(self):
        arr = [1, 2, 3, 7, 10, 19, 27, 77]
        self.assertEqual(3, fibonacci_search(arr, 7))
        self.assertEqual(7, fibonacci_search(arr, 77))
        self.assertEqual(None, fibonacci_search(arr, 8))
        self.assertEqual(None, fibonacci_search(arr, -1))

    def test_jump_search(self):
        arr = [1, 2, 3, 7, 10, 19, 27, 77]
        self.assertEqual(3, binary_search(arr, 7))
        self.assertEqual(7, binary_search(arr, 77))
        self.assertEqual(None, binary_search(arr, 8))
        self.assertEqual(None, binary_search(arr, -1))

    def test_dfs_search(self):
        g = Graph()
        g.edges = {
            'A': ['B', 'C', 'G'],
            'B': ['A', 'C', 'D'],
            'C': ['A', 'B'],
            'D': ['B', 'F', 'E'],
            'E': ['D', 'F'],
            'F': ['D', 'E'],
            'G': ['A', 'H'],
            'H': ['G'],
        }
        result = dfs(g, 'A', 'F')
        path = ['A', 'G', 'H', 'C', 'B', 'D', 'E']
        self.assertEqual(('F', path), result)


if __name__ == '__main__':
    unittest.main()
