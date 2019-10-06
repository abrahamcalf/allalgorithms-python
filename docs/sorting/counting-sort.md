# Counting sort
Counting sort is a sorting algorithm which does not actually sort
the array but rather reconstructs it. It operates by counting how
often every unique item (e.g., a certain number) occurs, sorts the
unique items by TreeSort and then reconstructs an array by copying
every unique item (the number of occurences)th times into the result.
Its advantage is the fast computation which is only linear with respect
of the input array *if* the number of unique items is significantly
smaller than the number of items.

## Install

```
pip install allalgorithms
```

## Usage

```py
from allalgorithms.sorting import counting_sort

arr = [77, 2, 10, -2, 1, 7]

print(counting_sort(arr))
# -> [-2, 1, 2, 7, 10, 77]
```

## API

```
counting_sort(array)
```

> Returns a sorted array (does in-place replacements)

##### Params:

- `array`: Array to sort

