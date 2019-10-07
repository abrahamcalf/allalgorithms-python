# Kadane's Algorithm 

Kadane’s algorithm is to look for all positive contiguous segments of the array (max_ending_here is used for this). And keep track of maximum sum contiguous segment among all positive segments (max_so_far is used for this) Each time we get a positive sum compare it with max_so_far and update max_so_far if it is greater than max_so_far
## Install

```
pip install allalgorithms
```

## Usage

```py
from allalgorithms.subarray import kadane

arr = [-2, 1, 2, 7, 10, 77]

print(kadane.maxsum_subarray(arr))
# -> 97

print(kadane.returnArray(arr))
# -> [97, [1, 2, 7, 10, 77]]
```

## API

### maxsum_subarray(array)

> Return sum of maximum contigious subarray

### returnArray(array)

> Return sum along with the respective subarray

##### Params:

- `array`: Array (may contain negative elements)
