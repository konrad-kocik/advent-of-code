from reader import get_program
from runner import run_program
from fixer import fix_program

program_path = 'input.raw'

print('Part 1 acc={}'.format(run_program(get_program(program_path))[0]))
print('Part 2 acc={}'.format(fix_program(get_program(program_path))[0]))
