# Depth first Search

Depth first search enables the finding of a specific node within a graph structure by traversing down the deepest paths first. 
## Install

```
pip install allalgorithms
```

## Usage

```py
from allalgorithms.structures import Graph
from allalgorithms.searches import dfs

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

print(dfs(g, 'A', 'F))
# -> 'F', ['A', 'G', 'H', 'C', 'B', 'D', 'E']


```

## API

### dfs(array, source_node, query)

> Return node name if its found, otherwise returns `None`, as well as the path it took.

##### Params:

- `graph`: Graph object
- `source node`: Element to start search from
- `query`: Element to search for in the array
