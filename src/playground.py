from src.context_manager import *
from src.constants import *
from csv import Sniffer, reader
from itertools import islice

with open(fnames[0]) as f:
    sample = f.read(2000)
    dialect = Sniffer().sniff(sample)
print(vars(dialect))

with open(fnames[0]) as f:
    _reader = reader(f, dialect)
    for row in islice(_reader, 10):
        print(row)
