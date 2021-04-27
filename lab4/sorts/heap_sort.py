"""Peter Rasmussen, Lab 4, sorts/heap_sort.py

This module implements a recursive version of the heapify and heap sort methods.

The heapify and sort methods are adapted from the implementation cited below.
Kumra, Mohit. "HeapSort". GeeksforGeeks, https://www.geeksforgeeks.org/heap-sort/.
Accessed 23 April 2021.

"""

# Standard library imports
from copy import deepcopy
from time import time_ns
from typing import Union


class HeapSortError(Exception):
    pass


class HeapSort:
    """Recursive implementation of the heapify and heap sort methods."""

    def __init__(self, unsorted_li: list, n_items_to_sort: Union[int, None] = None):
        """
        Initialize list and other variables.
        :param unsorted_li: List to be sorted

        The heapify and sort methods are adapted from the implementation cited below.
        Kumra, Mohit. "HeapSort". GeeksforGeeks, https://www.geeksforgeeks.org/heap-sort/.
        Accessed 23 April 2021.
        Original function, referenced above, was modified so that it could be used as a method in
        this class.
        """
        self.unsorted_li = unsorted_li
        # Set n_items_to_sort to length of temp_li if not specified
        if n_items_to_sort is None:
            self.n_items_to_sort = len(unsorted_li)
        self.n_comparisons = 0
        self.n_exchanges = 0
        self.n_partition_calls = 0
        self.start: int = time_ns()
        self.stop: Union[int, None] = None
        self.elapsed: Union[int, None] = None
        self.sorted_li: Union[list, None] = None

    def heapify(self, li: list, parent_ix: int, n_items_to_sort: Union[int, None]):
        """
        Heapify an temp_li.
        :param li: Array to heapify
        :param parent_ix: Parent (i.e., root) index of subtree
        :param n_items_to_sort: Number of items, beginning from root, to sort

        Kumra, Mohit. "HeapSort". GeeksforGeeks, https://www.geeksforgeeks.org/heap-sort/.
        Accessed 23 April 2021.
        Original function, referenced above, was modified so that it could be used as a method in
        this class.
        """
        # Initialize max_val_ix as parent
        max_val_ix = parent_ix
        left_ix = 2 * parent_ix + 1
        right_ix = 2 * parent_ix + 2

        # Case when left child is greater than parent: if so, set max_val_ix equal to left child
        if (left_ix < n_items_to_sort) and (li[left_ix] > li[max_val_ix]):
            self.n_comparisons += 2
            max_val_ix = left_ix

        # Case when right child > value at max_val_ix: if so, set max_val_ix equal to right child
        if (right_ix < n_items_to_sort) and (li[right_ix] > li[max_val_ix]):
            self.n_comparisons += 2
            max_val_ix = right_ix

        # Swap parent for left child or right child IF the former is less than that latter
        if max_val_ix != parent_ix:
            self.n_exchanges += 1
            self.n_comparisons += 1
            li[parent_ix], li[max_val_ix] = li[max_val_ix], li[parent_ix]  # swap

            # Heapify at the location from which we swapped the largest item in the subtree
            self.heapify(li, max_val_ix, n_items_to_sort)

    def sort(self) -> list:
        """
        Build a max heap and then sort it.
        :return: Sorted list

        Kumra, Mohit. "HeapSort". GeeksforGeeks, https://www.geeksforgeeks.org/heap-sort/.
        Accessed 23 April 2021.
        Original function, referenced above, was modified to make the code easier to read.
        """
        temp_li = deepcopy(self.unsorted_li)

        # Make sure n_items_to_sort is not greater than length of temp_li
        if self.n_items_to_sort > len(temp_li):
            raise HeapSortError(
                "n_items_to_sort {n_items_to_sort} shouldn't be greater than list length.")

        # Build a max heap
        for parent_ix in range(self.n_items_to_sort // 2 - 1, -1, -1):
            self.heapify(temp_li, parent_ix, self.n_items_to_sort)

        # One by one extract elements
        for i in range(self.n_items_to_sort - 1, 0, -1):
            self.n_exchanges += 1
            temp_li[i], temp_li[0] = temp_li[0], temp_li[i]  # swap
            self.heapify(temp_li, 0, i)

        # Stop the timer and compute total runtime
        self.stop_timer()

        self.sorted_li = temp_li

        return self.sorted_li

    def stop_timer(self):
        """
        Stop timer and compute elapsed time
        :return: None
        """
        self.stop = time_ns()
        self.elapsed = self.stop - self.start
