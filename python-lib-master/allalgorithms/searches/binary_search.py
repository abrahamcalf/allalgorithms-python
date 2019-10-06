# -*- coding: UTF-8 -*-
#
# Binary search works for a sorted array.
# The All ▲lgorithms library for python
#
# Contributed by: Carlos Abraham Hernandez
# Github: @abranhe
#
def binary_search(arr, query):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (hi + lo) // 2
        val = arr[mid]
        if val == query:
            return mid
        elif val < query:
            lo = mid + 1
        else:
            hi = mid - 1
    return None
