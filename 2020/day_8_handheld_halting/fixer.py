from copy import deepcopy

from command_factory import transform_command
from runner import run_program


def fix_program(program):
    last_cmd_id = len(program) - 1

    for cmd_id, cmd in enumerate(program):
        fixed_cmd = transform_command(cmd)

        if fixed_cmd:
            fixed_program = deepcopy(program)
            fixed_program[cmd_id] = fixed_cmd
            acc, next_cmd_id = run_program(fixed_program)

            if next_cmd_id > last_cmd_id:
                return acc, next_cmd_id

    raise Exception('Cannot fix the program')
