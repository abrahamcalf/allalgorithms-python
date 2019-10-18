# -*- coding: UTF-8 -*-
#
# Find Minimum Algorithm
# The All ▲lgorithms library for python
#
# Contributed by: Cayo Viegas
# Github: @CayoViegas
#

def find_min(L):
	min = L[0]
		
	for x in L:
		if x < min:
			min = x
				
	return min
