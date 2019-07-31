from src.context_manager import *
from src.gen_context_manager import *
from src.constants import *
import csv
from itertools import islice, chain
from collections import namedtuple

# **************************** Goal 1 ****************************
#
# for fname, parser, class_name in zip(fnames, parsers, class_names):
#     with FileContextManager(fname, parser, class_name) as f:
#         rows.append(next(f))
#
#     print(rows)
#
# print(rows[0].ssn, rows[1].horsepower)

# for fname, parser, class_name in zip(fnames, parsers, class_names):
#     with gen_file_context_manager(fname, parser, class_name) as f:
#         print('39:', *list(islice(f, 100000)), sep='\n')
#         print(next(f))
with gen_file_context_manager(fnames[0], parsers[0], class_names[0]) as f:
    print('39:', len(list(islice(f, 100000))), sep='\n')
