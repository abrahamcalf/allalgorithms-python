# -*- coding: UTF-8 -*-
#
# Check fibonacci number
# The All ▲lgorithms library for python
#
# Contributed by: Natan Lucena
# Github: @NatanLucena
#

import math 
  
def isPerfectSquare(x): 
    s = int(math.sqrt(x)) 
    return s*s == x 
  
def isFibonacci(n): 

    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4) 
