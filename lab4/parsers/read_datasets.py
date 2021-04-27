"""Peter Rasmussen, Lab 4, parsers/read_dataset.py

This module reads an input file and organizes its contents as integers into an OrderedList.
"""

# standard library imports
from pathlib import Path
from typing import Union

# local imports
from lab4.lists.ordered_list import OrderedList
from lab4.misc.symbols import Symbols


def read_dataset(in_file: Union[str, Path]) -> OrderedList:
    """
    Read integers from file input and append them to a list.
    :return: List populated with data
    """
    with open(str(in_file), "r") as f:
        dataset = [int(x) for x in f.readlines()]
    li = OrderedList(max_size=len(dataset))

    return li


def read_datasets(src_dir: Union[str, Path]) -> dict:
    """
    Read each dataset from a directory and each to a dictionary keyed on filename.
    :param src_dir: Directory that houses input files
    :return: Dictionary of datasets
    e.g., d = {'asc50': li_1, ..., 'dup10k': li_n}
    """
    d = {}
    for src in Path(src_dir).iterdir():
        d[src.stem] = read_dataset(src)

    return d
