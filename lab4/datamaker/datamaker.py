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

    def __init__(self, size: int):
        self.size = size

        # Initialize list variables
        self.asc_order_list: Union[OrderedList, None] = None
        self.rev_order_list: Union[OrderedList, None] = None
        self.ran_order_list: Union[OrderedList, None] = None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"DataMaker object: Size {self.size}"

    def make_lists(self):
        """
        Make one in-ordered, reverse-ordered, and randomly ordered list each.
        :return: None
        """
        self.asc_order_list = self.make_asc_order_list(self.size)
        self.rev_order_list = self.asc_order_list.copy()
        self.rev_order_list = self.make_rev_order_list(self.rev_order_list)
        self.ran_order_list = self.asc_order_list.copy()
        self.ran_order_list = self.make_ran_order_list(self.ran_order_list)

    @staticmethod
    def make_asc_order_list(size: int) -> OrderedList:
        """
        Make asc_order list.
        :param size: Size of list to create
        :return: Ordered list of elements from 1 to size
        """
        li = OrderedList(size)
        counter = 0
        while counter < size:
            li.append(counter + 1)
            counter += 1
        return li

    @staticmethod
    def make_ran_order_list(li: OrderedList) -> list:
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
        li.reverse()
        return li
