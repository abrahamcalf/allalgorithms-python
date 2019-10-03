import unittest

from allalgorithms.graph import (
    dfs_paths,
    bfs_paths
)


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


    def test_bfs(self):
        self.assertEqual([['A', 'C', 'F'], ['A', 'B', 'E', 'F']], list(bfs_paths(self.test_graph, 'A', 'F')))


if __name__ == "__main__":
    unittest.main()
