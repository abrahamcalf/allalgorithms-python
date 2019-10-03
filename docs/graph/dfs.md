# Breath first search

[Depth-first search](https://en.wikipedia.org/wiki/Depth-first_search) (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.

## Install

```
pip install allalgorithms
```

## Usage

```py
from allalgorithms.graph import dfs_path

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

list(dfs_paths(graph, 'A', 'F'))
# -> [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

```

## API

def dfs_paths(graph: Dict[str, set], start: str, destination: str) -> Union[list, None]:

> Return list of lists that contain path to destination from start, if there is not any returns `None`

##### Params:

- `graph`: Dictionary containing the graph to be searched
- `start` : Name of the start node
- `destination` : Name of the destination node
