"""Peter Rasmussen, Lab 4, parsers/file_io.py

This module reads an input file and organizes its contents into a dictionary of lists.
"""

# standard library imports
from pathlib import Path
from typing import Union


class ReadDatasetError(Exception):
    pass


class FileIO:
    """Handles reading inputs and writing outputs."""

    def __init__(self, in_path: Path, out_path: Path):
        self.in_path = Path(in_path)
        self.out_path = Path(out_path)

    def read_datasets(self, in_dir: Union[str, Path]) -> dict:
        """
        Read each dataset from a directory and each to a dictionary keyed on filename.
        :param in_dir: Directory that houses input files
        :return: Dictionary of datasets
        e.g., d = {'asc50': li_1, ..., 'dup10k': li_n}
        """
        d = {}
        for src in Path(in_dir).iterdir():
            d.update(self.read_dataset(src))
        return d

    def read_input(self) -> dict:
        """
        Read a file or directory and return a dictionary of one or more datasets.
        :return: Dictionary of one or more datasets keyed on file stem
        """
        if self.in_path.is_file():
            return self.read_dataset(self.in_path)
        elif self.in_path.is_dir():
            return self.read_datasets(self.in_path)
        else:
            raise ReadDatasetError("File or directory does not exist.")

    def write_output(self, output_dict: dict):
        """
        Write a file or a set of files to a directory.
        :return: None
        """
        pass

    def create_out_filename(self, dataset_key: str) -> Path:
        """
        Create output filename.
        :param dataset_key: Name of dataset (e.g., ran1k)
        :return: File path
        If self.out_path is a directory, the dataset_key (e.g., asc1k) is used to create output name
        """
        if self.out_path.is_dir():
            return self.out_path / f"{dataset_key}.csv"
        return self.out_path

    @staticmethod
    def read_dataset(in_file: Union[str, Path]) -> dict:
        """
        Read integers from file input and append them to a list.
        in_file: Input file to read
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
