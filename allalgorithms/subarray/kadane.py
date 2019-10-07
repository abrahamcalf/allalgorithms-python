# -*- coding: UTF-8 -*-
#
# Kadane's Algorithm
# The All ▲lgorithms library for python
#
# Contributed by: Kunal Keshav Singh Sahni 
# Github: @kunal768
#

import sys

def maxsum_subarray(arr):
	curr = arr[0]
	maxx = arr[0]
	n = len(arr)

	for i in range(1,n):
		curr = max(arr[i],curr+arr[i])
		maxx = max(curr,maxx)

	return maxx


def returnArray(arr):
    size = len(arr) 
    max_so_far = -sys.maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
    for i in range(0,size): 
  
        max_ending_here += arr[i] 
  
        if max_so_far < max_ending_here: 
            max_so_far = max_ending_here 
            start = s 
            end = i 
  
        if max_ending_here < 0: 
            max_ending_here = 0
            s = i+1

    return [max_so_far,arr[start:end+1]]
