# -*- coding: UTF-8 -*-
#
# OddEven Sort Algorithm
# The All ▲lgorithms library for python
#
# Contributed by: Cayo Viegas
# Github: @CayoViegas
#

def oddEvenSort(arr, n): 
    isSorted = 0
    while isSorted == 0: 
        isSorted = 1
        temp = 0
        for i in range(1, n-1, 2): 
            if arr[i] > arr[i+1]: 
                arr[i], arr[i+1] = arr[i+1], arr[i] 
                isSorted = 0
                  
        for i in range(0, n-1, 2): 
            if arr[i] > arr[i+1]: 
                arr[i], arr[i+1] = arr[i+1], arr[i] 
                isSorted = 0
      
    return arr
    
