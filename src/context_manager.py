import csv
from collections import namedtuple


class FileContextManager:
    def __init__(self, file_name, parser, class_name):
        self.file_name = file_name
        self.file_obj = None
        self.reader = None
        self.parser = parser
        self.class_name = class_name

    def __enter__(self):
        self.file_obj = open(self.file_name)
        self.reader = csv.reader(self.file_obj,
                                 self.get_dialect(self.file_obj))
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
    def get_dialect(file_obj):
        sample = file_obj.read(2000)
        dialect = csv.Sniffer().sniff(sample)
        file_obj.seek(0)
        return dialect
