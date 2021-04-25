"""Peter Rasmussen, Lab 4, datamaker/make_data.py

This module provides the DataMaker class, which we use to create in-order, randomly-ordered,
and reverse-ordered datasets of varying sizes. For each of these order types, the user can specify
the fraction of duplicates present in each output dataset.

"""


# Standard library imports
from pathlib import Path

# Local imports
from lab4.datamaker.datamaker import DataMaker
from lab4.misc.utils import reformat_big_integer


def make_data(dst_dir: Path):
    list_types = ["asc", "rev", "ran", "dup"]

    # Iterate over each list size
    for size in [50, 500, 1000, 2000, 5000, 10000]:
        datamaker = DataMaker(size, dup_frac=0.2)
        datamaker.make_lists()

        # Iterate over list
        for list_type in list_types:

            # Build output filename
            filename = f"{list_type}{reformat_big_integer(size)}.dat"
            dst = dst_dir / filename

            with open(str(dst), "w") as f:

                # Iterate over each number in list
                for integer in datamaker.__getattribute__(list_type):
                    f.write(str(integer) + "\n")
