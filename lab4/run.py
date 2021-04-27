"""Peter Rasmussen, Lab 3, run.py

This module processes a polynomial expressions file and a corresponding variable-value evaluation
file to symbolically combine and then evaluate polynomial expressions.

"""

# standard library imports
from copy import deepcopy
from pathlib import Path
from time import time_ns

# local imports
from lab4.datamaker.make_data import make_data
from lab4.parsers.read_datasets import read
from lab4.sorts.heap_sort import HeapSort
from lab4.sorts.merge_sort import MergeSort


def run(
    in_path: Path,
    out_path: Path,
    test_out_path: Path,
    datamaker_out_path: Path,
    file_header: str
):
    """
    Symbolically combine polynomials and then evaluate for various evaluation sets.
    :param in_path: Data input path or directory
    :param out_path: Data output path or directory
    :param test_out_path: Test output path
    :param datamaker_out_path: Datamaker output directory
    """

    program_start = time_ns()

    if datamaker_out_path is not None:
        make_data(datamaker_out_path)

    else:
        sorters = {"heap_sort": {"sort_class": HeapSort, "kwargs": {}},
                   "two_way_merge": {"sort_class": MergeSort, "kwargs": {"way": 2}},
                   "three_way_merge": {"sort_class": MergeSort, "kwargs": {"way": 3}},
                   "four_way_merge": {"sort_class": MergeSort, "kwargs": {"way": 4}},
                   }
        datasets = read(in_path)
        if len(datasets) == 0:
            raise ValueError("No files were read.")
        output_dict = {}
        for key, dataset in datasets.items():
            d1 = {"unsorted_data": dataset}
            for sort_name, sorter_di in sorters.items():
                sort_class, kwargs = sorter_di["sort_class"], sorter_di["kwargs"]
                sort_obj = sort_class(deepcopy(dataset), **kwargs)
                sort_obj.sort()

                sorter = d2[](deepcopy(dataset))
                merge_sort.sort()
                di[way] = {"sorted_data": merge_sort.sorted_li,
                           "n_comparisons": merge_sort.n_comparisons,
                           "n_exchanges": merge_sort.n_exchanges,
                           "n_partition_calls": merge_sort.n_partition_calls}




            program_stop = time_ns()
            elapsed = program_start - program_stop


