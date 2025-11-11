from debugger import Debugger

print('\nSolving first part of puzzle')
debugger = Debugger('input.raw')
debugger.run_program()
output = debugger.read_output()
print(f'Answer to first part of puzzle is: {output}')

print('\nSolving second part of puzzle')
debugger = Debugger('input.raw')
debugger.copy_program()
initial_register_a = debugger.read_initial_register_a()
print(f'Answer to second part of puzzle is: {initial_register_a}')
