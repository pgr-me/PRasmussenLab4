"""Peter Rasmussen, Lab 4, datamaker/datamaker.py

This module provides a simple Array class which the parse_evaluation_input uses to store variable-
value lists.

"""

# Standard library imports
from __future__ import annotations
import random

# Local imports
from lab4.lists.base_list import ListError, BaseList
from lab4.sorts.heap_sort import heap_sort


class OrderedList(BaseList):
    """
    List whose contents can be in-ordered, reverse-ordered, or randomly ordered.
    User can specify desired number of elements that are duplicates.
    """

    def __init__(self, max_size: int, dup_frac=0):
        """Initialize an empty list"""
        super().__init__(max_size, dup_frac)

    def randomize(self) -> OrderedList:
        """
        Randomize list contents.
        :return: Randomized list
        """

        temp_li = OrderedList(self.max_size)
        while not self.is_empty():
            ix = round(random.random() * (self.length - 1))
            item = self.delete(ix)
            temp_li.append(item)
        while not temp_li.is_empty():
            item = temp_li.delete(0)
            self.append(item)

        return self

    def reverse(self) -> OrderedList:
        """
        Reverse order of list.
        :return: Reversed list
        """
        length = self.length
        ix1 = 0
        while ix1 < length // 2:
            ix2 = length - ix1 - 1
            self[ix1], self[ix2] = self[ix2], self[ix1]
            ix1 += 1
        return self

    def sort(self) -> OrderedList:
        """
        Sort list in-order.
        :return: In-order list
        """
        heap_sort(self)
        print(type(self))
        return self
