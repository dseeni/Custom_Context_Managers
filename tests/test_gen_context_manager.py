from itertools import islice


def test_gen_context_manager_exhausts_file(create_gen_context_manager):
    with create_gen_context_manager as f:
        assert len(list(islice(f, 1200))) == 1000
    # make sure the file is closed after exit
    try:
        next(f)
    except StopIteration:
        pass


def test_gen_context_manager_return_values(create_gen_context_manager):
    with create_gen_context_manager as f:
        row = next(f)
        assert row.ssn == '100-53-9824'
        assert row.first_name == 'Sebastiano'


def test_gen_context_manager_headers(create_gen_context_manager):
    with create_gen_context_manager as f:
        assert 'ssn' in dir(next(f))
        assert 'first_name' in dir(next(f))
        assert 'last_name' in dir(next(f))
        assert 'language' in dir(next(f))


def test_file_context_manager_stop_iteration(create_gen_context_manager):
    with create_gen_context_manager as f:
        assert len(list(islice(f, 1200))) == 1000

