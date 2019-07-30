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


class FileContextManager:
    def __init__(self, file_names: tuple, header=False): # filenames to iterate over as tuple
        self.file_names = file_names
        self.header = header
        self.file_objects = [open(file_name) for file_name in self.file_names]

    def __enter__(self):
        # enter context and return new instances of an iterator per file
        print('Returning a new iterator')
        return iter(self)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('closing files')
        for f in self.file_objects:
            f.close()
        return False

    def __iter__(self):
        return self.FilesIterator(self)

    class FilesIterator:
        def __init__(self, file_context_manager):
            self.file_context_manager = file_context_manager
            self.file_names = self.file_context_manager.file_names
            self.file_objects = file_context_manager.file_objects
            # print(self.file_names)

        def __iter__(self):
            print('Calling FileIterator instance __iter__')
            return self

        def __next__(self):
            for obj in self.file_objects:
                # f = open(file_name)
                reader = csv.reader(obj, self.sniffer_extract())
                while True:
                    try:
                        print(next(obj))
                    except StopIteration:
                        break
            # return self.csv_parser(self.sniffer_extract(), include_header=self.file_context_manager.header)

        def sniffer_extract(self):
            for file in self.file_names:
                with open(file) as f:
                    sample = f.read(2000)
                    dialect = csv.Sniffer().sniff(sample)
                return dialect

        def csv_parser(self, sniffer_dialect,  include_header=False):
            for file_name in self.file_names:
                f = open(file_name)
                reader = csv.reader(f, sniffer_dialect)
                while True:
                    try:
                        next(f)
                    except StopIteration:
                        break






# file_rows = csv_parser(fnames, sniffer_extract(fnames))
# print(list(islice(file_rows, 10)))


