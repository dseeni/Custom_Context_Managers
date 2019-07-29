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




def sniffer_extract(file_names):
    for file in file_names:
        with open(file) as f:
            sample = f.read(2000)
            dialect = csv.Sniffer().sniff(sample)
        return dialect
        # print(vars(dialect))
        # print()


def csv_parser(file_names, sniffer_dialect,  include_header=False):
    for file_name in file_names:
        with open(file_name) as f:
            reader = csv.reader(f, sniffer_dialect)
            if not include_header:
                next(f)
            yield from reader


file_rows = csv_parser(fnames, sniffer_extract(fnames))
print(list(islice(file_rows, 10)))


