from src.context_manager import *
from src.constants import *
import csv
from itertools import islice, chain
from collections import namedtuple

# file_reader = FileContextManger(fnames)

# with FileContextManger(fnames) as file_reader:
#     for file in file_reader.file_names:
#         with open(file) as f:
#             sample = f.read(2000)
#             dialect = csv.Sniffer().sniff(sample)
#         # print(vars(dialect))
#         # print()
#
#         with open(file) as f:
#             _reader = csv.reader(f, dialect)
#             for row in islice(_reader, 10):
#                 print(row)
#             print()

# with open(fnames[0]) as f:
#     sample = f.read(2000)
#     dialect = csv.Sniffer().sniff(sample)
# print(vars(dialect))
#
# with open(fnames[0]) as f:
#     _reader = csv.reader(f, dialect)
#     for row in islice(_reader, 10):
#         print(row)
#
#
# def create_named_tuple_class(fname, class_name):
#     fields = extract_field_names(fname)
#     return namedtuple(class_name, fields)
#
# def extract_field_names(fname):
#     reader = csv_parser(fname, include_header=True)
#     return next(reader)
#
for fname, parser, class_name in zip(fnames, parsers, class_names):
    with FileContextManager(fname, parser, class_name) as f:
        print(*islice(f, 10000000000), sep='\n')


