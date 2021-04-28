# Peter Rasmussen, Lab 4

This Python package sorts one or more data files using recursive implementations of straight merge,
natural merge, and heap sort algorithms and writes outputs to CSV.

## Getting Started

The package is designed to be executed as a module from the command line. The user must specify the
input and output file paths, either as a pair of file paths or directory paths, as illustrated
below.

To process one file, specify the input and output file paths.
```shell
python -m path/to/lab4 -i path/to/in_file.dat -o path/to/out_file.csv 
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
* Using the 25 input files and five sorts, the user can execute 125 runs in one go.

## Input and Output Files

The ```resources/inputs``` directory contains the set of input files. Pre-processed outputs are in
the ```resources/outputs``` directory.

## Pre-sorts
This program has been tested using in-order, reverse-ordered, and randomly-ordered lists. List 
"pre-sorts" are available in the ```resources/inputs``` directory. For each pre-sort, there are
pre-tested file sizes of 50, 500, 1,000, 5,000, and 10,000 integers. The randomly-ordered set of
lists includes one set without duplicates and one with 20% duplicates. The other pre-sorts -
in-order and reverse-ordered - have zero duplicates.

We use the following file prefixes to identify the list presort:
* In-order: asc
* Reverse-ordered: rev
* Randomly-ordered: ran
* Randomly-ordered (20% duplicates): dup

## Example Output File

An example of the metrics portion of the output for asc5.csv is shown below.

**metric**|**unsorted**|**heap\_sort**|**two\_way\_merge**|**three\_way\_merge**|**four\_way\_merge**|**natural\_merge**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
n|2000|2000|2000|2000|2000|2000
n\_comparisons|N/A|64277|10864|31060|47704|10864
n\_exchanges|N/A|18708|14864|12162|11107|14864
n\_partition\_calls|N/A|0|1999|1999|1999|2000
elapsed\_ns|N/A|50141000|36241000|31427000|27518000|36522000


Beneath the metrics table is the side-by-side unsorted and sorted lists (2000-item reverse order
list and corresponding sorts shown).

**ix**|**unsorted**|**heap\_sort**|**two\_way\_merge**|**three\_way\_merge**|**four\_way\_merge**|**natural\_merge**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
0|2000|1|1|1|1|1
1|1999|2|2|2|2|2
2|1998|3|3|3|3|3
3|1997|4|4|4|4|4
4|1996|5|5|5|5|5

## Sources

The heapify and sort methods are adapted from the following source.
    
    Kumra, Mohit. "HeapSort". GeeksforGeeks, https://www.geeksforgeeks.org/heap-sort/.
    Accessed 23 April 2021.

A memoization routine, which ultimately was not included in the final version of the program, was obtained from the following source.

    Class obtained from source cited below.
    “Python - anyone have a memoizing decorator that can handle unhashable arguments?" Stack Overflow, 26 April 2021,
    https://stackoverflow.com/questions/4669391/python-anyone-have-a-memoizing-decorator-that-can-handle-unhashable-arguments

## Licensing

This project is licensed under the MIT license.
