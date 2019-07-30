from src.context_manager import *
from src.constants import *
from itertools import islice


def test_file_context_manager_exhausts_file(create_context_manager):
    with create_context_manager as f:
        assert len(list(islice(f, 1200))) == 1000
    # make sure the file is closed after exit
    assert f.file_obj.closed is True
    try:
        next(f)
    except StopIteration:
        pass


def test_file_context_manager_enter_exit(create_context_manager):
    assert '__exit__' and '__enter__' in dir(create_context_manager)


def test_file_context_manager_iter_next(create_context_manager):
    assert '__iter__' and '__next__' in dir(create_context_manager)


def test_file_context_manager_return_values(create_context_manager):
    with create_context_manager as f:
        row = next(f)
        assert row.ssn == '100-53-9824'
        assert row.first_name == 'Sebastiano'


def test_file_context_manager_headers(create_context_manager):
    with create_context_manager as f:
        row = next(f)
        assert 'ssn' in dir(f._nt)
        assert 'first_name' in dir(f._nt)
        assert 'last_name' in dir(f._nt)
        assert 'language' in dir(f._nt)


def test_file_context_manager_stop_iteration(create_context_manager):
    with create_context_manager as f:
        assert len(list(islice(f, 1200))) == 1000

