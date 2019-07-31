from pytest import fixture
import os
from src.constants import *
from src.context_manager import *


@fixture('session', autouse=True)
def set_test_directory():
    os.chdir('src/')


@fixture('function')
def create_context_manager():
    return FileContextManager(fnames[0], parsers[0], class_names[0])

@fixture('function')
def create_gen_context_manager():
    pass
