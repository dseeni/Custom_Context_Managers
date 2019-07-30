from pytest import fixture
import os


@fixture('session', autouse=True)
def set_test_directory():
    os.chdir('src/')


@fixture('function')
def create_context_manager():
    pass
