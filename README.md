# Peter Rasmussen, Lab 4

This Python package sorts one or more data files using straight merge and heap sort approaches and 
writes outputs to CSV.

## Getting Started

The package is designed to be executed as a module from the command line. The user must specify the
input and output file paths, either as a pair of file paths or directory paths, as illustrated
below.

To process one file, specify the input and output file paths.
```shell
python -m path/to/lab4 -i path/to/in_file.dat -o path/to/eval_infile.txt 
```

To process a directory of data files, specify the input and output directory paths.
```shell
python -m path/to/lab4 -i path/to/input_dir -o path/to/output_dir
```

Optionally, the user may specify a file header that is prepended to the outputs. The example below
illustrates usage of the optional argument.

```shell
python -m path/to/lab4 -i path/to/in_file.dat -o path/to/out_file.csv -f "Your Header"
```

A summary of the command line arguments are below.

Positional arguments:

    -i, --in_path       Input File or Directory Pathname
    -o, --out_path      Output File or Directory Pathname

Optional arguments:

    -h, --help          Show this help message and exit
    -f, --file_header   Input custom file header above output file

## Features

* Four-way merge complements two-way and three-way merge sorts and heap sort
* CSV outputs organized such that, for each input dataset, performance metrics are tabulated at the
  top of the CSV and beneath that is a side-by-side comparison of the echoed input and the sorted
  outputs.
* Tested on file sizes of 10,000 integers.
* Option to process one file at a time or in bulk.
* Recursive implementation of each sort algorithm to enable apples-to-apples performance
  comparisons.

## Input and Output Files

The ```resources/inputs``` directory contains the set of input files. Pre-processed outputs are in
the ```resources/outputs``` directory.

## Example Output File

An example of the output is shown below.

| metric  | unsorted  | two_way_merge  | three_way_merge  | four_way_merge  | heap_sort  |
|---|---|---|---|---|---|
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   |   |

Outputs are organized by operation (e.g., A+B). For each operation, the input polynomial expression

is echoed and the output expression (e.g., result of A+B) is one line below. A simple table
summarizes the evaluated answer alongside the evaluation set (e.g., x1y2z3). Below the polynomial
expression operation and evaluation outputs is total runtime.

Example output file:

    # Peter Rasmussen, Lab 3
    # Polynomial simplification and evaluation
    # Input files:
    #	/Users/peter/PycharmProjects/PRasmussenLab3/resources/additional_polynomial_input_04.txt
    #	/Users/peter/PycharmProjects/PRasmussenLab3/resources/additional_evaluation_input_02.txt
    # Output file: /Users/peter/PycharmProjects/PRasmussenLab3/resources/additional_output_04_02.txt

    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    Polynomial input expression definitions
    A = 31a3b4c3d4e1+11a4b1c0d0e0-1a4b1c3d3e3-13a2b3c2d4e0+24a1b3c4d4e3
    B = 7a1b4c2d3e1-29a1b2c3d0e2-25a3b2c0d4e3+6a4b2c0d1e2-1a1b0c2d0e3
    C = a2b1c3d1e1-10a2b1c0d3e4+23a4b2c2d3e2+16a0b2c2d3e2-5a2b1c1d1e2
    D = 4a3b1c0d1e2+24a4b4c2d0e2+28a2b3c2d1e0+18a1b3c0d2e1-16a1b4c4d0e2
    A+B
    Input:	(31a3b4c3d4e1+11a4b1c0d0e0-1a4b1c3d3e3-13a2b3c2d4e0+24a1b3c4d4e3)+(7a1b4c2d3e1-29a1b2c3d0e2-25a3b2c0d4e3+6a4b2c0d1e2-1a1b0c2d0e3)
    Output:	31a3b4c3d4e1+11a4b1c0d0e0-1a4b1c3d3e3-13a2b3c2d4e0+24a1b3c4d4e3+7a1b4c2d3e1-29a1b2c3d0e2-25a3b2c0d4e3+6a4b2c0d1e2-1a1b0c2d0e3
    Evaluation Set			Answer
    a0b4c1d5e4				0
    a2b3c5d0e1				-64772

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # Peter Rasmussen, Lab 3
    # Input file: /Users/peter/PycharmProjects/PRasmussenlab3/resources/additional_input.txt
    # Output file: /Users/peter/PycharmProjects/PRasmussenlab3/resources/additional_output.txt

## Licensing

This project is licensed under the MIT license.
