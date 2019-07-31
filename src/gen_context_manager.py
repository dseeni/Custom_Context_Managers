import csv
from collections import namedtuple
from contextlib import contextmanager


def get_dialect(file_obj):
    sample = file_obj.read(2000)
    dialect = csv.Sniffer().sniff(sample)
    file_obj.seek(0)
    return dialect


@contextmanager
def gen_file_context_manager(file_name, single_parser, single_class_name):
    file_obj = open(file_name)
    reader = csv.reader(file_obj, get_dialect(file_obj))

    def cast_row():
        headers = map(lambda l: l.lower(), next(reader))
        DataTuple = namedtuple(single_class_name, headers)
        while True:
            try:
                row = next(reader)
                zipped = (fn(value) for value, fn in zip(row, single_parser))
                parsed = DataTuple(*zipped)
                yield parsed
            except StopIteration:
                break
    try:
        yield cast_row()
    finally:
        try:
            next(file_obj)
        except StopIteration:
            pass
        # print('closing file')
        file_obj.close()
