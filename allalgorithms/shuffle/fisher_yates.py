# -*- coding: UTF-8 -*-
#
# Binary search works for a sorted array.
# The All ▲lgorithms library for python
#
# Contributed by: a1phyte
# Github: @a1phyte
#
import random

def fisher_yates(unshuffled: list) -> list:
    i = len(unshuffled) - 1;
    shuffled = list();
    while i > 0:
        shuffled.append(unshuffled.pop(random.randint(0, i)))
    shuffled.append(unshuffled.pop())