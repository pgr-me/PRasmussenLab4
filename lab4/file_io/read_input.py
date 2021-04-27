"""Peter Rasmussen, Lab 4, parsers/read_input.py

This module reads an input file and organizes its contents as integers into an OrderedList.
"""

# standard library imports
from pathlib import Path
from typing import Union


class ReadDatasetError(Exception):
    pass


def read_dataset(in_file: Union[str, Path]) -> dict:
    """
    Read integers from file input and append them to a list.
    :return: List populated with data
    """
    if not in_file.is_file():
        raise ReadDatasetError(f"Input file {in_file} does not exist.")
    with open(str(in_file), "r") as f:
        dataset = [int(x) for x in f.readlines()]
    li = []
    for integer in dataset:
        li.append(integer)

    return {in_file.stem: li}


def read_datasets(in_dir: Union[str, Path]) -> dict:
    """
    Read each dataset from a directory and each to a dictionary keyed on filename.
    :param in_dir: Directory that houses input files
    :return: Dictionary of datasets
    e.g., d = {'asc50': li_1, ..., 'dup10k': li_n}
    """
    d = {}
    for src in Path(in_dir).iterdir():
        d.update(read_dataset(src))
    return d


def read_input(in_path: Union[Path, str]) -> dict:
    """
    Read a file or directory and return a dictionary of one or more datasets.
    :param in_path: Input file or directory path
    :return: Dictionary of one or more datasets keyed on file stem
    """
    if Path(in_path).is_file():
        return read_dataset(in_path)
    elif Path(in_path).is_dir():
        return read_datasets(in_path)
    else:
        raise ReadDatasetError("File or directory does not exist.")
