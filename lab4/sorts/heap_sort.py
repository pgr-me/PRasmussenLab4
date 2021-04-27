"""Peter Rasmussen, Lab 4, heap_sort.py

This module implements a recursive version of the heap sort.

"""

# Standard library imports
from typing import Union


class HeapError(Exception):
    pass


def heapify(li: list, parent_ix, n_items_to_sort: Union[int, None]):
    """
    Heapify an l.
    :param li: Array to heapify
    :param parent_ix: Parent (i.e., root) index of subtree
    :param n_items_to_sort: Number of items, beginning from root, to sort

    Kumra, Mohit. "HeapSort". GeeksforGeeks, https://www.geeksforgeeks.org/heap-sort/. Accessed 23 April 2021.
    Original function modified to make code easier to read.
    """
    # Initialize max_val_ix as parent
    max_val_ix = parent_ix
    left_ix = 2 * parent_ix + 1
    right_ix = 2 * parent_ix + 2

    # Case when left child is greater than parent: if so, set max_val_ix equal to left child
    if (left_ix < n_items_to_sort) and (li[left_ix] > li[max_val_ix]):
        max_val_ix = left_ix

    # Case when right child > value at max_val_ix: if so, set max_val_ix equal to right child
    if (right_ix < n_items_to_sort) and (li[right_ix] > li[max_val_ix]):
        max_val_ix = right_ix

    # Swap parent for left child or right child IF the former is less than that latter
    if max_val_ix != parent_ix:
        li[parent_ix], li[max_val_ix] = li[max_val_ix], li[parent_ix]  # swap

        # Heapify at the location from which we swapped the largest item in the subtree
        heapify(li, max_val_ix, n_items_to_sort)


def heap_sort(li, n_items_to_sort=None):
    """
    Build a max heap and then sort it.

    Kumra, Mohit. "HeapSort". GeeksforGeeks, https://www.geeksforgeeks.org/heap-sort/. Accessed 23 April 2021.
    Original function modified to make code easier to read.
    """
    # Set n_items_to_sort to length of l if not specified
    if n_items_to_sort is None:
        n_items_to_sort = len(li)

    # Make sure n_items_to_sort is not greater than length of l
    elif n_items_to_sort > len(li):
        raise HeapError("n_items_to_sort {n_items_to_sort} shouldn't be greater than list length.")

    # Build a max heap
    for parent_ix in range(n_items_to_sort // 2 - 1, -1, -1):
        heapify(li, parent_ix, n_items_to_sort)

    # One by one extract elements
    for i in range(n_items_to_sort - 1, 0, -1):
        li[i], li[0] = li[0], li[i]  # swap
        heapify(li, 0, i)
