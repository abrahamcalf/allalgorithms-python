# -*- coding: UTF-8 -*-
#
# Heap Sort Algorithm
# The All ▲lgorithms library for python
#
# Contributed by: DatHydroGuy
# Github: @DatHydroGuy
#


def build_heap(array_to_sort, array_length, index):
    """
    Build a heap, where each node has two child nodes, and a root node is greater than both child nodes.
    """
    largest = index         # Flag the largest element as the last (root) element
    left = 2 * index + 1    # Calculate index of left child node
    right = 2 * index + 2   # Calculate index of right child node

    # See if left child of root exists and is greater than root
    if left < array_length and array_to_sort[index] < array_to_sort[left]:
        largest = left

    # See if right child of root exists and is greater than root
    if right < array_length and array_to_sort[largest] < array_to_sort[right]:
        largest = right

    # If a larger element than root was found, swap with root so that root holds the new largest value
    if largest != index:
        array_to_sort[index], array_to_sort[largest] = array_to_sort[largest], array_to_sort[index]  # swap

        # Re-build the heap under the new largest root node
        build_heap(array_to_sort, array_length, largest)


def heap_sort(array_to_sort):
    """
    Builds a max-heap, then continuously removes the largest element and re-builds the heap until sorted
    """
    array_length = len(array_to_sort)

    # Build a max-heap to sort the elements into order
    for index in range(array_length // 2 - 1, -1, -1):
        build_heap(array_to_sort, array_length, index)

    # One by one extract elements
    for index in range(array_length - 1, 0, -1):
        array_to_sort[index], array_to_sort[0] = array_to_sort[0], array_to_sort[index]  # swap
        build_heap(array_to_sort, index, 0)
