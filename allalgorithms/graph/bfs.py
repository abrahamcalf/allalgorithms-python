# -*- coding: UTF-8 -*-
#
# find path from a node to another node using bfs algorithm.
# The All ▲lgorithms library for python
# Code credit: https://github.com/eddmann
# Contributed by: glyphack
# Github: @glyphack

from typing import Dict, Union


def bfs_paths(graph: Dict[str, set], start: str, destination: str) -> Union[list, None]:
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == destination:
                yield path + [next]
            else:
                queue.append((next, path + [next]))
