"""Peter Rasmussen, Lab 4, file_io/write_headers.py

This module provides functions that write output headers and footers.

"""

# Standard library imports
from io import TextIOWrapper
import os
from pathlib import (
    Path,
    PosixPath,
    PurePath,
    PurePosixPath,
    PureWindowsPath,
    WindowsPath,
)


# Local imports


def header_helper(paths, kind="Input"):
    """
    Build file IO identification portion of header.
    :param paths: String, Path, list of paths, or tuple of paths
    :param kind: Input or Output
    :return: File IO identification message
    """
    # Check type for kind
    if kind not in ["Input", "Output"]:
        raise ValueError(
            f"Kind must be either 'Input' or 'Output'. You provided kind={kind}"
        )

    # Build the path identification portion of header
    if type(paths) in [
        str,
        Path,
        PosixPath,
        PurePath,
        PurePosixPath,
        PureWindowsPath,
        WindowsPath,
    ]:
        file_msg = f"{kind} file: {paths.absolute()}\n"

    elif type(paths) in [list, tuple]:
        file_msg = f"{kind} files:\n"
        for path in paths:
            file_msg += f"#\t{path.absolute()}\n"

    # Raise an error if paths is of wrong type
    else:
        msg = f"{kind} must by of type str, Path, list, or tuple. You supplied {type(paths)}"
        raise TypeError(msg)

    return file_msg


def make_header(header: str, in_paths, out_paths, operation_message):
    """
    Write the header of a prefix-to-postfix conversion file.
    :param header: Single-line header string
    :param in_paths: Path to input file
    :param out_paths: Path to output file
    :param operation_message: Indicate what the program does
    """
    in_path_msg = header_helper(in_paths, "Input")
    out_path_msg = header_helper(out_paths, "Output")

    header = (
        f"# {98 * '@'}\n"
        f"# {header}\n"
        f"# {operation_message}\n"
        f"# {in_path_msg}"
        f"# {out_path_msg}"
        "\n"
    )
    return header


def write_footer(file: TextIOWrapper, footer_di: dict):
    """
    Write the footer of a prefix-to-postfix conversion file.
    :param file: File-like object to write to
    :param footer_di: Dictionary of function names & their performance metrics and associated values
    """
    footer_str = ""
    for function_name, metric_di in footer_di.items():
        footer_str += function_name + os.linesep
        for metric, value in metric_di.items():
            footer_str += f"\t{metric}: {value}" + os.linesep
    file.write(os.linesep + f"# {98 * '@'}" + os.linesep)
    file.write("Complexity outputs" + os.linesep)
    file.write(footer_str)
