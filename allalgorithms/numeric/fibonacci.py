# -*- coding: UTF-8 -*-
#
# Numeric Algorithms: Factorials and Memoization
# The All ▲lgorithms library for python
#
# Contributed by: Chance
# Github: @chance-nelson
#


def fibonacci(n):
    """Compute the Fibonacci sequence number at a certain index

    This is the obvious recursive approach, and runs on the order of O(n*2).
    """
    # Base case 1: fibonacci(1) == 0
    if n == 1:
        return 0

    # Base case 2: fibonacci(2) == 1
    elif n == 2:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


def memoize(f):
    """Special decorator to add memoization to any recursive function

    Keep a cache of results from past runs. This cache can then be referenced
    instead of calling the function again.
    """
    memory = {}
    
    def inner(num):
        if num not in memory:
            memory[num] = f(num)

        return memory[num]

    return inner


fibonacci_memo = memoize(fibonacci)
