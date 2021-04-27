"""Peter Rasmussen, Lab 4, sorts/merge_sort.py

This module implements recursive versions of the two-way, three-way, and four-way straight merges
and the natural merge.

"""

# Standard library imports
from typing import Union


class MergeSortError(Exception):
    pass


class MergeSort:
    """
    This class recursively partitions and performs 2-way, 3-way, and 4-way merges.
    """

    def __init__(self, ways: int = 2):
        """
        Initialize list and n-ways variables.
        :param ways: Order of the merge
        """
        self.ways = ways
        if self.ways not in [2, 3, 4]:
            raise MergeSortError(
                "This implementation is only available for 2-way, 3-way, and 4-way merges")

        self.n_comparisons = 0
        self.n_exchanges = 0
        self.n_partition_calls = 0
        self.partitioned_li = []

    def merge_pass(self, l: list, ways: int = 2) -> list:
        """
        Make one merge pass of adjacent sublist pairs, triples, or quadruples.
        :param l: Partitioned list to merge
        :param ways: Two-way, three-way, or four-way merge
        :return: Partially- or fully-merged list
        """
        sorted_l = []
        while len(l) > 0:
            if len(l) == 1:
                self.n_exchanges += 1
                l1 = l.pop(0)
                sorted_l.append(l1)
            else:
                l1 = l.pop(0)
                l2 = l.pop(0)
                if (ways == 2) or (len(l) == 0):
                    self.n_exchanges += 2
                    sorted_l.append(self.two_way_merge(l1, l2))
                else:
                    l3 = l.pop(0)
                    if (ways == 3) or (len(l) == 0):
                        self.n_exchanges += 3
                        sorted_l.append(self.three_way_merge(l1, l2, l3))
                    else:
                        self.n_exchanges += 4
                        l4 = l.pop(0)
                        sorted_l.append(self.four_way_merge(l1, l2, l3, l4))

        return sorted_l

    def merge_all(self, l: list, ways: int = 2) -> list:
        """
        Recursively merge partitions to obtain a sorted list.
        :param l: Partitioned list to merge
        :param ways: Two-way, three-way, or four-way merge
        :return: Sorted, merged list
        """
        if len(l) == 1:
            return l[0]
        return self.merge_all(self.merge_pass(l, ways=ways))

    def natural_partition(self, l: list, li_partitions: Union[list, None] = None):
        """
        Recursively execute natural partitioning.
        l: List to perform natural partition on
        """
        if li_partitions is None:
            li_partitions = []
        if len(l) == 0:
            return li_partitions
        else:
            i = l.pop(0)
            # Append first item to li_partitions if li_partitions is empty
            if len(li_partitions) == 0:
                li_partitions.append([i])
            else:
                # If i >= to its predecessor, append to last sublist of li_partitions
                if i >= li_partitions[-1][-1]:
                    li_partitions[-1].append(i)
                # Otherwise, create new sublist in li_partitions and append to that
                else:
                    li_partitions.append([i])
            return self.natural_partition(l)

    def partition(self, l: list, partitioned_l: Union[list, None] = None) -> list:
        """
        Recursively partition a list.
        :param l: List to partition
        :param partitioned_l: List to add partitions to
        :return: Fully-partitioned partitioned list
        """
        if partitioned_l is None:
            partitioned_l = []
        if len(l) == 0:
            return partitioned_l

        if len(l) == 1:
            return partitioned_l + [l]
        else:
            partitioned_l.append([l.pop(0)])
            self.n_partition_calls += 1
            return self.partition(l, partitioned_l)

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
