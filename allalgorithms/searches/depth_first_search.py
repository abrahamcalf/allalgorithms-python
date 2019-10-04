# -*- coding: UTF-8 -*-
#
# Depth first search works for a graph structure, comprised of adjacency lists.
# The All ▲lgorithms library for python
#
# Contributed by: Thomas Basche
# Github: @tombasche
#
from graph import Graph


def dfs(graph: Graph, source: str, target: str):
    """
    Given a graph and a source node, find a target using Depth-first search

    Great for traversing directed acyclic graphs, and thus job scheduling.
    """
    visited = [source]
    path = []
    steps = 1
    while visited:
        node = visited.pop()
        if node == target:
            return target
        if node in path:
            continue
        path.append(node)
        for neighbour in graph.neighbours(node):
            visited.append(neighbour)
            steps += 1
