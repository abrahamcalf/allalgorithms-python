import unittest

from allalgorithms.graph import dfs_paths


class TestGraph(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.test_graph = {
            "A": set(["B", "C"]),
            "B": set(["A", "D", "E"]),
            "C": set(["A", "F"]),
            "D": set(["B"]),
            "E": set(["B", "F"]),
            "F": set(["C", "E"]),
        }

    def test_dfs(self):
        self.assertEqual([['A', 'B', 'E', 'F'], ['A', 'C', 'F']], list(dfs_paths(self.test_graph, 'A', 'F')))


if __name__ == "__main__":
    unittest.main()
