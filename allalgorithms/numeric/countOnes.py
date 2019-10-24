# -*- coding: UTF-8 -*-
#
# count ones in a array
# The All ▲lgorithms library for python
#
# Contributed by: Natan Lucena
# Github: @NatanLucena
#


def countOnes(arr,low,high): 
      
    if high>=low: 
           
        mid = low + (high-low)/2
           
        if ((mid == high or arr[mid+1]==0) and (arr[mid]==1)): 
            return mid+1
 
        if arr[mid]==1: 
            return countOnes(arr, (mid+1), high) 

        return countOnes(arr, low, mid-1) 
      
    return 0
