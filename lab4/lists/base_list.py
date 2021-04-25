"""Peter Rasmussen, Lab 3, lists/array.py

This module provides a simple Array class which the parse_evaluation_input uses to store variable-
value lists.

"""


# Standard library imports
import random
from typing import Union


class ListError(Exception):
    """Error class for List classes."""
    pass


class BaseList:
    """Array-based list implementation."""

    def __init__(self, max_size: int, dup_frac=0):
        """Initialize an empty list"""
        self.max_size = max_size
        if dup_frac < 0 or dup_frac > 1:
            raise ValueError("dup_frac must be between 0 and 1 inclusive.")
        self.dup_frac = dup_frac
        self.n_dups = 0
        self.array: list = max_size * [None]
        self.length = 0
        self.max_index: Union[int, None] = None

    def __iter__(self):
        index = 0
        while index < self.length:
            yield self.array[index]
            index += 1

    def __getitem__(self, index):
        return self.get(index)

    def __len__(self):
        return self.length

    def __str__(self):
        if self.is_empty():
            return "[]"
        str_output = "["
        for i in self:
            str_output += (str(i) + ', ')
        str_output = str_output[:-2] + "]"
        return str_output

    def __repr__(self):
        return self.__str__()

    def __setitem__(self, index, item):
        self.replace(index, item)

    def append(self, item):
        """
        Append an item to the list.
        :param item: Data element to add
        :return: None
        """
        self.assert_list_not_full()
        if self.is_empty():
            self.max_index = 0
        else:
            self.max_index += 1
        self.array[self.max_index] = item
        self.length += 1
        self.n_dups = round(self.length * self.dup_frac)

    def assert_index_in_range(self, index):
        if index == 0 and self.is_empty():
            return
        if index > self.max_index:
            raise IndexError("List index out of range.")

    def assert_list_not_full(self):
        if self.is_full():
            raise ListError("List overflow.")

    def assert_list_not_empty(self, function_name):
        if self.is_empty():
            raise ListError(f"Cannot {function_name} from an empty list.")

    def copy(self):
        """
        Make a deep copy of the list.
        :return: Deep copy of list
        """
        li = BaseList(self.max_size)
        for item in self:
            li.append(item)
        return li

    def delete(self, index):
        """
        Delete item at index.
        :param index: Index at which to delete item.
        :return: Deleted item
        """
        self.assert_list_not_empty("delete")
        self.assert_index_in_range(index)
        self.assert_index_nonnegative(index)
        item = self[index]
        if index < self.max_index:
            shift_index = index
            length = len(self)
            while True:
                self[shift_index] = self[shift_index + 1]
                shift_index += 1
                if shift_index == length - 1:
                    break

        self.array[self.max_index] = None
        self.length -= 1
        if self.is_empty():
            self.max_index = None
            self.n_dups = 0
        else:
            self.max_index -= 1
            self.n_dups = round(self.length * self.dup_frac)

        return item

    def duplicate(self):
        """
        Create a list with duplicate items.
        :param: Indicate post-sort: in-order, randomly-ordered, or reverse-ordered
        :return: Duplicated list
        """
        self.assert_list_not_empty("duplicate")

        list_index = 0
        dups = self.n_dups
        dup_li = BaseList(dups)
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

        return self

    def get(self, index):
        """
        Get item at given list index.
        :param index: List index from which to retrieve item
        :return: Item at index
        """
        self.assert_list_not_empty("get")
        self.assert_index_nonnegative(index)
        self.assert_index_in_range(index)

        return self.array[index]

    def insert(self, index: int, item):
        """
        Insert item at index and move subsequent items one place over.
        :param index: Index at which to insert item
        :param item: Insertion item
        """
        self.assert_list_not_full()
        if self.is_empty() and index > 0:
            raise IndexError("List index out of range.")

        if self.is_empty() or (index == self.max_index) or (index == -1):
            self.append(item)
        else:
            shift_index = len(self)
            self.append(None)
            while shift_index > index:
                self[shift_index] = self[shift_index - 1]
                shift_index -= 1
            self[index] = item

    def is_empty(self):
        """
        Check if list is empty.
        :return: True if list is empty
        """
        return self.length == 0

    def is_full(self):
        return self.length == self.max_size

    def pop(self):
        """
        Remove item at end of list.
        :return: Popped item
        """
        self.assert_list_not_empty("get")

        item = self.array[self.max_index]
        self.array[self.max_index] = None
        self.length -= 1
        if self.is_empty():
            self.max_index = None
            self.n_dups = 0
        else:
            self.max_index -= 1
            self.n_dups = round(self.length * self.dup_frac)
        return item

    def replace(self, index: int, item: Union[int, str]):
        """
        Replace one item for another.
        :param index: Index at which to replace
        :param item: Replacement item
        :return: None
        """
        self.assert_index_in_range(index)
        self.assert_index_nonnegative(index)
        if self.is_empty():
            self.append(item)

        self.array[index] = item

    @staticmethod
    def assert_index_integer(index: int):
        """
        Raise error if index is not an integer.
        :param index: Index to check
        :return: None
        """
        if type(index) != int:
            raise ListError("Indexes must be integers.")

    @staticmethod
    def assert_index_nonnegative(index: int):
        """
        Raise error if index is not non-negative.
        :param index: Index to check
        :return: None
        """
        if index < 0:
            raise ListError("Negative indexing is not supported in this implementation.")
