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
    """
    inputs:
        n: integer

    outputs: list of prime numbers less or equal than n
    """
    assert n>=1 and n<=SIEVE_LIMIT, "input value is not valid"
    prime = sieve(n)
    ans = []
    for i in range(n+1):
        if prime[i]:
            ans.append(i)
    return ans
