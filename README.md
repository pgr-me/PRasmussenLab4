# Peter Rasmussen, Lab 3

This Python package adds, subtracts, and multiplies polynomial expressions. 

## Getting Started

The package is designed to be executed as a module from the command line. The user must specify the
input and output file paths, as illustrated below.

```shell
python -m path/to/lab3 -p path/to/poly_infile.txt -e path/to/eval_infile.txt -o path/to/outfile.txt
```

Optionally, the user may specify True for the --test flag to run the tests module. Additionally, the
user may specify a file header that is prepended to the outputs. The example below illustrates usage
of the optional arguments. Finally, the user may add additional operators (e.g., %) if desired.

```shell
python -m path/to/lab3 -p path/to/poly_infile.txt -e path/to/eval_infile.txt -o path/to/outfile.txt -t True -f "Your Header"
```

A summary of the command line arguments are below.

Positional arguments:

    -e, --evaluation_in_file    Evaluation Input File Pathname
    -p, --polynomial_in_file    Polynomial Input File Pathname
    -o, --out_file              Output File Pathname

Optional arguments:

    -h, --help                  Show this help message and exit
    -f, --file_header           Input custom file header above output file
    -t, --test                  Indicate True to run tests

## Features

* Uses circular-linked list data structure whose nodes are themselves lists of polynomial terms
* Supports up to 26 variables (a, b, ... z) 
* Error handling for invalid symbols, type errors, and value errors
* Options to run tests & write custom output file header
* Runtime statistic appended to end of output file

## Input and Output Files

The ```resources/``` directory contains a set of input files and outputs generated by running the
module using the default optional arguments. Required inputs and outputs are included in this directory.

## Example Output File

An example of the output is shown below.

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
