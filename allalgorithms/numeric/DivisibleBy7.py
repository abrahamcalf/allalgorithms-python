# -*- coding: UTF-8 -*-
#
# Divisible by 7 algorithm
# The All ▲lgorithms library for python
#
# Contributed by: Natan Lucena
# Github: @NatanLucena
#

def isDivisibleBy7(num) : 
      
    if num < 0 : 
        return isDivisibleBy7( -num ) 
  
    if( num == 0 or num == 7 ) : 
        return True
      
    if( num < 10 ) : 
        return False
          
    return isDivisibleBy7( num / 10 - 2 * ( num - num / 10 * 10 ) )     
