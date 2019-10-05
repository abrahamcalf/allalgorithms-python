# Comb Sort

Comb sort is an improvement on ubble sort, which compares elements separate by a gap and swaps them if necessary. After each iteration, the gap shrinks by a factor of 1.3, until a gap of 1 is reached. Though this algorithm is more efficient than bubble sort on average, its worst case performance is still O(n^2). Best-case performance is O(n log n).

## Install

```
pip install allalgorithms
```

## Usage

```py
from allalgorithms.sorting import comb_sort

arr = [77, 2, 10, -2, 1, 7]

print(comb_sort(arr))
# -> [-2, 1, 2, 7, 10, 77]
```

## API

### comb_sort(array)

> Returns a sorted array

##### Params:

- `array`: Unsorted Array
