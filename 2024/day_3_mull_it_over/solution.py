from computer import add_up_results_of_all_instructions_from_memory

print('\nSolving first part of puzzle')
sum_of_results = add_up_results_of_all_instructions_from_memory('input.raw')
print(f'Answer to first part of puzzle is: {sum_of_results}')

print('\nSolving second part of puzzle')
sum_of_results = add_up_results_of_all_instructions_from_memory('input.raw', conditional_statements=True)
print(f'Answer to second part of puzzle is: {sum_of_results}')
