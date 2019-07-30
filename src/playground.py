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
with FileContextManager(fnames, True) as f:
    # print(*islice(next(f), 100000), sep='\n')
        print(next(f))

# f = FileContextManager(fnames, True)
# print(next(iter(f)))
# print(f.file_objects[0].closed)

# f = open(fnames[0])
# while True:
#     try:
#         print(next(f))
#     except StopIteration:
#         print('stop')
#         break
# for i in range(100000): #     print(next(f))
