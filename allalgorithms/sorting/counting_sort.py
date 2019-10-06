# -*- coding: UTF-8 -*-
#
# Radix Sort Algorithm
# The All ▲lgorithms library for python
#
# Contributed by: Nicholas Gao
# Github: @n-gao
#
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def add_child(self, value):
        if value < self.value:
            if self.left_child is None:
                self.left_child = BinaryTree(value)
            else:
                self.left_child.add_child(value)
        else:
            if self.right_child is None:
                self.right_child = BinaryTree(value)
            else:
                self.right_child.add_child(value)

    def get_sorted_values(self):
        result = []
        if self.left_child is not None:
            result = self.left_child.get_sorted_values()
        result.append(self.value)
        if self.right_child is not None:
            result = result + self.right_child.get_sorted_values()
        return result

def counting_sort(arr):
    counts = {}
    tree = None
    for value in arr:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = counts[value] + 1 if value in counts else 1
            if tree is None:
                tree = BinaryTree(value)
            else:
                tree.add_child(value)

    sorted_values = tree.get_sorted_values()
    i = 0
    for value in sorted_values:
        for _ in range(counts[value]):
            arr[i] = value
            i += 1

    return arr
