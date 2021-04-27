"""Peter Rasmussen, Lab 4, sorts/merge_sort.py

This module implements recursive versions of the two-way, three-way, and four-way straight merges
and the natural merge.

"""

# Standard library imports
from copy import deepcopy
from typing import Union
from time import time_ns


class MergeSortError(Exception):
    pass


class MergeSort:
    """
    This class recursively partitions and performs 2-way, 3-way, and 4-way merges.
    """

    def __init__(self, unsorted_li: list, way: Union[int, str] = 2):
        """
        Initialize list and n-way / natural merge variables.
        :param way: Order if straight merge or specification of natural merge
        """
        self.unsorted_li = unsorted_li
        self.way = way
        if self.way not in ["natural", 2, 3, 4]:
            raise MergeSortError(
                "This implementation only available for natural, 2-way, 3-way, and 4-way merges")

        self.n_comparisons = 0
        self.n_exchanges = 0
        self.n_partition_calls = 0
        self.start: int = time_ns()
        self.stop: Union[int, None] = None
        self.elapsed: Union[int, None] = None
        self.partitioned_li: Union[list, None] = None
        self.sorted_li: Union[list, None] = None

    def sort(self):
        """
        Sort the list using either 2-way, 3-way, 4-way straight merge or natural merge.
        :return: Sorted list
        """
        if self.way == "natural":
            self.partitioned_li = self.natural_partition(deepcopy(self.unsorted_li))
        else:
            self.partitioned_li = self.partition(deepcopy(self.unsorted_li))
        self.sorted_li = self.merge_all(deepcopy(self.partitioned_li))


    def merge_all(self, li: list) -> list:
        """
        Recursively merge partitions to obtain a sorted list.
        :param li: Partitioned list to merge
        :return: Sorted, merged list
        """
        if len(li) == 1:
            return li[0]
        return self.merge_all(self.merge_pass(li))

    def merge_pass(self, li: list) -> list:
        """
        Make one merge pass of adjacent sublist pairs, triples, or quadruples.
        :param li: Partitioned list to merge
        :return: Partially- or fully-merged list
        """
        sorted_li = []
        while len(li) > 0:
            if len(li) == 1:
                self.n_exchanges += 1
                l1 = li.pop(0)
                sorted_li.append(l1)
            else:
                l1 = li.pop(0)
                l2 = li.pop(0)
                if (self.way in [2, "natural"]) or (len(li) == 0):
                    self.n_exchanges += 2
                    sorted_li.append(self.two_way_merge(l1, l2))
                else:
                    l3 = li.pop(0)
                    if (self.way == 3) or (len(li) == 0):
                        self.n_exchanges += 3
                        sorted_li.append(self.three_way_merge(l1, l2, l3))
                    else:
                        self.n_exchanges += 4
                        l4 = li.pop(0)
                        sorted_li.append(self.four_way_merge(l1, l2, l3, l4))

        return sorted_li

    def natural_partition(self, unsorted_li: list, partitioned_li: Union[list, None] = None):
        """
        Recursively execute natural partitioning.
        unsorted_li: List to perform natural partition on
        """
        if partitioned_li is None:
            partitioned_li = []
        if len(unsorted_li) == 0:
            return partitioned_li
        else:
            i = unsorted_li.pop(0)
            # Append first item to partitioned_li if partitioned_li is empty
            if len(partitioned_li) == 0:
                partitioned_li.append([i])
            else:
                # If i >= to its predecessor, append to last sublist of partitioned_li
                if i >= partitioned_li[-1][-1]:
                    self.n_comparisons += 1
                    partitioned_li[-1].append(i)
                # Otherwise, create new sublist in partitioned_li and append to that
                else:
                    partitioned_li.append([i])
            self.n_partition_calls += 1
            return self.natural_partition(unsorted_li)

    def partition(self, unsorted_li, partitioned_li: Union[list, None] = None) -> list:
        """
        Recursively partition a list.
        :param unsorted_li: List to be partitioned
        :param partitioned_li: List to add partitions to
        :return: Fully-partitioned list
        """
        if partitioned_li is None:
            partitioned_li = []
        if len(unsorted_li) == 0:
            return partitioned_li

        if len(unsorted_li) == 1:
            return partitioned_li + [unsorted_li]
        else:
            partitioned_li.append([unsorted_li.pop(0)])
            self.n_partition_calls += 1
            return self.partition(unsorted_li, partitioned_li)

    def four_way_merge(self, l1: list, l2: list, l3: list, l4: list) -> list:
        """
        Merge four sorted lists into one sorted list.
        :param l1: First list
        :param l2: Second list
        :param l3: Third list
        :param l4: Fourth list
        :return: Merged, sorted list
        """
        li_merge = []
        while l1 and l2 and l3 and l4:
            i1, i2, i3, i4 = l1[0], l2[0], l3[0], l4[0]
            # Cases when one of the elements is the smallest
            if (i1 < i2) and (i1 < i3) and (i1 < i4):
                self.n_comparisons += 3
                li_merge.append(l1.pop(0))
            elif (i2 < i1) and (i2 < i3) and (i2 < i4):
                self.n_exchanges += 1
                self.n_comparisons += 6
                li_merge.append(l2.pop(0))
            elif (i3 < i1) and (i3 < i2) and (i3 < i4):
                self.n_exchanges += 1
                self.n_comparisons += 9
                li_merge.append(l3.pop(0))
            elif (i4 < i1) and (i4 < i2) and (i4 < i3):
                self.n_exchanges += 1
                self.n_comparisons += 12
                li_merge.append(l4.pop(0))
            # Case when all four elements are the smallest (i.e., equal)
            elif i1 == i2 == i3 == i4:
                self.n_comparisons += 15
                li_merge.append(l1.pop(0))
            # Cases when three elements are the smallest
            elif i1 == i2 == i3:
                self.n_comparisons += 17
                li_merge.append(l1.pop(0))
            elif i1 == i2 == i4:
                self.n_comparisons += 19
                li_merge.append(l1.pop(0))
            elif i1 == i3 == i4:
                self.n_comparisons += 21
                li_merge.append(l1.pop(0))
            elif i2 == i3 == i4:
                self.n_exchanges += 1
                self.n_comparisons += 23
                li_merge.append(l2.pop(0))
            # Cases when two elements are the smallest
            elif (i1 == i2) and (i1 < i3):
                self.n_comparisons += 25
                li_merge.append(l1.pop(0))
            elif (i1 == i3) and (i1 < i4):
                self.n_comparisons += 27
                li_merge.append(l1.pop(0))
            elif (i1 == i4) and (i1 < i2):
                self.n_comparisons += 29
                li_merge.append(l1.pop(0))
            elif i2 == i3:
                self.n_exchanges += 1
                self.n_comparisons += 30
                li_merge.append(l2.pop(0))
            elif i2 == i4:
                self.n_exchanges += 1
                self.n_comparisons += 31
                li_merge.append(l2.pop(0))
            else:  # i3 == i4
                self.n_exchanges += 1
                self.n_comparisons += 31
                li_merge.append(l3.pop(0))

        # Now we only have three lists left
        if not l1:
            return li_merge + self.three_way_merge(l2, l3, l4)
        elif not l2:
            return li_merge + self.three_way_merge(l1, l3, l4)
        elif not l3:
            return li_merge + self.three_way_merge(l1, l2, l4)
        else:  # not l4
            return li_merge + self.three_way_merge(l1, l2, l3)

    def three_way_merge(self, l1: list, l2: list, l3: list):
        """
        Merge three sorted lists into one sorted list.
        :param l1: First list
        :param l2: Second list
        :param l3: Third list
        :return: Merged, sorted list
        """
        li_merge = []
        while l1 and l2 and l3:
            i1, i2, i3 = l1[0], l2[0], l3[0]
            # Cases when one of the elements is the smallest
            if (i1 < i2) and (i1 < i3):
                self.n_comparisons += 2
                li_merge.append(l1.pop(0))
            elif (i2 < i1) and (i2 < i3):
                self.n_exchanges += 1
                self.n_comparisons += 4
                li_merge.append(l2.pop(0))
            elif (i3 < i1) and (i3 < i2):
                self.n_exchanges += 1
                self.n_comparisons += 6
                li_merge.append(l3.pop(0))
            # Case when all three elements are the smallest (i.e., equal)
            elif i1 == i2 == i3:
                self.n_comparisons += 8
                li_merge.append(l1.pop(0))
            # Cases when two of the elements are the smallest
            elif i1 == i2:
                self.n_comparisons += 9
                li_merge.append(l1.pop(0))
            elif i1 == i3:
                self.n_comparisons += 10
                li_merge.append(l1.pop(0))
            else:  # i2 == i3
                self.n_exchanges += 1
                self.n_comparisons += 11
                li_merge.append(l2.pop(0))

        # Now we only have two lists left
        if not l1:
            return li_merge + self.two_way_merge(l2, l3)
        elif not l2:
            return li_merge + self.two_way_merge(l1, l3)
        else:  # not l3
            return li_merge + self.two_way_merge(l1, l2)

    def two_way_merge(self, l1: list, l2: list):
        """
        Merge two sorted lists into one sorted list.
        :param l1: First list
        :param l2: Second list
        :return: Merged, sorted list
        """
        li_merge = []
        while l1 and l2:
            if l1[0] < l2[0]:
                li_merge.append(l1.pop(0))
            else:
                self.n_exchanges += 1
                li_merge.append(l2.pop(0))
            self.n_comparisons += 1

        return li_merge + l1 + l2

    def stop_timer(self):
        """
        Stop timer and compute elapsed time
        :return: None
        """
        self.stop = time_ns()
        self.elapsed = self.stop - self.start
