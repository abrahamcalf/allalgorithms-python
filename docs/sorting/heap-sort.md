# Heap Sort

Heap sort is a comparison-based sorting algorithm which operates on a Binary Heap data structure. It can be regarded as a version of Selection sort which is improved by use of the heap data structure rather than a linear-time search.

Heap sort is typically slower than Quicksort, but it does have a better worst-case scenario of O(n log n).  It is an in-place algorithm, but does not produce a stable sort.

## Install

```
pip install allalgorithms
```

## Usage

```py
from allalgorithms.sorting import heap_sort

arr = [77, 2, 10, -2, 1, 7]
heap_sort(arr)

print(arr)
# -> [-2, 1, 2, 7, 10, 77]
```

## API

### heap_sort(array)

> Performs an in-place sort of the passed-in array

##### Params:

- `array`: Unsorted Array
