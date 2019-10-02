# -*- coding: UTF-8 -*-
#
# find path from a node to another node using dfs algorithm.
# The All ▲lgorithms library for python
# Code credit: https://github.com/eddmann
# Contributed by: glyphack
# Github: @glyphack
#
from typing import Dict, Union


def dfs_paths(graph: Dict[str, set], start: str, destination: str) -> Union[list, None]:
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == destination:
                yield path + [next]
            else:
                stack.append((next, path + [next]))
