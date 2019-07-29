from src.context_manager import *
from src.constants import *
from csv import Sniffer, reader
from itertools import islice

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

with open(fnames[0]) as f:
    sample = f.read(2000)
    dialect = Sniffer().sniff(sample)
print(vars(dialect))

with open(fnames[0]) as f:
    _reader = reader(f, dialect)
    for row in islice(_reader, 10):
        print(row)



