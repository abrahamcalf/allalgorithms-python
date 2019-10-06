# Merge Sort

In computer science, merge sort is an efficient, general-purpose, comparison-based sorting algorithm. Most implementations produce a stable sort, which means that the implementation preserves the input order of equal elements in the sorted output

## Install

```
pip install allalgorithms
```

## Usage

```py
from allalgorithms.sorting import merge_sort

arr = [77, 2, 10, -2, 1, 7]

print(merge_sort(arr))
# -> [-2, 1, 2, 7, 10, 77]
```

## API

### merge_sort(array)

> Returns a sorted array

##### Params:

- `array`: Unsorted Array
