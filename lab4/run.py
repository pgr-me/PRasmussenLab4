"""Peter Rasmussen, Lab 3, run.py

This module processes a polynomial expressions file and a corresponding variable-value evaluation
file to symbolically combine and then evaluate polynomial expressions.

"""

# standard library imports
import csv
from copy import deepcopy
from pathlib import Path
from time import time_ns

# local imports
from lab4.datamaker.make_data import make_data
from lab4.file_io import FileIO, make_header
from lab4.sorts import HeapSort
from lab4.sorts import MergeSort


def run(
        in_path: Path,
        out_path: Path,
        datamaker_out_path: Path,
        file_header: str
):
    """
    Symbolically combine polynomials and then evaluate for various evaluation sets.
    :param in_path: Data input path or directory
    :param out_path: Data output CSV path or directory where CSVs will be saved
    :param datamaker_out_path: Datamaker output directory
    :param file_header: Header to add to top of CSV
    """

    program_start = time_ns()

    if datamaker_out_path is not None:
        make_data(datamaker_out_path)

    else:
        sorters = {"heap_sort": {"sort_class": HeapSort, "kwargs": {}},
                   "two_way_merge": {"sort_class": MergeSort, "kwargs": {"way": 2}},
                   "three_way_merge": {"sort_class": MergeSort, "kwargs": {"way": 3}},
                   "four_way_merge": {"sort_class": MergeSort, "kwargs": {"way": 4}},
                   "natural_merge": {"sort_class": MergeSort, "kwargs": {"way": "natural"}},
                   }

        file_io = FileIO(in_path, out_path)
        datasets = file_io.read_input()
        if len(datasets) == 0:
            raise ValueError("No files were read.")

        # Iterate over each dataset
        for dataset_name, dataset in datasets.items():
            print(f"Dataset: {dataset_name}")
            data_dict = {"unsorted": dataset}

            # Iterate over each sorter (e.g., 2-way merge sort, natural merge, etc.)
            for sort_name, sorter_di in sorters.items():
                print(f"\tSort: {sort_name}")
                # Extract dictionary arguments, instantiate sorter, and sort list
                sorter_class, kwargs = sorter_di["sort_class"], sorter_di["kwargs"]
                sorter = sorter_class(deepcopy(dataset), **kwargs)
                sorter.sort()

                # Build temp dictionary and add outputs
                data_dict[sort_name] = {"sorted": sorter.sorted_li,
                                        "n": sorter.n,
                                        "n_comparisons": sorter.n_comparisons,
                                        "n_exchanges": sorter.n_exchanges,
                                        "n_partition_calls": sorter.n_partition_calls,
                                        "elapsed_ns": sorter.elapsed}

            # Make destination filepath
            dst = file_io.create_out_filename(dataset_name)

            # Make file headers
            operation_message = "Unsorted and sorted lists and sorted list performance metrics."
            in_file = in_path / f"{dst.stem}.dat"
            file_header_ = make_header(file_header, in_file, dst, operation_message)

            # Make column names
            column_names: list = list(data_dict.keys())

            # Create metrics table
            csv_li: list = [["metric"] + column_names]

            # Metrics table: Add number of comparisons, exchanges, and partition calls
            for metric in ["n", "n_comparisons", "n_exchanges", "n_partition_calls", "elapsed_ns"]:
                li = [di[metric] for k, di in data_dict.items() if k != "unsorted"]
                if metric == "n":
                    metric_li = [metric, len(dataset)] + li
                else:
                    metric_li = [metric, "N/A"] + li
                csv_li.append(metric_li)

            csv_li.append([""] + len(column_names) * [""])  # blank line to separate tables

            # Create data table
            csv_li.append(["ix"] + column_names)
            for ix, value in enumerate(data_dict["unsorted"]):
                li = [ix, value] + [sort_dict["sorted"][ix] for sort_name, sort_dict in
                                    data_dict.items() if sort_name != "unsorted"]
                csv_li.append(li)

            # Write outputs to CSV
            with open(str(dst), "w") as f:
                f.write(file_header_)
                writer = csv.writer(f)
                writer.writerows(csv_li)
