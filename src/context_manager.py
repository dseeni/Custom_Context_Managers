from src.constants import *
import csv
from itertools import islice

# with a context manager
# iterator with iter method returns iterator with next /iter
# open each file
# read a few lines and csv snip
# possible also sniff/infer data type
# create a header extract
# create a named tuple based on header
# cast each row to the named tuple
# view current files in context
# if stop iteration, remove file from file que
# store named tuple for each file
# read the next row of each file
# cast data types


class FileContextManger:
    def __init__(self, file_names: tuple): # filenames to iterate over as tuple
        self.file_names = file_names

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


# file_reader = FileContextManger(fnames)

with FileContextManger(fnames) as file_reader:
    for file in file_reader.file_names:
        with open(file) as f:
            sample = f.read(2000)
            dialect = csv.Sniffer().sniff(sample)
        # print(vars(dialect))
        # print()

        with open(file) as f:
            _reader = csv.reader(f, dialect)
            for row in islice(_reader, 10):
                print(row)
            print()

def sniffer_extract(fnames):
    for file in file_reader.file_names:
        with open(file) as f:
            sample = f.read(2000)
            dialect = Sniffer().sniff(sample)
        # print(vars(dialect))
        # print()

def csv_parser(fnames, sniffer_dialect,  include_header=False):
    with open(fnames) as f:
        reader = csv.reader(f, delimiter=delimiter, quotechar=quotechar)
        if not include_header:
            next(f)
        yield from reader
