# Binary Search

In computer science, binary search, also known as half-interval search, logarithmic search, or binary chop, is a search algorithm that finds the position of a target value within a sorted array

## Install

```
pip install allalgorithms
```

## Usage

```py
from allalgorithms.searches import binary_search

arr = [-2, 1, 2, 7, 10, 77]

print(binary_search(arr, 7))
# -> 3

print(binary_search(arr, 3))
# -> None
```

## API

### binary_search(array, query)

> Return array index if its found, otherwise returns `None`

##### Params:

- `array`: Sorted Array
- `query`: Element to search for in the array
