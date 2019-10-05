# -*- coding: UTF-8 -*-
#
# Comb Sort Algorithm
# The All ▲lgorithms library for python
#
# Contributed by: Christine Mecklenborg
# Github: @cmecklenborg
#


def comb_sort(arr):
    n = len(arr)
    gap = n
    swapped = True

    while gap != 1 or swapped:
        gap = (gap*10)//13
        swapped = False

        for i in range(n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True

    return arr
