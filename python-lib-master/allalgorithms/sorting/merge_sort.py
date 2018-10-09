# -*- coding: UTF-8 -*-
#
# Merge Sort Algorithm
# The All ▲lgorithms library for python
#
# Contributed by: Carlos Abraham Hernandez
# Github: @abranhe
#
def merge_sort(arr):
    if len(arr) == 1:
        return arr

    left = merge_sort(arr[:(len(arr)//2)])
    right = merge_sort(arr[(len(arr)//2):])
    out = []

    while bool(left) or bool(right):
        if bool(left) ^ bool(right):
            alias = left if left else right
        else:
            alias = left if left[0] < right[0] else right

        out.append(alias[0])
        alias.remove(alias[0])

    return out
