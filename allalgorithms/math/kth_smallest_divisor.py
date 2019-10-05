# -*- coding: UTF-8 -*-
#
# Find the k-th smallest divisor of a natural number.
# The All ▲lgorithms library for python
#
# Contributed by: Higor Santos
# Github: @higorsnt
#


def kth_divisor(number, k):
    vector1 = []
    vector2 = []

    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            vector1.append(i)

            if i != int(number ** 0.5) + 1:
                vector2.append(number // i)
    vector2.reverse()

    if k > (len(vector1) + len(vector2)):
        raise ValueError("Doesn't Exist")
    else:
        if (k - 1) < len(vector1):
            return vector1[k - 1]
        else:
            return vector2[k - len(vector1) - 1]
