import csv
from collections import namedtuple
from contextlib import contextmanager
from src.constants import *
from itertools import islice

def get_dialect(file_obj):
    sample = file_obj.read(2000)
    dialect = csv.Sniffer().sniff(sample)
    file_obj.seek(0)
    return dialect


@contextmanager
def gen_file_context_manager(file_name, parser, class_name):
    file_obj = open(file_name)
    reader = csv.reader(file_obj, get_dialect(file_obj))

    def cast_row():
        headers = map(lambda l: l.lower(), next(reader))
        DataTuple = namedtuple(class_name, headers)
        for row in reader:
            row = next(reader)
            zipped = (fn(value) for value, fn in zip(row, parser))
            parsed = DataTuple(*zipped)
            yield parsed
    try:
        yield cast_row()
    finally:
        try:
            next(file_obj)
        except StopIteration:
            pass
        # print('closing file')
        file_obj.close()

for fname, parser, class_name in zip(fnames, parsers, class_names):
    with gen_file_context_manager(fname, parser, class_name) as f:
        print('39:', *list(islice(f, 100000)), sep='\n')
        # print(next(f))


