# Breadth first search

[Breadth-first search](https://en.wikipedia.org/wiki/Breadth-first_search) (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key'[1]), and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.

## Install

```
pip install allalgorithms
```

## Usage

```py
from allalgorithms.graph import bfs_paths

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

list(bfs_paths(graph, 'A', 'F'))
# -> [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

```

## API

def bfs_paths(graph: Dict[str, set], start: str, destination: str) -> Union[list, None]:

> Return list of lists that contains path to destination from start, if there is not any returns `None`

##### Params:

- `graph`: Dictionary containing the graph to be searched
- `start` : Name of the start node
- `destination` : Name of the destination node
