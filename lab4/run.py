"""Peter Rasmussen, Lab 3, run.py

This module processes a polynomial expressions file and a corresponding variable-value evaluation
file to symbolically combine and then evaluate polynomial expressions.

"""

# standard library imports
from pathlib import Path
from time import time_ns

# local imports
from lab4.datamaker.make_data import make_data
from lab4.parsers.read_datasets import read


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

    run_start = time_ns()

    if test_out_path is not None:
        pass

    if datamaker_out_path is not None:
        make_data(datamaker_out_path)

    else:
        datasets = read(in_path)
        if len(datasets) == 0:
            raise ValueError("No files were read.")
        for key, dataset in datasets.items():
            start = time_ns()

            stop = time_ns()
            elapsed = start - stop


            1
