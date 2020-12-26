from reader import get_program
from fixer import fix_program


def test_fix_program():
    expected_acc = 8
    expected_next_cmd_id = 9

    program = get_program('test_input.raw')
    acc, next_cmd_id = fix_program(program)

    assert acc == expected_acc
    assert next_cmd_id == expected_next_cmd_id
