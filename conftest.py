from os import chdir
from pathlib import Path
from pytest import fixture


@fixture(autouse=True)
def change_test_dir(request):
    """ Automatically change the working directory to the test file's directory. """
    test_file_dir = Path(request.fspath).parent
    chdir(test_file_dir)
