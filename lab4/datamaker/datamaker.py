"""Peter Rasmussen, Lab 4, datamaker/datamaker.py

This module provides the DataMaker class, which we use to create in-order, randomly-ordered,
and reverse-ordered datasets of varying sizes. For each of these order types, the user can specify
the fraction of duplicates present in each output dataset.

"""


# Standard library imports
from typing import Union

# Local imports
from lab4.lists.ordered_list import OrderedList


class DataMaker:
    """Makes in-order (asc), reverse-ordered (rev), and randomly ordered (ran) datasets."""
    def __init__(self, size: int, dup_frac):
        """
        Initialize size and duplicate fraction parameters and list variables.
        :param size:
        :param dup_frac:
        """
        self.size = size
        self.dup_frac = dup_frac

        # Initialize list variables
        self.asc: Union[OrderedList, None] = None
        self.rev: Union[OrderedList, None] = None
        self.ran: Union[OrderedList, None] = None
        self.dup: Union[OrderedList, None] = None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"DataMaker object: Size {self.size}"

    def make_lists(self):
        """
        Make one in-ordered, reverse-ordered, and randomly ordered list each.
        :return: None
        """
        self.asc = self.make_asc_order_list(self.size)

        self.rev = self.make_asc_order_list(self.size)
        self.rev.reverse()

        self.ran = self.make_asc_order_list(self.size)
        self.ran.randomize()

        self.dup = self.make_asc_order_list(self.size, dup_frac=self.dup_frac)
        self.dup.randomize()

    @staticmethod
    def make_asc_order_list(size: int, dup_frac: float = 0) -> OrderedList:
        """
        Make asc_order list.
        :param size: Size of list to create
        :param dup_frac: Fraction of duplicate elements
        :return: Ordered list of elements from 1 to size
        """
        li = OrderedList(size, dup_frac=dup_frac)
        counter = 0
        while counter < size:
            li.append(counter + 1)
            counter += 1
        if dup_frac > 0:
            li.duplicate()
        return li

    @staticmethod
    def make_ran_order_list(li: OrderedList) -> OrderedList:
        """
        Make randomly ordered list.
        :param li: OrderedList to randomize
        :return: Randomized list
        """
        li.randomize()
        return li

    @staticmethod
    def make_rev_order_list(li: OrderedList):
        """
        Make reverse-ordered list.
        :param li: OrderedList to reverse order for
        :return: Reverse-ordered list
        """
        print(type(li))
        li.reverse()
        return li
