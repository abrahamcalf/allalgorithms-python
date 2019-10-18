# -*- coding: UTF-8 -*-
#
# BogoSort Algorithm
# The All ▲lgorithms library for python
#
# Contributed by: Cayo Viegas
# Github: @CayoViegas
#

from random import shuffle

def bogosort(seq):
	while not all(x <= y for x, y in zip(seq, seq[1:])):
		shuffle(seq)
	
	return seq
	
