# -*- coding: UTF-8 -*-
#
# Numeric Algorithms
# The All ▲lgorithms library for python
#
# Contributed by: Rodolfo
# Github: @RQuispeC
#
import math

SIEVE_LIMIT = 1000000

def sieve(n):
    prime = [True]*(n+1)
    prime[0] = False
    prime[1] = False
    for i in range(2,int(math.sqrt(n)) + 1):
        if prime[i]:
            for j in range(i*i, n+1, i):
                prime[j] = False
    return prime

def prime_lower(n):
    if n < 1 or n > SIEVE_LIMIT:
        return []
    prime = sieve(n)
    ans = []
    for i in range(n+1):
        if prime[i]:
            ans.append(i)
    return ans
