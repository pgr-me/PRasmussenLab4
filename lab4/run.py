"""Peter Rasmussen, Lab 3, run.py

This module processes a polynomial expressions file and a corresponding variable-value evaluation
file to symbolically combine and then evaluate polynomial expressions.

"""

# standard library imports
from copy import deepcopy
from pathlib import Path
import sys
from time import time_ns

# local imports
from lab4.datamaker.make_data import make_data
from lab4.file_io.read_input import read_input
from lab4.sorts import HeapSort
from lab4.sorts import MergeSort


sys.setrecursionlimit(12000)


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
        datasets = read_input(in_path)
        if len(datasets) == 0:
            raise ValueError("No files were read.")
        output_dict = {"datasets": {}}

        # Iterate over each dataset
        for key, dataset in datasets.items():
            dataset_dict = {"unsorted_data": dataset}

            # Iterate over each sorter (e.g., 2-way merge sort, natural merge, etc.)
            for sort_name, sorter_di in sorters.items():

                # Extract dictionary arguments, instantiate sorter, and sort list
                sorter_class, kwargs = sorter_di["sort_class"], sorter_di["kwargs"]
                sorter = sorter_class(deepcopy(dataset), **kwargs)
                sorter.sort()

                # Build temp dictionary and add outputs
                dataset_dict[sort_name] = {"sorted_data": sorter.sorted_li,
                                           "n_comparisons": sorter.n_comparisons,
                                           "n_exchanges": sorter.n_exchanges,
                                           "n_partition_calls": sorter.n_partition_calls}

            # Populate the output dictionary using the dataset-level dictionary
            output_dict["datasets"][key] = dataset_dict
            output_dict["datasets"]["out_path"]

        program_stop = time_ns()
        program_elapsed = program_start - program_stop
        output_dict["program_elapsed"] = program_elapsed

        # Write outputs to CSV
        1
