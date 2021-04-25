"""Peter Rasmussen, Lab 4, datamaker/datamaker.py

This module provides a simple Array class which the parse_evaluation_input uses to store variable-
value lists.

"""

# Standard library imports
import random

# Local imports
from lab4.lists.simple_list import ListError, SimpleList


class OrderedList(SimpleList):
    """
    List whose contents can be in-ordered, reverse-ordered, or randomly ordered.
    User can specify desired number of elements that are duplicates.
    """

    def __init__(self, max_size: int, dup_frac=0):
        """Initialize an empty list"""
        super().__init__(max_size)
        if dup_frac < 0 or dup_frac > 1:
            raise ValueError("dup_frac must be between 0 and 1 inclusive.")
        self.dup_frac = dup_frac
        self.n_dups = 0

    def duplicate(self, post_sort: str = "asc_order"):
        """
        Create a list with duplicate items.
        :param: Indicate post-sort: in-order, randomly-ordered, or reverse-ordered
        :return: Duplicated list
        """
        self.assert_list_not_empty("duplicate")
        if post_sort not in ("asc_order", "ran_order", "rev_order"):
            raise ListError(f"Post-sort must be one of 'asc_order', 'ran_order', or 'rev_order'")
        list_index = 0
        dups = self.n_dups
        dup_li = OrderedList(dups)
        orig_len = self.length
        while list_index < dups:
            rand_index = round(random.random() * (orig_len - 1))
            rand_item = self[rand_index]
            dup_li.append(rand_item)
            list_index += 1

        for dup_item in dup_li:

            while True:
                rand_index = round(random.random() * (orig_len - 1))
                item = self[rand_index]
                if item not in dup_li:
                    self[rand_index] = dup_item
                    break

        if post_sort in ["asc_order", "rev_order"]:
            heap_sort(self)
            if post_sort == "rev_order":
                self.reverse()
        else:
            self.randomize()

        return self

    def randomize(self):
        """
        Randomize list contents.
        :return: Randomized list
        """

        temp_li = List(self.max_size)
        while not self.is_empty():
            ix = round(random.random() * (self.length - 1))
            item = self.delete(ix)
            temp_li.append(item)
        while not temp_li.is_empty():
            item = temp_li.delete(0)
            self.append(item)

        return self

    def reverse(self):
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
