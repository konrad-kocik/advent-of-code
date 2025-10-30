from string_evaluator import count_nice_strings

print('\nSolving first part of puzzle')
nice_strings_count = count_nice_strings('input.raw')
print(f'Answer to first part of puzzle is: {nice_strings_count}')

print('\nSolving second part of puzzle')
nice_strings_count = count_nice_strings('input.raw', new_rules=True)
print(f'Answer to second part of puzzle is: {nice_strings_count}')
