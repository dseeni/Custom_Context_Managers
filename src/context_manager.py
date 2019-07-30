from src.constants import *
import csv
from itertools import islice
from collections import namedtuple

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
    def __init__(self, file_name, parser, class_name):
        self.file_name = file_name
        self.file_obj = None
        self.reader = None
        self.parser = parser
        self.class_name = class_name

    def __enter__(self):
        self.file_obj = open(self.file_name)
        self.reader = csv.reader(self.file_obj, self.sniffer_extract(self.file_obj))
        headers = map(lambda l: l.lower(), next(self.reader))
        self._nt = namedtuple(self.class_name, headers)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()
        return False

    def __iter__(self):
        return self

    def __next__(self):
        if self.file_obj.closed:
            print('end of file reached')
            raise StopIteration
        else:
            data = next(self.reader)
            zipped = (fn(value) for value, fn in zip(data, self.parser))
            return self._nt(*zipped)

    @staticmethod
    def sniffer_extract(file_obj):
        sample = file_obj.read(2000)
        dialect = csv.Sniffer().sniff(sample)
        file_obj.seek(0)
        return dialect
