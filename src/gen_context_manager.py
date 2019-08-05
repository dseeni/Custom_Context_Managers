import csv
from collections import namedtuple
from contextlib import contextmanager


@contextmanager
def gen_file_context_manager(file_name, single_parser, single_class_name):
    file_obj = open(file_name)
    dialect = csv.Sniffer().sniff(file_obj.read(2000))
    file_obj.seek(0)
    try:
        reader = csv.reader(file_obj, dialect)
        headers = map(lambda l: l.lower(), next(reader))
        DataTuple = namedtuple(single_class_name, headers)
        yield (DataTuple(*(fn(value) for value, fn
                           in zip(row, single_parser))) for row in reader)

    finally:
        try:
            next(file_obj)
        except StopIteration:
            pass
        # print('closing file')
        file_obj.close()
