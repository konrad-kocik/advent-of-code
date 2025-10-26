from debugger import Debugger

print('\nSolving first part of puzzle')
debugger = Debugger()
debugger.initialize('input.raw')
debugger.run_program()
output = debugger.get_output()
print(f'Answer to first part of puzzle is: {output}')
