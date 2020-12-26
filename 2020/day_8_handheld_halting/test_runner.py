from reader import get_program
from runner import run_program


def test_run_program():
    expected_acc = 5
    program = get_program('test_input.raw')
    assert run_program(program)[0] == expected_acc
